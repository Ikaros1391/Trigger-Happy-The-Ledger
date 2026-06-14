class LowPolyPhysicsComponent:
    def __init__(self):
        self.position = Vector3(0, 0, 0)
        self.velocity = Vector3(0, 0, 0)
        self.is_grounded = True
        self.hover_fuel = 2.0  # Seconds of jet hover
        
    def update_physics(self, delta_time, state):
        # 1. Apply constant low-cost gravity if in air
        if not self.is_grounded and not state.is_hovering:
            self.velocity.y -= STANDARD_GRAVITY * delta_time

        # 2. Check simple trigger volumes (Slag Pools)
        friction_coefficient = 2.5
        if state.is_touching_slag_volume:
            friction_coefficient = 0.15  # Slide amplification
            # Add subtle additive force in the direction she was already moving
            self.velocity += state.move_direction * SLAG_BOOST_FORCE * delta_time

        # 3. Apply friction to horizontal vectors
        self.velocity.x -= self.velocity.x * friction_coefficient * delta_time
        self.velocity.z -= self.velocity.z * friction_coefficient * delta_time

        # 4. Update the low-poly asset's position matrix
        self.position += self.velocity * delta_time

—--------


class SageElementSystem:
    # Keying elements directly to absolute cardinal directions (Shared with Corey)
    ELEMENT_PYRO = 0  # Flick UP
    ELEMENT_VOLT = 1  # Flick RIGHT
    ELEMENT_CRYO = 2  # Flick DOWN
    ELEMENT_SLAG = 3  # Flick LEFT

    def __init__(self):
        self.current_element = self.ELEMENT_PYRO
        self.stick_is_centered = True

    def process_stick_flick(self, stick_x, stick_y, state):
        """Monitors the right stick coordinates for instant element selection."""
        tilt_amount = (stick_x * stick_x) + (stick_y * stick_y)
        if tilt_amount < 0.5:
            self.stick_is_centered = True
            return

        if self.stick_is_centered:
            self.stick_is_centered = False 

            if abs(stick_x) > abs(stick_y):
                self.current_element = self.ELEMENT_VOLT if stick_x > 0 else self.ELEMENT_SLAG
            else:
                self.current_element = self.ELEMENT_PYRO if stick_y > 0 else self.ELEMENT_CRYO
                
            self._apply_visual_glow(state)

    def _apply_visual_glow(self, state):
        """Swaps the low-poly gauntlet core color based on the selected element."""
        if self.current_element == self.ELEMENT_PYRO: state.gauntlet_glow = (1.0, 0.2, 0.0)
        elif self.current_element == self.ELEMENT_VOLT: state.gauntlet_glow = (1.0, 0.9, 0.0)
        elif self.current_element == self.ELEMENT_CRYO: state.gauntlet_glow = (0.0, 0.6, 1.0)
        elif self.current_element == self.ELEMENT_SLAG: state.gauntlet_glow = (0.5, 1.0, 0.0)


class SageIntentMap:
    """
    Sage (The Sorcerer Tank) Intent Map.
    Maps completely different physical behaviors to the exact same muscle memory framework.
    """
    def __init__(self, element_system):
        self.elements = element_system
        self.overclock_timer = 0.0
        self.is_overclocked = False

    def execute_utility(self, state) -> None:
        """Mapped strictly to SQUARE: Deploys Binding Seal Matrices."""
        # Visual feedback: Low-poly runic circle burns into the floor decal
        active_type = self.elements.current_element
        
        if self.is_overclocked:
            # Overclock rule: Instantly detonate a massive elemental shockwave instead of a passive ring
            state.trigger_unstable_matrix_explosion(element=active_type)
        else:
            state.spawn_floor_matrix_volume(element=active_type, radius=4.0)

    def execute_relocation(self, state, left_stick) -> None:
        """Mapped strictly to CIRCLE: Demon Hand Spell / Hydraulic Tackle."""
        if state.is_grounded():
            # GROUNDED: Forward Hydraulic Tackle rams straight through enemy targets
            state.execute_hydraulic_forward_tackle(vector=left_stick)
        else:
            # AIRBORNE: Casts Demon Hand
            target = state.get_closest_grapnel_target_in_view()
            if target and (target.is_frozen() or target.is_environment_anchor()):
                # Immobile Target Rule: Slingshot Sage's massive bulk across the arena
                state.apply_immediate_velocity_impulse(vector=target.direction * SLINGSHOT_FORCE)
                state.reset_hover_timer()  # Refreshes Runic Hover
            elif target:
                # Normal Target Rule: Sage's weight is an anchor; pull the enemy directly to him
                target.yank_to_coordinates(destination=state.position)
                state.auto_queue_aerial_slam_combo(target)

    def execute_counter(self, state) -> None:
        """Mapped strictly to TRIANGLE: Close Utility & Advanced Posture Checks."""
        if state.enemy_is_attacking_in_window():
            # Perfect Frame Advantage Parry: Triggers a snapshot of personal slow-mo
            state.execute_hydraulic_reroute_parry()
            state.grant_zero_startup_frames_on_next_attack()
            return

        if state.enemy_in_melee_range():
            # The Vertical Vault Sequence: Piston release launches Sage vertically
            state.play_animation("anchor_stab_and_piston_vault")
            state.apply_downward_damage_to_enemy()
            state.apply_vertical_impulse(force=HIGH_CLEARANCE)
            state.reset_hover_timer()
        else:
            # Open air tactical safety
            state.execute_quick_shoulder_shove()

    def execute_primary_and_precision(self, state, hold_l2, tap_r2) -> None:
        """Mapped strictly to L2 + R2: The True Charge Strike thesis statement."""
        if hold_l2:
            state.enter_over_the_shoulder_camera()
            if tap_r2 or self.is_overclocked:
                # Full commitment physical payout
                state.play_animation("true_charge_strike_execution")
                state.apply_hitbox(damage=MAX_DAMAGE, hit_stun=MAX_STUN)
        else:
            if tap_r2:
                state.execute_standard_kinetic_brawl_punch()


class SagePhysicsAndStyleLoop:
    """Manages Sage's unique Margin interactions, Combo Gravity, and Overclock Mode."""
    
    def process_incoming_hit(self, state, sage_intent, margin_score):
        """Evaluates armor states to dynamically waive penalties or reward trades."""
        if state.hyper_armor_is_active():
            # Strategic Trade Rule: Waive the penalty entirely for using deliberate armor
            margin_score.waive_hit_penalty()
            if state.attack_connects_in_window():
                margin_score.spike_rank_massively()  # "Perfect Trade" Bonus
        else:
            # Lazy Hit Penalty: Caught off guard, punish the style score
            margin_score.apply_heavy_decay_penalty()

    def update_movement_and_gravity(self, delta_time, state):
        """Handles his Runic Hover and locks physics completely during active combos."""
        if state.is_in_active_combo_sequence():
            # Classic Character-Action Exception: Combos matter more than physics. Freeze gravity!
            state.velocity.y = 0.0
            return

        if state.is_hovering_on_runes():
            state.spawn_low_poly_runic_particles_beneath_boots()
            state.hover_fuel_timer -= delta_time
            if state.hover_fuel_timer <= 0:
                state.terminate_hover_state()
        elif not state.is_grounded():
            # Standard weight calculation drops him down heavily outside of combos/hover
            state.velocity.y -= SAGE_HEAVY_GRAVITY * delta_time

—--

class GlitchElementSystem:
    # Keying elements directly to absolute cardinal directions (Shared Roster Rule)
    ELEMENT_PYRO = 0  # Flick UP    -> High-intensity white-hot damage furnace
    ELEMENT_VOLT = 1  # Flick RIGHT -> Exponential chain-lightning hit-count spike
    ELEMENT_CRYO = 2  # Flick DOWN  -> Frozen targets for data-stream zipping
    ELEMENT_SLAG = 3  # Flick LEFT  -> Zero-gravity acid suspension pools

    def __init__(self):
        self.current_element = self.ELEMENT_PYRO
        self.stick_is_centered = True

    def process_stick_flick(self, stick_x, stick_y, state):
        """Monitors right stick coordinates for instant cardinal element selection."""
        tilt_amount = (stick_x * stick_x) + (stick_y * stick_y)
        if tilt_amount < 0.5:
            self.stick_is_centered = True
            return

        if self.stick_is_centered:
            self.stick_is_centered = False 

            if abs(stick_x) > abs(stick_y):
                self.current_element = self.ELEMENT_VOLT if stick_x > 0 else self.ELEMENT_SLAG
            else:
                self.current_element = self.ELEMENT_PYRO if stick_y > 0 else self.ELEMENT_CRYO
                
            self._apply_digital_color_swap(state)

    def _apply_digital_color_swap(self, state):
        """Swaps digital visor/trail emissive textures instantly based on selection."""
        if self.current_element == self.ELEMENT_PYRO: state.glitch_glow = (1.0, 0.2, 0.0)
        elif self.current_element == self.ELEMENT_VOLT: state.glitch_glow = (1.0, 0.9, 0.0)
        elif self.current_element == self.ELEMENT_CRYO: state.glitch_glow = (0.0, 0.6, 1.0)
        elif self.current_element == self.ELEMENT_SLAG: state.glitch_glow = (0.5, 0.0, 1.0)


class GlitchIntentMap:
    """
    Glitch (The Engineering Phantom) Intent Map.
    Maps reality-bending spatial relocation and time manipulation to the universal framework.
    """
    def __init__(self, element_system):
        self.elements = element_system
        self.has_active_anchor = False
        self.anchor_position = Vector3(0, 0, 0)
        self.anchor_health_snapshot = 100
        self.anchor_cooldown = 0.0
        self.is_overclocked = False

    def execute_utility(self, state) -> None:
        """Mapped strictly to SQUARE: Deploys Magnetic Singularity Fields."""
        active_type = self.elements.current_element
        # Spawns a low-poly black hole decal that violently pulls enemies into one chunk
        state.spawn_singularity_field_volume(element=active_type, duration=4.0)

    def execute_relocation(self, state, left_stick) -> None:
        """Mapped strictly to CIRCLE: Phase-Dash Blinks & Data-Stream Traversal."""
        if state.is_grounded():
            # GROUNDED: Instant forward horizontal teleport blink
            state.execute_phase_dash_blink(vector=left_stick)
        else:
            # AIRBORNE: Tracks targeted nodes or Frozen targets
            target = state.get_closest_grapnel_target_in_view()
            if target and (target.is_frozen() or target.is_environment_anchor()):
                # Data-Stream Zip Rule: Dissolves into code, zips straight through node, preserves full velocity
                state.teleport_through_node_coordinates(target_pos=target.position)
                state.trigger_low_poly_code_shatter_vfx(target)
                state.apply_immediate_velocity_impulse(vector=state.get_forward_vector() * TERMINAL_SPEED)
                state.reset_hover_timer()
            else:
                # Basic Air Blink
                state.execute_phase_dash_blink(vector=left_stick)

    def execute_counter(self, state) -> None:
        """Mapped strictly to TRIANGLE: Rewind Buffer Management & Anchor-Drop Launch."""
        # 1. Post-Hit Override Window Check (Evaluated immediately after taking damage)
        if state.is_inside_post_hit_rewind_window():
            self._execute_data_restore_rewind(state)
            return

        # 2. Standard Stance Check (Ensures no input overlap with melee vaulting templates)
        if not self.has_active_anchor:
            # No Anchor Exists: Drop anchor and execute Quantum Bounce Vertical Launch
            if state.is_grounded():
                self.anchor_position = state.position.copy()
                self.anchor_health_snapshot = state.current_health
                self.has_active_anchor = True
                self.anchor_cooldown = 5.0
                
                # Invert gravity vector instantly to shoot her into the sky
                state.play_animation("anchor_drop_quantum_bounce")
                state.apply_vertical_impulse(force=HIGH_CLEARANCE)
                state.reset_hover_timer()  # Ready for 2-second digital hover
        else:
            # Anchor Already Exists: Direct manual tactical rewind reset
            self._execute_data_restore_rewind(state)

    def _execute_data_restore_rewind(self, state):
        """Instantly warps her physical and mathematical matrix back to the anchor point."""
        state.set_position(self.anchor_position)
        state.current_health = self.anchor_health_snapshot
        state.play_animation("phase_reappear_idle")
        state.trigger_rewind_pixel_vfx()
        
        # Overclock exception check: In the Blender, the anchor remains active infinitely
        if not self.is_overclocked:
            self.has_active_anchor = False
            state.clear_post_hit_window()

    def execute_primary_and_precision(self, state, hold_l2, tap_r2) -> None:
        """Mapped strictly to L2 + R2: Rapid Stacks & Phase Overdrive Beam Cash-out."""
        if hold_l2:
            state.enter_over_the_shoulder_camera()
            # Channels continuous laser beam that forces all data corruption stacks to detonate
            state.channel_phase_overdrive_beam(is_active=True)
        else:
            state.channel_phase_overdrive_beam(is_active=False)
            if tap_r2:
                # Rapid-fire daggers that hit 20 times a second to spike Margin Score
                state.fire_high_frequency_static_discharge_daggers()


class GlitchPhysicsAndStyleLoop:
    """Manages Glitch's fragile Margin Rank, Post-Hit Undo checks, and Overclock Blender."""
    
    def process_incoming_hit(self, state, glitch_intent, margin_score):
        """Enforces hyper-fragility: sets up the post-hit window before shattering score."""
        state.open_post_hit_rewind_window(duration_frames=15)
        
        # Performance Verification check at end of frame
        if state.failed_to_rewind_in_window():
            # Player missed the tight post-hit Triangle window: punish health and zero out rank
            margin_score.shatter_rank_to_zero()
            state.apply_standard_damage_interruption()

    def update_overclock_blender(self, delta_time, glitch_intent):
        """Bypasses standard anchor usage flags to allow infinite 'Blender' teleport loops."""
        if glitch_intent.is_overclocked:
            glitch_intent.has_active_anchor = True  # Enforces anchor state permanently for 10s
            glitch_intent.anchor_cooldown = 0.0

—---

class DebtCollectorAIScale:
    # 3 Distinct AI Behavioral Tiers based on active Margin Rank (D to SSS)
    TIER_BASIC_HUNTER = 0  # Linear patterns, slow flurries, rare slingshots
    TIER_PROF_COLLECTOR = 1 # Active counter-parries, aggressive slingshots
    TIER_APEX_PREDATOR = 2  # Continuous weapon chains, active momentum reads

    @staticmethod
    def calculate_spawn_probability(corey_debt_total) -> float:
        """Scales encounter probability modifier directly based on Corey's outstanding debt."""
        base_chance = 0.05
        debt_scalar = min(corey_debt_total / 100000.0, 0.45) # Cap at 50% max spawn chance
        return base_chance + debt_scalar

    def determine_ai_tier(self, entry_margin_rank) -> int:
        """Evaluates entry rank snapshots to dynamically scale brain complexity fairly."""
        if entry_margin_rank in ["D", "C", "B"]:
            return self.TIER_BASIC_HUNTER
        elif entry_margin_rank in ["A", "S"]:
            return self.TIER_PROF_COLLECTOR
        else: # SS or SSS Rank
            return self.TIER_APEX_PREDATOR


class DebtCollectorIntentMap:
    """
    The Debt Collector (Agile Stalker Mini-Boss) Intent Map.
    Changes physical sword assets dynamically based on declared tactical intentions.
    Provides instant visual 'tells' for high-speed PS2-style action readability.
    """
    def __init__(self, ai_tier):
        self.ai_tier = ai_tier
        self.active_weapon_mesh = "Dormant_Blade"
        self.is_playable_campaign_mode = False
        self.is_overclocked = False

    def execute_utility(self, state, active_element) -> None:
        """Mapped strictly to SQUARE: The Elemental Weapon Augmentation Matrix."""
        if active_element == 3: # SLAG (Flick LEFT) -> Whip-Blade Slag Matrix
            self.active_weapon_mesh = "Coiled_Whip_Blade_Purple"
            state.swap_boss_weapon_mesh(self.active_weapon_mesh)
            state.play_animation("whip_blade_horizontal_sweep")
            state.spawn_floor_matrix_volume(element=3, radius=5.0) # Strips traction
            
        elif active_element == 2: # CRYO (Flick DOWN) -> Odachi Frost Cleave
            self.active_weapon_mesh = "Executioners_Odachi_Cyan"
            state.swap_boss_weapon_mesh(self.active_weapon_mesh)
            state.play_animation("odachi_earth_slam")
            state.spawn_linear_ice_crystal_wave() # Forces deep freeze status
            
        elif active_element == 1: # VOLT (Flick RIGHT) -> Dual Dagger Static Field
            self.active_weapon_mesh = "Monomolecular_Daggers_Yellow"
            state.swap_boss_weapon_mesh(self.active_weapon_mesh)
            state.play_animation("dagger_cross_ground_strike")
            state.spawn_pulsing_static_dome(radius=4.0) # Drains player resources
            
        elif active_element == 0: # PYRO (Flick UP) -> Buster Cleaver Rocket Slag
            self.active_weapon_mesh = "Buster_Cleaver_Orange"
            state.swap_boss_weapon_mesh(self.active_weapon_mesh)
            state.play_animation("cleaver_ground_drag_slice")
            state.spawn_burning_molten_metal_trail() # Damage-over-time hazard

    def execute_relocation(self, state, target_node) -> None:
        """Mapped strictly to CIRCLE: Coiled Whip-Blade Long-Range Slingshot."""
        # Visual Tell: Weapon segments completely into a liquid metallic cord
        self.active_weapon_mesh = "Coiled_Whip_Blade_Open"
        state.swap_boss_weapon_mesh(self.active_weapon_mesh)
        
        # Action: Slingshots his massive bulk through the air, matching Corey's speed
        state.play_animation("whip_blade_slingshot_launch")
        state.apply_immediate_velocity_impulse(vector=target_node.direction * AGILE_BOSS_SPEED)

    def execute_counter(self, state) -> None:
        """Mapped strictly to TRIANGLE: Braced Parry Wall & Vertical Cleaver Rocket Launch."""
        # Visual Tell: Braces the heavy iron slab in front of his chest like a solid wall
        self.active_weapon_mesh = "Buster_Cleaver"
        state.swap_boss_weapon_mesh(self.active_weapon_mesh)

        if state.enemy_is_attacking_in_window():
            if self.ai_tier >= DebtCollectorAIScale.TIER_PROF_COLLECTOR:
                # Active Counter: Hydraulic parry breaks Corey's focus, decaying her Margin Rank
                state.execute_hydraulic_cleaver_parry()
                state.queue_immediate_shotgun_counter_strike()
            return

        if state.enemy_in_melee_range():
            # Vertical Clearance Sequence: Rocket engine on back of cleaver detonates downward
            state.play_animation("cleaver_stab_and_rocket_launch")
            state.apply_downward_damage_to_player()
            state.apply_vertical_impulse(force=HIGH_CLEARANCE)
        else:
            state.execute_quick_cleaver_shove()

    def execute_primary_and_precision(self, state, hold_l2, tap_r2) -> None:
        """Mapped strictly to L2 + R2: The Executioner's Odachi / Dual Dagger Flurry / Cleaver Blast."""
        if hold_l2:
            # MAXIMUM DAMAGE STATE (The Ultimate Tell)
            # Visual Tell: Stands completely still, entering an over-the-shoulder targeting camera
            self.active_weapon_mesh = "Executioners_Odachi"
            state.swap_boss_weapon_mesh(self.active_weapon_mesh)
            
            if tap_r2:
  

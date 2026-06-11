from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ==============================================================================
# FINANCIAL AUDIT CONSTANTS
# ==============================================================================
WALL_BREAK_PENALTY = 500.0
GLASS_SHATTER_PENALTY = 150.0
LIQUIDITY_CRISIS_INTEREST_TICK = 25.0

# ==============================================================================
# SYSTEM ENUMS AND DATA STRUCTURES
# ==============================================================================
class Element(Enum):
    SLAG = auto()
    PYRO = auto()
    CRYO = auto()
    VOLT = auto()

@dataclass
class PlayerState:
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    health: float = 100.0
    active_element: Element = Element.SLAG
    reaper_gauge: float = 0.0
    reaper_mode_active: bool = False
    margin_points: float = 150.0
    margin_rank: str = "C"
    l2_hold_duration: float = 0.0
    is_airborne: bool = False
    time_dilation: float = 1.0
    current_charge_tier: int = 0
    is_charging: bool = False
    is_shopping: bool = False
    status_effects: List[str] = field(default_factory=list)
    metadata: Dict[str, any] = field(default_factory=lambda: {
        "frame_config": "Dual_Pistols",
        "combo_history": [],
        "buffer_timer": 0.0,
        "in_dead_state_buffer": False,
        "has_target_lock": False,
        "right_stick_flick_locked": False,
        "currently_sliding": False,
        "aerial_momentum_modifier": 1.0,
        "hover_boots_engaged": False,
        "perfect_cancel_window_active": False,
        "charge_elapsed_time": 0.0,
        "pressure_stored": False
    })

@dataclass
class UpgradeMatrix:
    max_health: float = 100.0
    max_armor_slots: int = 1
    current_armor_plates: int = 1
    purchased_skills: List[str] = field(default_factory=list)
    max_teleports_per_anchor: int = 1

@dataclass
class RebalancedCanisters:
    max_charges: int = 3
    current_charges: int = 3
    recharge_timer: float = 0.0
    cooldown_per_charge: float = 6.0

@dataclass
class LevelPerformanceMetrics:
    walls_broken: int = 0
    glass_shattered: int = 0
    seconds_in_liquidity_crisis: int = 0
    zen_van_calls: int = 0

@dataclass
class AuditorHeavyState:
    name: str = "The Auditor (Heavy Class)"
    weight_class: str = "Bruiser"
    health: float = 2500.0
    overdrive_stacks: int = 0
    max_overdrive_stacks: int = 3

# ==============================================================================
# INTENT CONTROLLER INTERFACE
# ==============================================================================
class IIntentController:
    def press_r2(self, state: PlayerState, upgrades: UpgradeMatrix = None) -> str: 
        raise NotImplementedError
    def press_l2(self, state: PlayerState, hold_time: float) -> str: 
        raise NotImplementedError
    def press_triangle(self, state: PlayerState, hold: bool, upgrades: UpgradeMatrix = None) -> str: 
        raise NotImplementedError
    def press_square(self, state: PlayerState) -> str: 
        raise NotImplementedError
    def press_circle(self, state: PlayerState) -> str: 
        raise NotImplementedError
    def flick_right_stick(self, state: PlayerState, direction: str) -> str: 
        raise NotImplementedError

# ==============================================================================
# COREY CONTROLLER IMPLEMENTATION (THE REAPER MARGIN SIGNATURE CHARACTER)
# ==============================================================================
class CoreyController(IIntentController):
    """ Cordelia Cross (Code Name: Reaper). Wields the transforming Chimaera Frame. """
    
    def _track_variety(self, state: PlayerState, current_move: str) -> float:
        history = state.metadata["combo_history"]
        if state.margin_rank == "SSS":
            return 1.0
        if current_move in history:
            return 0.0
        history.append(current_move)
        if len(history) > 4:
            history.pop(0)
        return 1.0

    def _get_frame_and_personality_modifier(self, state: PlayerState) -> str:
        """ Returns frame data style and behavioral context based on performance tier. """
        if state.reaper_mode_active:
            return "[FRAME METRIC: ZERO-FRAME SNAP CANCEL // COREY STATUS: ABSOLUTE SILENCE (CYBERNETIC OVERCLOCK)]"
        
        rank = state.margin_rank
        if rank in ["SSS", "SS"]:
            return "[FRAME METRIC: ULTRA-EFFICIENT MINIMALIST REC WINDOW // COREY STATUS: COLD EX-MILITARY REAPER MINDSET]"
        elif rank in ["S", "A"]:
            return "[FRAME METRIC: STANDARD CORPORATE TELEMETRY // COREY STATUS: DISCIPLINED MILITARY CALLOUTS]"
        else:
            return "[FRAME METRIC: HEAVY FRUSTRATED REC DELAY // COREY STATUS: AGGRESSIVE SARCASM AND SWEARING]"

    def press_r2(self, state: PlayerState, upgrades: UpgradeMatrix = None) -> str:
        config = state.metadata.get("frame_config", "Dual_Pistols")
        variety_mod = self._track_variety(state, f"R2{config}")
        frame_context = self._get_frame_and_personality_modifier(state)
        
        if state.reaper_mode_active:
            payloads = {
                Element.SLAG: "Acid rounds shred enemy armor value.",
                Element.PYRO: "Pyro rounds trigger continuous thermal loops.",
                Element.CRYO: "Cryo rounds instantly flash-freeze targets into anchors.",
                Element.VOLT: "Volt rounds ignite tesla arcs to erase enemy shields."
            }
            return f"⚡ REAPER ACTIVE -> Assault Rifle Form: Spraying automated hitscan {payloads[state.active_element]} {frame_context}"
        
        if config == "Dual_Pistols":
            state.margin_points += 50 * variety_mod
            return f"Reaper fires snappy ballistic pistol rounds. [Variety Mod: {variety_mod}x] {frame_context}"
        elif config == "Shotgun":
            state.margin_points += 80 * variety_mod
            return f"Reaper fires heavy ballistic Shotgun spread. High knockback impact. [Variety Mod: {variety_mod}x] {frame_context}"
        elif config == "Sniper":
            state.metadata["frame_config"] = "Dual_Pistols"
            state.margin_points += 200 * variety_mod
            return f"🎯 SNIPER FIRE: Massive high-velocity anti-material slug discharged. Resetting stance. [Variety Mod: {variety_mod}x] {frame_context}"
        
        return "Reaper fires physical ballistic round."

    def press_l2(self, state: PlayerState, hold_time: float) -> str:
        state.l2_hold_duration = hold_time
        frame_context = self._get_frame_and_personality_modifier(state)
        
        if state.reaper_mode_active:
            current = state.metadata.get("frame_config", "Dual_Pistols")
            next_form = "Shotgun" if current == "Dual_Pistols" else "Dual_Pistols"
            state.metadata["frame_config"] = next_form
            return f"🔄 REAPER FORM SNAP: Shifting barrel loops instantly to {next_form}. {frame_context}"
        
        if hold_time >= 0.35:
            state.metadata["frame_config"] = "Sniper"
            if state.is_airborne:
                state.time_dilation = 0.25
                return f"🎯 SNIPER ENGAGED: Camera zooms over shoulder. Midair BULLET TIME active. {frame_context}"
            return f"🎯 SNIPER ENGAGED: Grounded precision posture locked. No time dilation. {frame_context}"
        
        # Clean escape if player triggers a regular toggle switch while in Sniper state
        current = state.metadata.get("frame_config", "Dual_Pistols")
        if current == "Sniper":
            current = "Dual_Pistols"
            
        next_form = "Shotgun" if current == "Dual_Pistols" else "Dual_Pistols"
        state.metadata["frame_config"] = next_form
        return f"Reaper pneumatically changes configuration to {next_form} Form. {frame_context}"

    def press_triangle(self, state: PlayerState, hold: bool, upgrades: UpgradeMatrix = None) -> str:
        variety_mod = self._track_variety(state, "Triangle_Sledge")
        state.margin_points += 100 * variety_mod
        frame_context = self._get_frame_and_personality_modifier(state)
        
        if state.is_airborne:
            state.metadata["hover_boots_engaged"] = True
            return f"Reaper deploys Sledge Rig: Hover Boots engage, locking vertical Z-axis. {frame_context}"
        if hold:
            return f"Reaper ignites Sledge Rig rocket booster for a heavy committed impact smash. {frame_context}"
        return f"Reaper snaps Sledge Rig out for a quick frame-cancel Bayonet Parry. {frame_context}"

    def press_square(self, state: PlayerState) -> str:
        variety_mod = self._track_variety(state, f"Square{state.active_element.name}")
        state.margin_points += 60 * variety_mod
        frame_context = self._get_frame_and_personality_modifier(state)
        
        payloads = {
            Element.SLAG: "Launches Slag fluid canister. Covers floor in armor-reducing chemical slick.",
            Element.PYRO: "Launches Pyro igniter canister. Blasts high-thermal payload to detonate Slag.",
            Element.CRYO: "Launches Cryo coolant canister. Flash-freezes targets into solid grapple anchors.",
            Element.VOLT: "Launches Ionized Volt canister. Strips shields and electrifies standing Slag pools."
        }
        return f"Reaper throws payload: {payloads[state.active_element]} {frame_context}"

    def press_circle(self, state: PlayerState) -> str:
        frame_context = self._get_frame_and_personality_modifier(state)
        if state.is_airborne or state.metadata.get("has_target_lock", False):
            if state.metadata.get("hover_boots_engaged", False):
                state.metadata["hover_boots_engaged"] = False
                state.time_dilation = 1.0
return f"🪝 HOVER ZIP BREAK: Reaper fires her Grapple Zip cable! Winch tension cuts Hover Boots. {frame_context}"
if state.active_element == Element.SLAG:
state.metadata["currently_sliding"] = True
return f"Reaper drops into a low, high-velocity Acid Slide. (2.0x Momentum Active) {frame_context}"
return f"Reaper drops into a standard directional Ground Slide. {frame_context}"
def flick_right_stick(self, state: PlayerState, direction: str) -> str:
if state.metadata.get("right_stick_flick_locked", False):
return "Flick ignored: Camera tracking overrides element assignment during rifle scope lock."
directions = {"UP": Element.CRYO, "DOWN": Element.SLAG, "LEFT": Element.VOLT, "RIGHT": Element.PYRO}
if direction in directions:
state.active_element = directions[direction]
return f"🔄 CHAMBER ROTATED: Active load indexed to {state.active_element.name}."
return "Stick centered."
==============================================================================
ALTERNATE ROSTER CHARACTER IMPLEMENTATIONS
==============================================================================
class DebtCollectorController(IIntentController):
def press_r2(self, state: PlayerState, upgrades: UpgradeMatrix = None) -> str:
return "Debt Collector draws The Executioner's Odachi for massive horizontal physical slashes."
def press_l2(self, state: PlayerState, hold_time: float) -> str:
if hold_time >= 0.35:
return "Debt Collector enters Dual Blade Deflection Sprint: Total invulnerability to frontal projectiles."
return "Debt Collector draws Monomolecular Dual Daggers, preparing quick counter-slashes."
def press_triangle(self, state: PlayerState, hold: bool, upgrades: UpgradeMatrix = None) -> str:
if hold:
return "Debt Collector draws Buster Cleaver for an unblockable, rocket-boosted overhead plunge strike."
return "Debt Collector snaps Buster Cleaver out for an immediate, high-stagger Pommel Strike frame cancel."
def press_square(self, state: PlayerState) -> str:
element_effects = {
Element.SLAG: "Lays a circular slick of chemical oil, multiplying local movement velocity by 2.0x.",
Element.PYRO: "Swings ignited whip outward creating a tracking 3m firewall barrier.",
Element.CRYO: "Latches onto target, forcing an instant flash-freeze status constraint.",
Element.VOLT: "Drives whip into floor, shocking a 5m radius to completely knock players out of hover states."
}
return f"Debt Collector throws Coiled Whip-Blade: {element_effects[state.active_element]}"
def press_circle(self, state: PlayerState) -> str:
return "Debt Collector draws Curved Scimitar for an evasive, invincibility-frame lateral Ghost Step."
def flick_right_stick(self, state: PlayerState, direction: str) -> str:
directions = {"UP": Element.CRYO, "DOWN": Element.SLAG, "LEFT": Element.VOLT, "RIGHT": Element.PYRO}
if direction in directions:
state.active_element = directions[direction]
return f"⚔️ BLADE INDEXED: Debt Collector attunes his active sword steel to {state.active_element.name}."
return "Stance centered."
class SageController(IIntentController):
def press_r2(self, state: PlayerState, upgrades: UpgradeMatrix = None) -> str:
if state.metadata.get("pressure_stored", False):
state.metadata["pressure_stored"] = False
state.is_charging = False
state.current_charge_tier = 0
state.metadata["perfect_cancel_window_active"] = False
return "💥 PRESSURE DISCHARGE! Sage skips wind-up and instantly unleashes a MAX TIER 3 True Charge Strike!"
if not state.is_charging:
state.is_charging = True
state.current_charge_tier = 1
state.metadata["charge_elapsed_time"] = 0.0
state.metadata["perfect_cancel_window_active"] = True
return "Sage begins charging True Charge Strike. Tier 1 Active (Hyper-Armor engaged). [GOLD FLASH WINDOW]"
tick_rate = 0.1
state.metadata["charge_elapsed_time"] = state.metadata.get("charge_elapsed_time", 0.0) + tick_rate
time_held = state.metadata["charge_elapsed_time"]
if 0.4 <= time_held < 0.55:
if state.current_charge_tier < 2:
state.current_charge_tier = 2
state.metadata["perfect_cancel_window_active"] = True
return "Sage continues charging. Upgraded to Tier 2. [GOLD FLASH WINDOW]"
elif time_held >= 0.8:
if state.current_charge_tier < 3:
state.current_charge_tier = 3
state.metadata["perfect_cancel_window_active"] = True
return "Sage hits absolute limit! Upgraded to Tier 3 MAX. [GOLD FLASH WINDOW]"
elif time_held >= 0.95:
state.metadata["perfect_cancel_window_active"] = False
return f"Sage holding heavy stance... (Tier {state.current_charge_tier})"
def press_l2(self, state: PlayerState, hold_time: float) -> str:
if state.is_charging:
if state.metadata.get("perfect_cancel_window_active", False):
state.metadata["perfect_cancel_window_active"] = False
state.metadata["pressure_stored"] = True
state.is_charging = False
bonus = state.current_charge_tier * 25
return f"⚡ PERFECT HYDRAULIC RE-ROUTE! Stance canceled into forward Tackle! Next action inherits Tier 3 properties and deals +{bonus}% impact damage."
state.is_charging = False
state.current_charge_tier = 0
state.metadata["perfect_cancel_window_active"] = False
return "Sage panic-cancels into a regular tackle. Kinetic pressure safely vented. Stance reset to neutral."
if hold_time >= 0.35:
return "Sage locks into Unyielding Bulwark Posture: Becomes completely un-knockbackable while taking 50% reduced health damage."
return "Sage enters Iron Fortress Stance to absorb incoming physical impacts."
def press_triangle(self, state: PlayerState, hold: bool, upgrades: UpgradeMatrix = None) -> str:
state.metadata["pressure_stored"] = False
state.metadata["perfect_cancel_window_active"] = False
if hold:
return "Sage plants feet and releases a 360-degree Rupture Cleave."
return "Sage enters fast Apex Sheathe Stance to reset animation frames instantly."
def press_square(self, state: PlayerState) -> str:
state.metadata["pressure_stored"] = False
element_effects = {
Element.SLAG: "Erupts sticky Slag mud pool, scrambling enemy attack tracking vectors.",
Element.PYRO: "Drives gauntlet down, erupting high-pressure geothermal cracks.",
Element.CRYO: "Flash-freezes ground, forcing enemies onto their backs into hard physics anchors.",
Element.VOLT: "Turns ground piston into a Tesla Rod, auto-stunning melee attackers on tackle."
}
return f"Sage punches earth with Tectonic Anchor: {element_effects[state.active_element]}"
def press_circle(self, state: PlayerState) -> str:
state.metadata["pressure_stored"] = False
return "Sage executes a short directional Pivot Slide to re-orient heavy attack posture."
def flick_right_stick(self, state: PlayerState, direction: str) -> str:
directions = {"UP": Element.CRYO, "DOWN": Element.SLAG, "LEFT": Element.VOLT, "RIGHT": Element.PYRO}
if direction in directions:
state.active_element = directions[direction]
return f"⚙️ GAUNTLET PRESSURE ROUTED: Internal alchemical hydraulics set to {state.active_element.name}."
return "Hydraulics normalized."
class GlitchController(IIntentController):
def press_r2(self, state: PlayerState, upgrades: UpgradeMatrix = None) -> str:
return "Glitch unloads Static Discharge Daggers, stacking Data Corruption on hostiles."
def press_l2(self, state: PlayerState, hold_time: float) -> str:
if hold_time >= 0.35:
return "Glitch overclocks the beam: Linking all active targets and causing continuous data compression damage."
return "Glitch fires Phase Overdrive beam, linking corrupted targets and snapping them into a single tight cluster."
def press_triangle(self, state: PlayerState, hold: bool, upgrades: UpgradeMatrix = None) -> str:
matrix = upgrades if upgrades else UpgradeMatrix()
is_on_cooldown = state.metadata.get("tether_on_lockdown", False)
cooldown_remaining = state.metadata.get("tether_cooldown_timer", 0.0)
if is_on_cooldown:
if cooldown_remaining <= 0.0:
state.metadata["tether_on_lockdown"] = False
is_on_cooldown = False
else:
return f"⚠️ SYSTEM ERROR: Rewind Engine overheated. Anchor deployment locked for {cooldown_remaining:.1f}s."
if not hold:
if state.metadata.get("anchor_active", False):
state.position = state.metadata["anchor_position"]
state.health = state.metadata["anchor_health"]
state.metadata["remaining_teleport_charges"] -= 1
charges_left = state.metadata["remaining_teleport_charges"]
if charges_left <= 0:
state.metadata["anchor_active"] = False
state.metadata.pop("anchor_position", None)
state.metadata.pop("anchor_health", None)
state.metadata["tether_on_lockdown"] = True
state.metadata["tether_cooldown_timer"] = 15.0
return f"Rewind Buffer activated! Glitch teleports to {state.position}. ❌ ANCHOR SHATTERED: System enters a 15s lockdown phase!"
return f"Rewind Buffer activated! Glitch teleports to {state.position}. 💾 TETHER STABLE: [{charges_left}] charges remain."
return "Glitch executes a rapid local timeline glitch to skip past recovery frames."
if state.metadata.get("tether_on_lockdown", False):
return f"❌ DEPLOY REFUSED: Anchor matrix is currently cooling down ({state.metadata['tether_cooldown_timer']:.1f}s remaining)."
state.metadata["anchor_active"] = True
state.metadata["anchor_position"] = state.position
state.metadata["anchor_health"] = state.health
state.metadata["remaining_teleport_charges"] = matrix.max_teleports_per_anchor
return f"Glitch drops a digital Rewind Buffer hologram at {state.position}. Charge pool initialized to [{matrix.max_teleports_per_anchor}]."
def press_square(self, state: PlayerState) -> str:
element_effects = {
Element.SLAG: "Blasts oil mist over cluster. Passing bullets instantly trigger a massive firestorm zone.",
Element.PYRO: "Triggers a rapid explosive resonance detonation across all linked targets.",
Element.CRYO: "Flash-freezes clustered group into a giant physics anchor for grapple slingshots.",
Element.VOLT: "Fires high-frequency voltage loop, arcing exponentially across the compact pile to delete shields."
}
return f"Glitch deploys System Purge Canister into crowd: {element_effects[state.active_element]}"
def press_circle(self, state: PlayerState) -> str:
return "Glitch performs a zero-frame Quantum Blink directly into the enemy cluster's blind spot."
def flick_right_stick(self, state: PlayerState, direction: str) -> str:
directions = {"UP": Elem

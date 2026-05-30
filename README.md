Scalable control scheme abstraction for character action games. Most franchises reinvent their input mapping every iteration, forcing players to relearn fundamentals. This framework locks intent-based controls while supporting radical mechanical variation across characters.

Core Concept:
Five input slots define intent, not action. Circle is repositioning (dodge, dash, teleport—whatever). R2 is primary attack. L2 is secondary/extend. Triangle is melee. Square is utility. Same inputs, infinite implementations.

Proof of Concept: character schema to be added soon

Corey: Balanced modular weapon swaps
Debt Collector: Multi-tool telegraphing (same intents, different swords)
Sage: Heavy, committed, reading-based
Glitch: High mobility, crowd correction
Zen: Area control, status effects, deception
Why It Matters:
"This solves the scalability problem that franchises like Devil May Cry face. You can support infinite characters without bloating controls or forcing players to relearn every iteration."





# 📑 MASTER GAME DESIGN DOCUMENT: PROJECT REDGRAVE

### Project Title: TRIGGER HAPPY: THE LEDGER
### License: Creative Commons Zero (CC0) - Public Domain (Free to use, mod, code, or sell)

---

## 📌 1. THE THIRDPERSON KINETIC CAMERA BLUEPRINT

To facilitate an aggressive, unbroken momentum loop across both combat and traversal, the camera decouples from the player's shoulder, utilizing a wide-angle Dynamic Spring-Arm System.

- **Standard State:** Arm Length: 4.5 meters | FOV: 85°. Balanced spatial awareness.
- **Momentum State (Slide/Grapple):** Arm smoothly interpolates to 6.5 meters | FOV: 105°. Introduces high-velocity widescreen distortion.
- **Vertical State (Bayonet Vault):** Camera lags behind vertical Z-axis climb and tilts downward 25°, keeping the arena floor and incoming targets fully visible.

---

## 🎮 2. THE CHIMAERA FRAME & DUAL-TRACK CONTROL LAYOUT

To optimize production scopes and eliminate heavy 3D asset switching overhead, Corey does not carry separate weapons. Instead, she wields the **Chimaera Frame**—a single, modular tool that pneumatically telescopes, folds, and reconfigures its physical shape mid-combo. This enables instantaneous, zero-frame asset animation cancels.

- **R2 / RT (Gun-Fu Form):** Fire Equipped Weapon Form (Pistols / Shotgun).
- **L2 / LT:** Tap: Toggle Frame configuration between Dual Pistols and Shotgun | Hold: Extend barrel into Anti-Material Rifle Form.
- **Triangle / Y (Heavy Tool Form):** Deploy Sledge Rig (Tap: Bayonet Melee / Parry | Hold: Rear Rocket Booster Ignite | Mid-Air: Hover Boots Configuration).
- **Square / X:** Grenade Bumper (Launches Cooldown-Based Elemental Canisters directly through the frame's injection lines).
- **Circle / B:** Contextual Traversal Suite (Ground: High-Velocity Slide | Air/Locked: Grapple Zip Cable).
- **D-Pad:** Cycle Active Core Element (Kinetic, Slag, Cryo, Volt) to re-route elemental payloads through the frame.
- **L3 + R3:** Activate Reaper Mode Overclock.

---

## 🧪 3. THE HAZMAT MATRIX & GRENADE COMBOS

Corey's Chimaera Frame always outputs standard Kinetic ballistic damage by default, while the D-Pad sets the elemental chamber of her Square Grenade Bumper.

- **Kinetic (Default):** Flat environmental damage. Instantly shatters Status_Frozen targets into a 300-damage piercing shrapnel area-of-effect.
- **Slag Fluid:** Deploys a 6-meter oil slick. Corey's slide length and velocity are multiplied by 2.0x across it. Shooting it with kinetic rounds creates a 40 fire DPS napalm trap.
- **Cryo Coolant:** Flash-freezes targets. Freezing an airborne target turns them into a stationary physics anchor the Chimaera Frame can Grapple Zip ( Circle ) off of to slingshot across gaps.
- **Ionized Volt:** Strips corporate energy shields. Firing it into a Slag pool electrifies the surface for 25 lightning DPS, allowing Corey to safely hover above using her Hover Boots ( Triangle ).

---

## 📊 4. THE PERFORMANCE AUDIT ENGINE (PAE)

Traditional "Style Ranks" are rebranded into real-time corporate operational efficiency tracking, displayed via a floating 3D spatial ring around Corey's feet.

- **D-B Rank [Liquidity Crisis]:** Spatial Ring pulses neon red. Real-time interest penalties actively accrue debt as handlers penalize messy, slow combat.
- **A-S Rank [Compliant Operation]:** Spatial Ring stabilizes into solid, military white. Normal telemetry rules apply.
- **SS-SSS Rank [The Reaper Margin]:** Screen shifts to an amber night-vision tactical overlay. Audio cuts low frequencies for a heavy sub-bass heart-rate pulse. The corporate AI grants an operational subsidy, freezing all property damage ledger penalties for 30 seconds.

---

## 📈 5. MASTER ECONOMY BALANCING & THE "TAUNT" FORMULA

### Financial Ledger Rules

To protect the player's core survival loop and upgrade path from being choked out by poor performance penalties, the financial engine strictly isolates liquid spending currency from long-term damage penalties:

- **Cash-In-Hand:** Sourced directly from enemy drops and bounty completions. This currency is used exclusively at vending machines/shops for immediate upgrades (stimpaks, armor replacements, weapon mods). It is **never** directly drained by performance or property penalties during a level.
- **Global Lifetime Debt:** A persistent, overarching negative balance. Accrued structural damage and interest penalties are tracked separately and applied to this total only during the End-of-Level Financial Audit.

### Economy Variables & Math Constants

```python
STARTING_DEBT = 4502001.05
WALL_BREAK_PENALTY = 2500.00
GLASS_SHATTER_PENALTY = 150.00
LIQUIDITY_CRISIS_INTEREST_TICK = 10.00  # Added per second spent in D-B rank
ELITE_BOUNTY_DROP = 50000.00          # Added straight to Cash-In-Hand

ZEN_BASE_MARKUP = 1.25
ZEN_IMPATIENCE_MARKUP = 1.35
```

### The End-of-Level Financial Audit Engine

```python
def Calculate_Level_End_Audit(level_performance, current_global_debt):
    """
    Calculates operational penalties gathered during the level and applies 
    them to the persistent global debt ledger without affecting Cash-In-Hand.
    """
    # 1. Structural Damage Computations
    property_damage = (level_performance.walls_broken * WALL_BREAK_PENALTY) + \
                      (level_performance.glass_shattered * GLASS_SHATTER_PENALTY)
    
    # 2. Performance Interest Penalties (Time spent in D-B Ranks)
    interest_penalty = level_performance.seconds_in_liquidity_crisis * LIQUIDITY_CRISIS_INTEREST_TICK
    
    # 3. Calculate Debt Accrued for Current Level
    level_debt_accrued = property_damage + interest_penalty
    
    # 4. Post to Persistent Corporate Ledger
    new_global_lifetime_debt = current_global_debt + level_debt_accrued
    
    # 5. Return updated values to Trigger Settlement Matrix User Interface
    # Player chooses how much Cash-In-Hand to pay toward debt vs. hoarding for upgrades
    return level_debt_accrued, new_global_lifetime_debt
```

### The Active Combat Taunt Execution

```python
def Process_Taunt_Input(player_state, style_points):
    if player_state.is_shopping:
        # The Impatience Cutoff
        trigger_animation("Weapon_Cock")
        audio_mixer.stop_voice_line()
        style_decay_rate = 0.0          # Freeze style meter decay
        global_shop_markup = ZEN_IMPATIENCE_MARKUP
        open_shop_menu_instantly()
    else:
        # Standard Combat Taunt
        trigger_animation("Middle_Finger_To_Anomaly")
        style_points += 150             # Gives active style burst
        enemy_aggro_radius *= 1.5       # Enemies become faster and hit harder
```

---

## 👾 6. TARGET ENEMY & BOSS ROSTER

1. **The Liquidator (Swarmer):** Extreme vulnerability to Slag + Fire combos. Runs at the player in groups of 8.
2. **The Compliance Officer (Bruiser):** Immune to frontal hitscan. Shield must be flash-frozen with Cryo or out-flanked via a Shotgun-boosted Slide.
3. **The Foreclosure Drone (Aerial Sniper):** Suspended by cyber-sigils. Must be yanked down using the Grapple Hook ( Circle ) or picked off with the Anti-Material Rifle ( L2 + R2 ).
4. **The Actuary (Disruptor Mage):** Levitating bookkeepers. Casts hexes that freeze your Style Meter. Barrier drops instantly when hit by Ionized Volt.
5. **The Debt Collector (Elite Stalker):** Spawns when debt ledger rises too high. High agility assassins. Can only be damaged during recovery frames via a timed Bayonet Parry ( Triangle ).
6. **The Auditor (Mechanical Minotaur):** Charges blindly, destroying walls and spiking your debt. Tricking it into hitting columns exposes a weak point on its back.
7. **BOSS: The Liquidity Pool (The Final Anomaly):** A massive entity made of sentient black ledger ink. It mimics Corey's entire movement suite (slides, grapples, weapon swaps). Corey must push her rank into *The Reaper Margin* to pierce its defense.

---

## 🔓 PUBLIC DOMAIN USE TERMS

This project is dedicated to the public domain under CC0. Take this documentation and use it for standalone indie games, total conversion mods (GZDoom/Ultrakill), or commercial projects. No strings attached. Let's get this built.

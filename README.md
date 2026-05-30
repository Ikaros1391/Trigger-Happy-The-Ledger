# 📑 MASTER GAME DESIGN DOCUMENT: PROJECT REDGRAVE
### Project Title: TRIGGER HAPPY: THE LEDGER
### License: Creative Commons Zero (CC0) - Public Domain (Free to use, mod, code, or sell)

## 📌 1. THE THIRDPERSON KINETIC CAMERA BLUEPRINT
To facilitate an aggressive, unbroken momentum loop across both combat and traversal, the camera decouples from the player's shoulder, utilizing a wide-angle Dynamic Spring-Arm System.

*   **Standard State:** Arm Length: 4.5 meters | FOV: 85°. Balanced spatial awareness.
*   **Momentum State (Slide/Grapple):** Arm smoothly interpolates to 6.5 meters | FOV: 105°. Introduces high-velocity widescreen distortion.
*   **Vertical State (Bayonet Vault):** Camera lags behind vertical Z-axis climb and tilts downward 25°, keeping the arena floor and incoming targets fully visible.

## 🎮 2. HIGH-LEVEL DUAL-TRACK CONTROL LAYOUT
*   **R2 / RT:** Fire Equipped Weapon (Pistols / Shotgun).
*   **L2 / LT:** Tap: Toggle Pistols-Shotgun | Hold: Aim Anti-Material Rifle.
*   **Triangle / Y:** Sledge Rig (Tap: Bayonet Melee / Parry | Hold: Rocket | Mid-Air: Hover Boots).
*   **Square / X:** Grenade Bumper (Launches Cooldown-Based Elemental Canisters).
*   **Circle / B:** Contextual Traversal Suite (Ground: Slide | Air/Locked: Grapple Zip).
*   **D-Pad:** Select Active Element (Kinetic, Slag, Cryo, Volt).
*   **L3 + R3:** Activate Reaper Mode Overclock.

## 🧪 3. THE HAZMAT MATRIX & GRENADE COMBOS
Corey's primary firearms always deal Kinetic damage, while the D-Pad sets the element of her `Square` Grenade Bumper.
*   **Kinetic (Default):** Flat environmental damage. Instantly shatters `Status_Frozen` targets into a 300-damage piercing shrapnel area-of-effect.
*   **Slag Fluid:** Deploys a 6-meter oil slick. Corey's slide length and velocity are multiplied by 2.0x across it. Shooting it with kinetic rounds creates a 40 fire DPS napalm trap.
*   **Cryo Coolant:** Flash-freezes targets. Freezing an airborne target turns them into a stationary physics anchor Corey can Grapple Zip (`Circle`) off of to slingshot across gaps.
*   **Ionized Volt:** Strips corporate energy shields. Firing it into a Slag pool electrifies the surface for 25 lightning DPS, allowing Corey to safely hover above using her Hover Boots (`Triangle`).

## 📊 4. THE PERFORMANCE AUDIT ENGINE (PAE)
Traditional "Style Ranks" are rebranded into real-time corporate operational efficiency tracking, displayed via a floating 3D spatial ring around Corey's feet.
*   **D-B Rank [Liquidity Crisis]:** Spatial Ring pulses neon red. Real-time interest penalties actively drain currency as handlers penalize messy, slow combat.
*   **A-S Rank [Compliant Operation]:** Spatial Ring stabilizes into solid, military white. Normal telemetry rules apply.
*   **SS-SSS Rank [The Reaper Margin]:** Screen shifts to an amber night-vision tactical overlay. Audio cuts low frequencies for a heavy sub-bass heart-rate pulse. The corporate AI grants an operational subsidy, freezing all property damage ledger penalties for 30 seconds.

## 📈 5. MASTER ECONOMY BALANCING & THE "TAUNT" FORMULA
```python
STARTING_BALANCE         = 4502001.05
WALL_BREAK_PENALTY       = 2500.00
GLASS_SHATTER_PENALTY    = 150.00
ELITE_BOUNTY_DROP        = -50000.00 

ZEN_BASE_MARKUP          = 1.25  
ZEN_IMPATIENCE_MARKUP    = 1.35  

def Process_Taunt_Input(player_state, style_points):
    if player_state.is_shopping:
        # The Impatience Cutoff
        trigger_animation("Weapon_Cock")
        audio_mixer.stop_voice_line()
        style_decay_rate = 0.0 # Freeze style meter decay
        global_shop_markup = ZEN_IMPATIENCE_MARKUP
        open_shop_menu_instantly()
    else:
        # Standard Combat Taunt
        trigger_animation("Middle_Finger_To_Anomaly")
        style_points += 150 # Gives active style burst
        enemy_aggro_radius *= 1.5 # Enemies become faster and hit harder
```

## 👾 6. TARGET ENEMY & BOSS ROSTER
1.  **The Liquidator (Swarmer):** Extreme vulnerability to Slag + Fire combos. Runs at the player in groups of 8.
2.  **The Compliance Officer (Bruiser):** Immune to frontal hitscan. Shield must be flash-frozen with Cryo or out-flanked via a Shotgun-boosted Slide.
3.  **The Foreclosure Drone (Aerial Sniper):** Suspended by cyber-sigils. Must be yanked down using the Grapple Hook (`Circle`) or picked off with the Anti-Material Rifle (`L2 + R2`).
4.  **The Actuary (Disruptor Mage):** Levitating bookkeepers. Casts hexes that freeze your Style Meter. Barrier drops instantly when hit by Ionized Volt.
5.  **The Debt Collector (Elite Stalker):** Spawns when debt ledger rises too high. High agility assassins. Can only be damaged during recovery frames via a timed Bayonet Parry (`Triangle`).
6.  **The Auditor (Mechanical Minotaur):** Charges blindly, destroying walls and spiking your debt. Tricking it into hitting columns exposes a weak point on its back.
7.  **BOSS: The Liquidity Pool (The Final Anomaly):** A massive entity made of sentient black ledger ink. It mimics Corey's entire movement suite (slides, grapples, weapon swaps). Corey must push her rank into *The Reaper Margin* to pierce its defense.

## 🔓 PUBLIC DOMAIN USE TERMS
This project is dedicated to the public domain under CC0. Take this documentation and use it for standalone indie games, total conversion mods (GZDoom/Ultrakill), or commercial projects. No strings attached. Let's get this built.


# **CHIMÆRA OVERCLOCK**
**PROOF OF CONCEPT • PUBLIC DOMAIN SANDBOX**

---

## 🎮 CORE MECHANICS

### The Kinetic Camera Blueprint

No manual camera control—this game moves *with* you. The camera decouples from your shoulder and uses a dynamic wide-angle system that breathes with your momentum:

- **Standard State**: 4.5m arm length, 85° FOV. Clean sightlines for normal combat.
- **Momentum State** (slides, grapples): Pulls back to 6.5m at 105° FOV. You get that widescreen rush.
- **Vertical State** (climbing with bayonet): Camera lags behind and tilts down 25° to keep the ground visible—no disorienting verticality.

---

### Real-Time Execution Scaling (Personality & Frame Data)

Corey's entire presence—how she moves, how fast she recovers, how she sounds—shifts based on your operational efficiency:

- **D–B Tiers [Liquidity Crisis]**: Corey is pissed. Aggressive, vulgar, frustrated. Weapons feel heavy and move slow. High recovery frames. You're barely keeping your head above water.
- **A–S Tiers [Compliant Operation]**: Professional and balanced. Military discipline. Standard timing, mid-range speed. You're running clean operations.
- **SS–SSS Tiers [The Black Margin]**: Corey goes silent. The ex-military Reaper persona takes over. Animations strip down to pure efficiency. Recovery windows shrink hard.
- **Ultimate State [Reaper Mode Overclock]**: Amber night-vision overlay. Sub-bass audio pulses. Zero-frame weapon transforms. Corey is ice cold and lethal.

---

## 🔄 THE CHIMAERA FRAME & ELEMENTAL ARSENAL

You've got one weapon: the **Chimaera Frame**. It's a modular, transforming gun that reconfigures mid-combo without animation overhead. Swap forms, cycle elemental payloads—all mid-fight.

### Controls

- **R2 / RT**: Fire. Whatever form you're in (Pistols, Shotgun, Rifle, or Overclock AR).
- **L2 / LT (Tap)**: Swap between Dual Pistols and Shotgun.
- **L2 / LT (Hold ≥0.35s)**: Extend into Anti-Material Sniper Form.
- **Triangle / Y (Tap)**: Quick Bayonet Parry.
- **Triangle / Y (Hold)**: Rear Rocket Booster Impact Smash.
- **Triangle / Y (Mid-Air)**: Engage Hover Boots.
- **Square / X**: Grenade Bumper. Launch cooldown-based elemental canisters.
- **Circle / B (Ground)**: High-Velocity Slide.
- **Circle / B (Air / Lock-On)**: Grapple Zip Cable.
- **Right Stick**: Element Cycle. Rotate through Slag, Pyro, Cryo, and Volt payloads.
- **L3 + R3**: Reaper Mode Overclock. Activate when your gauge hits 100%.

### Elemental Hazmat Interactions

The real magic is in mixing your payload types:

- **Slag Fluid**: Creates oil slicks. Your slide velocity doubles crossing them.
- **Pyro Fluid**: Ignite Slag pools into thermal traps that pin enemies in place.
- **Cryo Coolant**: Flash-freezes targets. Freeze an airborne enemy and they become a physics anchor—grapple off them to slingshot across gaps.
- **Ionized Volt**: Strips corporate shields. Electrify Slag pools and hover above them safely with Hover Boots.

---

## 👥 THE CAST

**Cordelia "Corey" Cross** (The Reaper) is the main character you play—a stubborn frame-canceling specialist who can't die, only negotiate. Others are implemented as proof of concept:

- **Debt Collector**: Elite stalker. Mute, distorted mirror of Corey. Uses an Odachi, dual daggers, and a coiled whip-blade. High-stagger tracking counters. Hunts other enemies in the arena first, then challenges Corey to a 1-on-1 duel. His AI intelligence scales with your margins.
- **Sage**: Heavy hydraulic archetype. Hyper-armor charge stances. Perfect parry loops that let him cancel and reroute. Tanky and methodical.
- **Glitch**: Timeline trickster. Drops rewind hologram anchors that snap you back to previous coordinates and health values. Zero-frame repositioning.
- **Zen**: Mirror-cloner and alchemist. Runs the van shop. Can freeze your margin decay during a shopping session for a temporary corporate markup cost.

---

## 📊 THE MARGINS SYSTEM

Your operational efficiency is constantly tracked and decaying. This isn't a style rank—it's a real-time corporate ledger that determines how dangerous you are:

| Rank | Points | Decay Rate | Gauge Multiplier | Persona |
|------|--------|-----------|------------------|---------|
| **SSS** | 5000+ | 60.0/s | 6.0x | The Black Margin (Silent) |
| **SS** | 3500 | 45.0/s | 4.5x | The Black Margin (Silent) |
| **S** | 2000 | 30.0/s | 3.0x | Compliant (Professional) |
| **A** | 1000 | 20.0/s | 2.0x | Compliant (Professional) |
| **B** | 500 | 15.0/s | 1.5x | Liquidity Crisis (Vulgar) |
| **C** | 150 | 10.0/s | 1.0x | Liquidity Crisis (Vulgar) |
| **D** | 0 | 5.0/s | 0.5x | Liquidity Crisis (Vulgar) |

Higher margins = faster damage, quicker movement, more Gauge generation. Lower margins = you're struggling, and it *sounds* and *feels* different.

---

### The Buzzer Beater

When your Reaper Gauge empties, you get a **1.5-second grace window**. Land an attack during it and your points freeze. Miss it? Your decay rate jumps to 5x normal. High-risk, high-reward clutch mechanic.

---

## 💀 DEATH IS NEGOTIATION

You can't actually die. When you take fatal damage, the game stops and presents you with two choices:

1. **Reload** your last save.
2. **Continue** and accept a penalty marker.

Here's the catch: that penalty marker tanks your **end-of-level debt relief**. You still get paid for enemies, but less cash means lower debt payoff. That leftover debt carries into the next zone, increasing the Debt Collector's spawn chance. The difficulty ramps because of economics, not because your damage dropped. You're mechanically the same—just deeper in the hole.

---

## 💰 THE ECONOMY

Cash and debt are tracked separately:

- **Cash-In-Hand**: Dropped by enemies. Spent at vending machines for stimpaks and armor. Never drained by performance penalties.
- **Global Lifetime Debt**: Structural damage (breaking walls/glass) and interest pile up during a level. Compiled at the End-of-Level Financial Audit and added to your lifetime total. High debt = Debt Collector hunts you more aggressively in future zones.

This means poor execution doesn't cripple your immediate damage output, but it *does* haunt your economy. You have to manage both your margins *and* your ledger.

---

### Debt Collector Hunt Dynamics

The Debt Collector spawns randomly. Spawn chance scales with your global debt. When he shows up:

- He hunts other enemies in the arena first.
- He's looking for a 1-on-1 duel with Corey.
- He can't be killed, but chasing him off rewards a large cash payout.
- His AI difficulty scales with your current margins.
- Enemies he kills don't pay you—only enemies *you* kill count toward your cash.

---

## 🔓 PUBLIC DOMAIN (CC0)

This entire project—documentation, systems, math, character configs, everything—is **completely public domain** under Creative Commons Zero. No strings. No attribution required. Take it, mod it, commercialize it, remix it. Make it yours.

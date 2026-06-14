# =============================================================================
# CHIMAERA OVERCLOCK: MASTER GAME ENTRY POINT & FINANCIAL SYSTEM
# =============================================================================

import random
from EngineController import EngineController, GameState
from Intent import (
    CoreyElementSystem, CoreyIntentMap,
    DebtCollectorAIScale, DebtCollectorIntentMap, DebtCollectorBrainLoop
)

class FinancialDatabase:
    """Tracks Cordelia's wallet, property damage penalties, and stalker risk."""
    def __init__(self):
        self.total_cash = 0
        self.outstanding_debt = 50000  # Starting debt bracket
        self.property_damage_fees = 0

    def award_bounty(self, amount, margin_rank):
        """Spikes cash rewards based on performance rank."""
        rank_multipliers = {"D": 1.0, "C": 1.1, "B": 1.2, "A": 1.5, "S": 2.0, "SS": 2.5, "SSS": 3.0}
        multiplier = rank_multipliers.get(margin_rank, 1.0)
        
        earned = int(amount * multiplier)
        self.total_cash += earned
        print(f"Bounty Secured! Earned: ${earned} (Rank {margin_rank} Multiplier)")

    def log_property_damage(self, amount, is_overclocked):
        """Charges fees for structural destruction unless Overclock wave is active."""
        if is_overclocked:
            # Overclock Rule: Narrative/Arcade waiver is active; fees are zeroed out
            return
        self.property_damage_fees += amount

    def calculate_level_payout(self):
        """Deducts corporate property fees from total earnings at room exit."""
        net_payout = self.total_cash - self.property_damage_fees
        print("\n--- LEVEL PERFORMANCE FINANCIAL BREAKDOWN ---")
        print(f"Gross Bounties:  ${self.total_cash}")
        print(f"Property Damage: -${self.property_damage_fees}")
        print(f"Net Room Profit: ${max(0, net_payout)}")
        
        # Reset level tracking counters
        self.property_damage_fees = 0


class GameInstance:
    """Manages the level instantiation, active roster choice, and boss encounters."""
    def __init__(self):
        self.finances = FinancialDatabase()
        self.ai_director = DebtCollectorAIScale()
        
        # Initialize Reaper (Cordelia Cross) as the baseline player setup
        self.player_elements = CoreyElementSystem()
        self.player_intent = CoreyIntentMap(self.player_elements)
        
        # Hook everything into the universal master loop brain
        self.engine = EngineController(self.player_intent, self.player_elements, self.player_physics)

    def initialize_combat_room(self, anomaly_count):
        """Bootstraps a fresh arena and runs the random stalker boss check."""
        print(f"\nEntering Sector. Outstanding Corporate Debt: ${self.finances.outstanding_debt}")
        
        # 1. Roll the dice using her outstanding debt metric
        spawn_threshold = self.ai_director.calculate_spawn_probability(self.finances.outstanding_debt)
        roll = random.random()
        
        # 2. Check if the Debt Collector intercepts the transmission
        if roll <= spawn_threshold:
            print("WARNING: CHIMAERA FREQUENCY INTERCEPTED. THE DEBT COLLECTOR HAS ENTERED THE ARENA.")
            
            # Snap active margin score snapshot to scale his AI difficulty brain tier
            current_rank_snapshot = self.engine.state.margin_rank
            boss_tier = self.ai_director.determine_ai_tier(current_rank_snapshot)
            
            boss_intent = DebtCollectorIntentMap(boss_tier)
            boss_brain = DebtCollectorBrainLoop()
            
            # The room turns into an active, high-stakes bounty race!
            return True, boss_intent, boss_brain
            
        print("Transmission secure. Standard anomaly cleaning sequence active.")
        return False, None, None


# =============================================================================
# ARCADE SIMULATION RUNNER
# =============================================================================
if __name__ == "__main__":
    # Turn the key and initialize the game instance
    game = GameInstance()
    
    # Simulate a high-debt scenario where she enters a room filled with anomalies
    game.finances.outstanding_debt = 85000 
    boss_active, boss, brain = game.initialize_combat_room(anomaly_count=15)

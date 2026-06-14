import pygame
import sys
from EngineController import EngineController
from Intent import IntentProcessor
from StateData import PlayerState

def main():
    # Initialize the Pygame display and core systems
    pygame.init()
    
    # Setup your screen size (Zoomed-out character action proportions)
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_set_mode((screen_width, screen_height))
    pygame.display.set_caption("CHIMAERA OVERCLOCK")
    
    # Initialize your proprietary modular handlers
    intent_processor = IntentProcessor()
    controller = EngineController()
    
    # Setup your actors based on your studio's single-player strategy
    controller.player1 = PlayerState("Corey")
    controller.player2 = None  # Debt Collector starts unspawned
    
    # Frame management variables
    clock = pygame.time.Clock()
    running = True

    # ==========================================
    # 🔄 THE MAIN GAMEPLAY LOOP STARTS HERE
    # ==========================================
    while running:
        # 1. HARDWARE INPUTS LAYER
        # Check if the player closes the window or triggers buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Intercept raw movement, inputs, and metric logging
        controller.handle_events()

        # 2. MECHANICS & PHYSICS UPDATES LAYER
        # Corey's custom movement and physics states update every tick
        controller.player1.physics.update()
        
        # The Debt Collector's physics only update if he is dynamically spawned in
        if controller.player2 is not None:
            controller.player2.physics.update()

        # 3. GRAPHICS & RENDERING LAYER
        # Clear the window back to a solid black background canvas
        screen.fill((0, 0, 0))
        
        # Visual representations for testing tracking positions
        # Corey is drawn as a Red unit
        pygame.draw.circle(
            screen, 
            (255, 0, 0), 
            (int(controller.player1.physics.x), int(controller.player1.physics.y)), 
            25
        )
        
        # The Debt Collector is drawn as a Blue unit if he spawned
        if controller.player2 is not None:
            pygame.draw.circle(
                screen, 
                (0, 0, 255), 
                (int(controller.player2.physics.y), int(controller.player2.physics.y)), 
                25
            )

        # Flip the graphic memory buffer to render the new frames onto the screen
        pygame.display.flip()
        
        # Enforce frame rate limits to keep metric tracking mathematically perfect
        clock.tick(60)

    # ==========================================
    # 🛑 THE MAIN GAMEPLAY LOOP ENDS HERE
    # ==========================================
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
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
        
        # Initialize the universal low-poly physics brain from Intent.py
        from Intent import LowPolyPhysicsComponent
        self.player_physics = LowPolyPhysicsComponent()
        
        # Initialize Reaper (Cordelia Cross) as the baseline player setup
        self.player_elements = CoreyElementSystem()
        self.player_intent = CoreyIntentMap(self.player_elements)
        
        # Hook everything into the universal master loop brain (Physics is now active!)
        self.engine = EngineController(self.player_intent, self.player_elements, self.player_physics)
)

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

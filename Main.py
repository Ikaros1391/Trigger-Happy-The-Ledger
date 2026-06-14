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

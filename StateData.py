import time
from Physics import PhysicsObject

class Element:
    SLAG = "Slag"
    PYRO = "Pyro"
    CRYO = "Cryo"
    VOLT = "Volt"

class PlayerState:
    def __init__(self, character_name):
        self.character_name = character_name
        self.margin_points = 0
        self.margin_rank = "E"
        self.combo_history = []
        self.active_status = None
        self.status_duration = 0.0
        
        # Unique mechanics configurations for your 5 distinct showcase profiles
        self.canisters = {"Slag": 0, "Pyro": 0, "Cryo": 0, "Volt": 0}
        self.cooldowns = {}
        
        # Van Shopkeeper state overrides specifically for Zen
        self.is_shopkeeper_active = (character_name == "Zen")
        self.shop_inventory = ["Upgrade Component A", "Hardware Metric Booster"] if character_name == "Zen" else []

        # All characters seamlessly pull from the exact same physics rule engine!
        # Corey starts on the left side of the screen; bosses/NPCs spawn on the right
        spawn_x = 100 if character_name == "Corey" else 900
        self.physics = PhysicsObject(x=spawn_x, y=0)
        
        self.metadata = {
            "frame_config": [0] * 60,
            "input_buffer": []
        }

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
        
        # 🧾 Hypercapitalist Redgrave Corporation Debt
        self.debt_total = 1000000.0  
        self.cash_in_hand = 0.0
        
        # 🛡️ Defensive Attrition Layer (Low health, breakable plates)
        self.max_health = 50
        self.current_health = 50
        self.armor_plates = 3        
        
        # ⚡ Advanced Overclock Engine ("Reaper Mode")
        self.overclock_meter = 0.0    
        self.is_reaper_mode = False
        self.reaper_timer = 0.0
        self.active_element_infusion = None
        
        # 📊 Core Margin / Style Metrics (Rank D to SSS)
        self.margin_points = 0.0
        self.margin_rank = "D"
        self.margin_decay_timer = 0.0
        self.stagnation_penalty_multiplier = 1.0  
        self.combo_history = []                    
        
        # 🔫 Modular Weapon Frame / Canister Settings
        self.chimaera_weapon_form = "Pistol"  
        self.canisters = {"Slag": 3, "Pyro": 3, "Cryo": 3, "Volt": 3}
        self.cooldowns = {}
        
        # Physics Engine Connection
        spawn_x = 100 if character_name == "Corey" else 900
        self.physics = PhysicsObject(x=spawn_x, y=0)
        
        self.metadata = {
            "frame_config": [0] * 60,
            "input_buffer": []
    }
    

import time

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
        self.canisters = {"Slag": 0, "Pyro": 0, "Cryo": 0, "Volt": 0}
        self.cooldowns = {}
        self.metadata = {
            "frame_config": [0] * 60,
            "input_buffer": []
        }

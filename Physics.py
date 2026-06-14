class PhysicsObject:
    def __init__(self, x=0, y=0, mass=1.0):
        # Position and motion properties
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0
        self.mass = mass
        
        # Configuration constants
        self.gravity = 0.5
        self.friction = 0.85
        self.ground_level = 500  # Adjust based on your Pygame window height
        self.is_grounded = False

    def apply_force(self, fx, fy):
        """Applies a sudden impulse force (like an explosion or a hit)."""
        self.vx += fx / self.mass
        self.vy += fy / self.mass

    def update(self):
        """Calculates frame-by-frame movement math."""
        # Apply standard gravity if in mid-air
        if not self.is_grounded:
            self.vy += self.gravity

        # Apply friction to horizontal movement
        self.vx *= self.friction

        # Move the object positions
        self.x += self.vx
        self.y += self.vy

        # Simple screen boundary checks (Ground locking)
        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.vy = 0.0
            self.is_grounded = True
        else:
            self.is_grounded = False

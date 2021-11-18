import arcade

class Enemies(arcade.Sprite):
    """the enemies template"""

    def __init__(self, image, scale):
        super().__init__(image,scale)

        self.life = None
        self.speed = None
        
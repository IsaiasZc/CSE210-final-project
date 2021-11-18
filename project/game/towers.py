import arcade

class Towers(arcade.Sprite):
    """Towers template"""

    def __init__(self,img, scale):
        super().__init__(image, scale)

        main_path = ''
        self.HP = ""
        self.MP = ""
        self.attack_range = ""

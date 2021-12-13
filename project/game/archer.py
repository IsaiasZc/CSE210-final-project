from game.towers import Towers
from game import constants

class Archer(Towers):

    def __init__(self):
        self._image = "game/images/archer.png"
        self._scale = 0.3
        super().__init__(self._image, self._scale)

        self.fire_rate = 1.0
        # Create the bullet
        self.set_bullet_image("game/images/arrow1.png")
        self.bullet_speed = 5

        self.center_x, self.center_y = [constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 200]

        self.attack_range = 150

        self.damage = 20

        self.max_attacked = 1
        self.price = 20
        self.name = "archer"
        self.upgrade_price = 20
    
    def set_upgrade(self):
        upgrade_list = [self.bullet_speed,self.damage,self.price,self.upgrade_price]
        self.upgrade(upgrade_list,self.fire_rate)

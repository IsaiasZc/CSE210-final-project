import arcade
from game.towers import Towers
from game import constants

class Wizard(Towers):

    def __init__(self):
        self._image = "game/images/wizard.png"
        self._scale = 0.3
        super().__init__(self._image,self._scale)

        self.fire_rate = 0.8
        # Create the bullet
        self.set_bullet_image(":resources:images/space_shooter/laserBlue01.png")
        self.bullet_speed = 3
        self.center_x, self.center_y = [constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2]

        self.attack_range = 100
        self.damage = 20

        self.max_attacked = 1
        self.price = 10
        self.name = "wizard"
        self.upgrade_price = 15

        # self.bullet_sound = arcade.load_sound("game/sounds/wizard_attack.mp3")
        self.hit_sound = arcade.load_sound("game/sounds/wizard_hit.mp3")

    def set_upgrade(self):
        upgrade_list = [self.bullet_speed,self.damage,self.price,self.upgrade_price]
        self.upgrade(upgrade_list,self.fire_rate)
import arcade
from game.towers import Towers
from game import constants

class Assassin(Towers):

    def __init__(self):
        self._image = "game/images/assassin.png"
        self._scale = 0.4
        super().__init__(self._image, self._scale)

        self.fire_rate = 0.4
        # Create the bullet
        self.set_bullet_image("game/images/knife1.png")
        self.bullet_speed = 7

        self.center_x, self.center_y = [constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 200]

        self.attack_range = 60

        self.damage = 11

        self.max_attacked = 1
        self.price = 12
        self.name = "assassin"
        self.upgrade_price = 30
        
        # self.bullet_sound = arcade.load_sound("game/sounds/assassin_attack.mp3")
        self.hit_sound = arcade.load_sound("game/sounds/assassin_hit.mp3")
    
    
    def set_upgrade(self):
        upgrade_list = [self.bullet_speed,self.damage,self.price,self.upgrade_price]
        self.upgrade(upgrade_list,self.fire_rate)

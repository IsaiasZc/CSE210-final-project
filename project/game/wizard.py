from game.towers import Towers
from game import constants

class Wizard(Towers):

    def __init__(self):
        self._image = ":resources:images/animated_characters/robot/robot_walk0.png"
        self._scale = 0.5
        super().__init__(self._image,self._scale)

        self.fire_rate = 1
        # Create the bullet
        self.set_bullet_image(":resources:images/space_shooter/laserBlue01.png")
        self.bullet_speed = 3

        self.center_x, self.center_y = [constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2]

        self.attack_range = 100

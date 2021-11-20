import arcade
from arcade import sprite

from game import constants

class Enemies(arcade.Sprite):
    """the enemies template"""

    def __init__(self, image, scale):
        super().__init__(image,scale)

        self.life = None
        self.speed = None

        self.change_x = 0
        self.change_y = -1

    def move(self):
        """Move the sprite in the path direction"""

        position = [self.center_x, self.center_y]

        for i, path in enumerate(constants.SCREEN_PATH):
            last_possition = 13

            if position == constants.SCREEN_PATH[last_possition]:
                self.kill()
                break

            if position == path:
                next_x, next_y = constants.SCREEN_PATH[i + 1]
                if next_x > self.center_x:             
                    self.change_x = self.speed
                    self.change_y = 0
                elif next_x < self.center_x:
                    self.change_x = -self.speed
                    self.change_y = 0
                elif next_y > self.center_y:
                    self.change_x = 0
                    self.change_y = self.speed
                elif next_y < self.center_y:
                    self.change_x = 0
                    self.change_y = -self.speed
                break
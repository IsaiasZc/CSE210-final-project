from game.enemies import Enemies
from game import constants

class Zombie(Enemies):

    def __init__(self):

        self._image = ":resources:images/animated_characters/zombie/zombie_walk6.png"
        self._scale = 0.5
        super().__init__(self._image,self._scale)


        self.center_x, self.center_y = constants.SCREEN_PATH[0]

        self.speed = 1

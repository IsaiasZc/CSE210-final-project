from game.towers import Towers
from game import constants

class Archer(Towers):

    def __init__(self):
        self._image = ""
        self._scale = None
        super().__init__(self._image, self._scale)



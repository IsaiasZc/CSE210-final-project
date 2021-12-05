import arcade
import math
from game.towers import Towers 
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard
from game.side_menu import SideMenu
from game.waves import Waves
from game.fading_view import FadingView

class KeepScore(self):
    """Class to keep the score"""
    self.gui_camera = None
    self.score = 0

    self.gui_camera = arcade.Camera(self.width, self.height)

    def on_draw(self):
        """Remder the screen"""
  
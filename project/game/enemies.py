import arcade
from arcade import sprite

from game import constants

class Enemies(arcade.Sprite):
    """the enemies template"""

    def __init__(self, image, scale):
        super().__init__(image,scale)

        self.life = None
        self._speed = None

        # Know when is been attacked
        self.focus = False

        self.change_x = 0
        self.change_y = -1

        # self.life = None
        self.max_health = self.life

        # The enemy name
        self.name = ""
        self.kill_coins = None
        
    def draw_health_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self.max_health}/ {self.life}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + constants.HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + constants.HEALTH_NUMBER_OFFSET_Y,
                         font_size=8,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.life < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + constants.HEALTHBAR_OFFSET_Y,
                                         width=constants.HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        # Calculate width based on health
        health_width = constants.HEALTHBAR_WIDTH * (self.life / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (constants.HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=constants.HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)

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
        
    def updatelife(self,life):
        self.life = life
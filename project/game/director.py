import arcade
import time
from game import constants
from game.zombie import Zombie
from game.towers import SpaceCraft


class Director(arcade.Window):
    """The director of the game"""
    # MenuView()
    # InstructionView()
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        

        # # These are 'lists' that keep track of our sprites. Each sprite should
        # # go into a list.
        # self.wall_list = None
        # self.player_list = None

        # # Separate variable that holds the player sprite
        # self.player_sprite = None

        self.bol = None
        self.enemy = Zombie()

        self.background = None # arcade.texture("project/game/images/map_one.png")
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.enemy_list = []
        self.player = SpaceCraft()
        self.start_time = time.time()

    def setup(self):

        self.bol = Zombie()

        # Load texture
        self.background =arcade.load_texture("project/game/images/map_one.png")

    def on_draw(self):
        arcade.start_render()

        # Draw the bcakground texture
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background)

        for bullet in self.player.bullet_list:
            bullet.draw()

        self.player.draw()
        
        for enemy in self.enemy_list:
            enemy.draw()
        

        self.bol.draw()

        # Draw a grid s
        w = constants.SCREEN_WIDTH - 1
        h = constants.SCREEN_HEIGHT - 1
        n = 1
        # for x in range(20, w, 20):
        #      arcade.draw_line(x, 0, x, h, arcade.color.RED)

        # for y in range(20, h,20):
        #     arcade.draw_line(0, y, w, y,arcade.color.RED)

    def on_update(self, delta_time):

        self.bol.update()
        self.bol.move()

        self.player.rotate()

        self.end_time = time.time()
        # if self.end_time - self.start_time > 5:
        #     self.enemy_list.append(self.enemy())
        #     self.start_time = time.time()

        for enemy in self.enemy_list:
            enemy.move()
        
        for bullet in self.player.bullet_list:
            bullet.move()

        for bullet in self.player.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet, enemy):
                    self.enemy_list.remove(enemy)
                    self.player.bullet_list.remove(bullet)

    def on_key_press(self, key, modifiers):
        # Rotate left/right
        if key == arcade.key.LEFT:
            self.player.change_angle = 1
        elif key == arcade.key.RIGHT:
            self.player.change_angle = -1
        elif key == arcade.key.SPACE:
            self.player.fire()        

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_angle = 0
import arcade
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard
from game.side_menu import SideMenu
from game.enemies import Enemies

class Director(arcade.View):
    """The director of the game"""

    def __init__(self):

        # Call the parent class and set up the window
        # super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        # Code to change to view instead of window
        super().__init__()

        self.n = 1

        self.bol = None
        self.wizard = None
        self.wizard_list = []
        self.enemy_list = []
        self.background = None # arcade.texture("project/game/images/map_one.png")
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # * the first attempt to insert the side menu Class
        self.side_menu = SideMenu()

    def setup(self):

        
        # self.bol = Zombie()
        self.enemy_list = arcade.SpriteList()
        # self.enemy_list.append(self.bol)
        self.wizard = Wizard()
        self.wizard_list = arcade.SpriteList()
        self.wizard_list.append(self.wizard)

        self.max_enemies = 20
        self.enemies_in_map = 0

        # Load texture
        self.background =arcade.load_texture("project/game/images/map_one.png")

        arcade.schedule(self.add_enemy,1)

        # Create the Side Menu
        self.side_menu.reset_panel()
        self.side_menu.set_menu_options([Wizard()])
     

    def on_draw(self):
        arcade.start_render()

        # Draw the bcakground texture
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background)

        # Draw the sideMenu
        self.side_menu.draw_panel()
        self.side_menu.draw_held_towers()

        self.enemy_list.draw()
        for wizard in self.wizard_list:
            wizard.draw_bullet()
        # self.wizard.draw_bullet()
        self.wizard_list.draw()
        # Draw a grid s
        w = constants.SCREEN_WIDTH - 1
        h = constants.SCREEN_HEIGHT - 1
        n = 1

    def on_update(self, delta_time):

        if self.enemies_in_map > self.max_enemies:
            arcade.unschedule(self.add_enemy)
        
        self.enemy_list.update()
        for enemy in self.enemy_list:
            enemy.move()

        self.wizard_list.update()
        for wizard in self.wizard_list:
            wizard.on_update(delta_time,self.enemy_list)
            wizard.update_bullet(self.enemy_list)
            self.enemy_list.pop()

        # self.enemy_list.update()
        # for enemy in self.enemy_list:
        #     if Zombie.center_x > constants.SCREEN_WIDTH and Zombie.center_y > constants.SCREEN_HEIGHT:
        #         view = GameOverView()
        #         self.window.show_view(view)

        if self.enemy_list is None:
            view = GameOverView()
            self.window.show_view(view) 


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.side_menu.on_mouse_press(x,y)


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_release(self.wizard_list,x,y)

    
    def on_mouse_motion(self,x : float, y: float, dx: float, dy: float):

        self.side_menu.on_mouse_motion(dx, dy)
    
    def add_enemy(self, delta_time: float):
        self.enemies_in_map += 1
        self.enemy_list.append(Zombie())
        

class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        # arcade.set_viewport(0, self.window.width, 0, self.window.height)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("project/game/images/game_over_1.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)
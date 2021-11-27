import arcade
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard
from game.side_menu import SideMenu

class Director(arcade.Window):
    """The director of the game"""

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)


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



        self.wizard_list.update()
        for wizard in self.wizard_list:
            wizard.on_update(delta_time,self.enemy_list)
            wizard.update_bullet(self.enemy_list)
        
        self.enemy_list.update()
        for enemy in self.enemy_list:
            enemy.move()




    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.side_menu.on_mouse_press(x,y)


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_release(self.wizard_list,x,y)

    
    def on_mouse_motion(self,x : float, y: float, dx: float, dy: float):

        self.side_menu.on_mouse_motion(dx, dy)
    
    def add_enemy(self, delta_time: float):
        self.enemies_in_map += 1
        self.enemy_list.append(Zombie())
        
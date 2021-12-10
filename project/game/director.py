import arcade
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard
from game.side_menu import SideMenu
from game.waves import Waves
from game.fading_view import FadingView

class Director(FadingView):
    """The director of the game"""

    def __init__(self):

        # Call the parent class and set up the window
        # super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        # Code to change to view instead of window
        super().__init__()

        self.n = 1

        #* self.bol = None
        self.wizard = None
        self.wizard_list = []
        self.waves = Waves()
        #* self.enemy_list = []
        self.background = None # arcade.texture("project/game/images/map_one.png")
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


        # the first attempt to insert the side menu Class
        self.side_menu = SideMenu()
        self.background_sound = arcade.load_sound("project/game/sounds/Darkling_back_sound.mp3")
        self.wizard_sound = arcade.load_sound("project/game/sounds/wizard_attack.mp3")
        self.hit_sound = arcade.load_sound("project/game/sounds/hit.mp3")
        self.click_sound = arcade.load_sound("project/game/sounds/click_1.mp3")

    def setup(self):

        self.waves.reset()
        #* self.bol = Zombie()
        #* self.enemy_list = arcade.SpriteList()
        # self.enemy_list.append(self.bol)
        self.wizard = Wizard()
        self.wizard_list = arcade.SpriteList()
        self.wizard_list.append(self.wizard)

        #* self.max_enemies = 20
        #* self.enemies_in_map = 0

        # Load texture
        self.background =arcade.load_texture("project/game/images/map_one.png")

        #* arcade.schedule(self.add_enemy,1)

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

        #* self.enemy_list.draw()
        self.waves.enemies_in_wave.draw()
        for wizard in self.wizard_list:
            wizard.draw_bullet()
            
        for enemy in self.waves.enemies_in_wave:
            enemy.draw_health_number()
            enemy.draw_health_bar()
                       
        # self.wizard.draw_bullet()
        self.wizard_list.draw()
        # Draw a grid s
        w = constants.SCREEN_WIDTH - 1
        h = constants.SCREEN_HEIGHT - 1
        n = 1

    def on_update(self, delta_time):
        
        self.waves.update_wave(delta_time)
        if self.waves.end_wave():
            self.waves.add_new_wave()

        self.wizard_list.update()
        for wizard in self.wizard_list:
            #* wizard.on_update(delta_time,self.enemy_list)
            wizard.on_update(delta_time,self.waves.enemies_in_wave)
            #* wizard.update_bullet(self.enemy_list)
            wizard.update_bullet(self.waves)


        if self.waves.wave_life is None:
            view = GameOverView()
            self.window.show_view(view) 


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_press(x,y,self.waves.coins)
        arcade.play_sound(self.click_sound)
            


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_release(self.wizard_list,x,y,self.waves)

    
    def on_mouse_motion(self,x : float, y: float, dx: float, dy: float):

        self.side_menu.on_mouse_motion(dx, dy)
    
    def add_enemy(self, delta_time: float):
        self.enemies_in_map += 1
        self.enemy_list.append(Zombie())
        
# Different views
class MenuView(FadingView):
    """ Class that manages the 'menu' view. """

    def on_update(self, dt):
        self.update_fade(next_view=InstructionView)

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Menu Screen - press space to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if self.fade_out is None and key == arcade.key.SPACE:
            self.fade_out = 0

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

class InstructionView(FadingView):
    """ View to show instructions """

    def on_update(self, dt):
        self.update_fade(next_view=Director)

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Instructions Screen - press space to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.BLUE, font_size=30, anchor_x="center")
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if self.fade_out is None and key == arcade.key.SPACE:
            self.fade_out = 0

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

class GameOverView(FadingView):
    """ Class to manage the game over view """
    def on_update(self, dt):
        self.update_fade(next_view=MenuView)

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press SPACE to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, 30, anchor_x="center")
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.SPACE:
            self.fade_out = 0

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

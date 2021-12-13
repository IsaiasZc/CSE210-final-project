import arcade
import os
import sys
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard
from game.side_menu import SideMenu
from game.waves import Waves
from game.fading_view import FadingView
from game.archer import Archer
from game.assassin import Assassin

class Director(FadingView):
    """The director of the game"""

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        self.n = 1
        self.tower = None
        self.towers_list = []
        self.waves = Waves()
        self.background = None 
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Insert the side menu Class
        self.side_menu = SideMenu()
        self.background_sound = arcade.load_sound("project/game/sounds/Darkling_back_sound.mp3")
        self.tower_sound = arcade.load_sound("project/game/sounds/wizard_attack.mp3")
        self.hit_sound = arcade.load_sound("project/game/sounds/hit.mp3")
        self.click_sound = arcade.load_sound("project/game/sounds/click_1.mp3")

    def setup(self):

        self.waves.reset()
        self.towers_list = arcade.SpriteList()

        # Load texture
        self.background =arcade.load_texture("project/game/images/map_one.png")

        # Create the Side Menu
        self.side_menu.reset_panel()
        # Add the towers
        self.side_menu.set_menu_options([Wizard(),Archer(),Assassin()])


    def on_draw(self):
        arcade.start_render()

        # Draw the bcakground texture
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background)

        # Draw the sideMenu
        self.side_menu.draw_panel()
        self.side_menu.draw_held_towers(self.towers_list)

        #* self.enemy_list.draw()
        self.waves.enemies_in_wave.draw()
        for tower in self.towers_list:
            tower.draw_bullet()
            
        self.waves.draw_info()

        for enemy in self.waves.enemies_in_wave:
            #enemy.draw_health_number()

            enemy.draw_health_bar()
                       
        # self.tower.draw_bullet()
        self.towers_list.draw()
        # Draw a grid s
        w = constants.SCREEN_WIDTH - 1
        h = constants.SCREEN_HEIGHT - 1
        n = 1

    def on_update(self, delta_time):

        # if self.waves.wave_number == 5:
        #     self.side_menu.add_menu_option()
        
        self.waves.update_wave(delta_time)
        if self.waves.end_wave():
            self.waves.add_new_wave()

        self.towers_list.update()
        for tower in self.towers_list:
            #* tower.on_update(delta_time,self.enemy_list)
            tower.on_update(delta_time,self.waves.enemies_in_wave)
            #* tower.update_bullet(self.enemy_list)
            tower.update_bullet(self.waves)


        if self.waves.wave_life <= 0:
            view = GameOverView()
            self.window.show_view(view) 


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_press(x,y,self.waves.coins)
        arcade.play_sound(self.click_sound)
            


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        
        self.side_menu.on_mouse_release(self.towers_list,x,y,self.waves)

    
    def on_mouse_motion(self,x : float, y: float, dx: float, dy: float):

        self.side_menu.on_mouse_motion(dx, dy)
    
    def add_enemy(self, delta_time: float):
        self.enemies_in_map += 1
        self.enemy_list.append(Zombie())
        
# Different views
class MenuView(FadingView):
    """ Class that manages the 'menu' view. """
    def setup(self):
        """ Set up the game and initialize the variables. """
        # self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.player = None

    def on_update(self, dt):
        self.update_fade(next_view=InstructionView)
        

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)
        self.player = arcade.play_sound(self.background_sound)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()

        for i in range(len(self.backgrounds)):
                arcade.draw_texture_rectangle(self.bg_x[i], int(constants.SCREEN_HEIGHT / 2), constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.backgrounds[i])

        self.draw_timer += 1
        if self.draw_timer > self.bg_x_timer:
            for k in range(len(self.bg_x)):
                if self.bg_x[k] <= -800:
                    self.bg_x[k] = max(self.bg_x) + constants.SCREEN_WIDTH
                self.bg_x[k] -= 1

            # if max(self.bg_x) % 800 == 0:
            #     self.bg_switch = not self.bg_switch
            #     if not self.bg_switch:
            #         self.bg_x_timer = self.draw_timer + 200
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.main_menu_bg)

        arcade.draw_text("",
                        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 100,
                        arcade.color.BLACK, font_size=30, bold=True, anchor_x="center")
        arcade.draw_text("A Game where you will see", 
                        constants.SCREEN_WIDTH / 2 + 170, constants.SCREEN_HEIGHT / 2 + 50,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Clarendon blk bt"), anchor_x="center")
        arcade.draw_text("a mixture of characters", 
                        constants.SCREEN_WIDTH / 2 + 170, constants.SCREEN_HEIGHT / 2 - 50,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Clarendon blk bt"), anchor_x="center")
        arcade.draw_text("V 1.0.0",
                        constants.SCREEN_WIDTH / 2 + 170, constants.SCREEN_HEIGHT / 2 - 100,
                        arcade.color.WHITE, font_size=10, italic=True,font_name=("Clarendon blk bt"), anchor_x="center")
        arcade.draw_text(">>>>>>> Press SPACE to advance <<<<<<<", 
                        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 380,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Bauhaus 93"), anchor_x="center")

        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if self.fade_out is None and key == arcade.key.SPACE:
            self.fade_out = 0
            arcade.stop_sound(self.player)

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
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.instructions_bg)
        arcade.draw_text(">>>>>>> Press SPACE to advance <<<<<<<", 
                        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 380,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Bauhaus 93"), anchor_x="center")

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
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.game_over_bg)
        arcade.draw_text(">>>>>>> Press SPACE to restart <<<<<<<", 
                        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 360,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Bauhaus 93"), anchor_x="center")
        arcade.draw_text(">>>>>>> Press ESCAPE to exit the game <<<<<<<", 
                        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 390,
                        arcade.color.WHITE, font_size=25, italic=True,font_name=("Bauhaus 93"), anchor_x="center")

        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.SPACE:
            self.fade_out = 0
        elif key == arcade.key.ESCAPE:
            self.fade_out = 0
            os._exit(1)

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

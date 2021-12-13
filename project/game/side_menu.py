import arcade
from arcade.sprite_list.sprite_list import SpriteList
from game import constants
import copy
from game.wizard import Wizard
from game.archer import Archer
from game.assassin import Assassin

class SideMenu():

    def __init__(self):
        """Declare the side meru class to store the differents 
        menu options like, choose the characters
        """
        
        # TODO: There are two possible ways:
        # 1.- Store the Class Directly
        # 2.- Store an array [ Class, "name of tower"]
        self._menu_options = []

        # the tower clicked to drag it to the map
        self._held_towers =  []

        # The menu Sprite with its size, color, position
        self._menu_panel = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self._held_towers_original_position = []

        self.path_list= []

        # start the _menu_panel

    def reset_panel(self):
        """Create the new menu panel and return it to work with it."""
        self._menu_options = arcade.SpriteList()
        self._held_towers = arcade.SpriteList()
        self._menu_panel = arcade.SpriteList()
        self.path_list = arcade.SpriteList()
        self._held_towers_original_position = []
        panel = arcade.SpriteSolidColor(constants.SIDE_MENU_WIDTH,constants.SIDE_MENU_HEIGHT,arcade.csscolor.CHOCOLATE)
        panel.position = constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2
        self._menu_panel.append(panel)
        self.create_path()

        return self._menu_panel


    def draw_held_towers(self,towers_list):
        """This method will help us to draw the held tower by the player while is been dragging.
        
        Args.
            self : the SideMenu class.
        """
        if len(self._held_towers) > 0:
            self._held_towers[0].draw_radius(self.path_list,towers_list)
            self._held_towers[0].draw()

    def draw_panel(self):
        """draw the panel"""    
        self._menu_panel.draw()
        self._menu_options.draw()
        self.draw_price(self._menu_options)
        self.draw_tower_name(self._menu_options)
        # self.path_list.draw()
    
    def set_menu_options(self, options_list):

        for object in options_list:
            self._menu_options.append(object)
    
    def add_menu_option(self, option):
        self._menu_options.append(option)


    def on_mouse_press(self, x, y, coins):
        """Recognize when the player has press a tower to drag it
        
        Args.
            self: The SideMenu class.
            x : the x coordinate of the mouse.
            y . the y coordinate of the mouse.
        """
        towers = arcade.get_sprites_at_point((x,y), self._menu_options)

        # Here I want to know what tower has been clicked, and I have to create
        # duplicate to drag.
        if len(towers) > 0:
            if towers[0].price <= coins:
                #Create the new tower
                new_tower = self.create_tower(towers[0]) #? this could be another way copy.deepcopy(towers[0])

                self._held_towers = [new_tower]
                new_tower.selected = True

                # Save the original position
                self._held_towers_original_position = [self._held_towers[0].position]

    def on_mouse_motion(self, dx, dy):
        """Recognize when the user move the mouse and drag the tower
        if there is a tower in the held cards list.

        """
        for tower in self._held_towers:
            tower.center_x += dx
            tower.center_y += dy

    def on_mouse_release(self, towers_list, x, y,wave):
        """"""

        # For now, we don't have a collision detection to know
        # where the player can site the tower.

        if len(self._held_towers) == 0:
            return

        # recognize if the player is releasing the tower over the panel
        in_panel = arcade.check_for_collision_with_list(self._held_towers[0],self._menu_panel)
        in_path = arcade.check_for_collision_with_list(self._held_towers[0],self.path_list)
        other_towers = arcade.check_for_collision_with_list(self._held_towers[0],towers_list)

        # If the tower is relased in the panel, delete it
        if len(in_panel) > 0 or len(in_path) > 0 or len(other_towers) > 0:
            self._held_towers.clear()

        # For each held tower, set it in the map.
        for dropped_tower in self._held_towers:
            # Drop the card in the mouse position.
            dropped_tower.position = x, y
            dropped_tower.selected = False
            dropped_tower.in_panel = False
            wave.coins -= dropped_tower.price
            towers_list.append(dropped_tower)
        
        self._held_towers.clear()
    
    def create_tower(self,tower):
        """create a tower similar to the clicked"""

        if tower.name == "wizard":
            return Wizard()
        elif tower.name == "archer":
            return Archer()
        elif tower.name == "assassin":
            return Assassin()
    
    def create_path(self):
        for i,(cur_x, cur_y) in enumerate(constants.SCREEN_PATH):
            if i == 13:
                break
            next_x, next_y = constants.SCREEN_PATH[i + 1]
            if cur_x == next_x:
                width = 60
                height = abs(cur_y - next_y)
            elif cur_y == next_y:
                width = abs(cur_x - next_x)
                height = 60
            panel = arcade.SpriteSolidColor(width, height, arcade.csscolor.WHITE)
            # Vertical
            if cur_x == next_x:
                panel.position = next_x, next_y + ((cur_y - next_y) / 2)
            # Horizontal
            elif cur_y == next_y:
                panel.position = next_x + ((cur_x - next_x) / 2) , next_y - 10
            self.path_list.append(panel)

    def draw_price(self,tower_list):
        for tower in tower_list:    
            price_string = f"Cost: {tower.price}"
            arcade.draw_text(price_string,
                            start_x=tower.center_x - 30,
                            start_y=tower.center_y - 50,
                            font_size=10,
                            bold=True,
                            color=arcade.color.BLUE)
    
    def draw_tower_name(self,tower_list):
        for tower in tower_list:    
            name_string = f"{tower.name}"
            arcade.draw_text(name_string,
                            start_x=tower.center_x - 30,
                            start_y=tower.center_y + 40,
                            font_size=10,
                            bold=True,
                            color=arcade.color.BLUE)

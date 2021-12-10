import arcade
from arcade.sprite_list.sprite_list import SpriteList
from game import constants
import copy
from game.wizard import Wizard

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

        # start the _menu_panel

    def reset_panel(self):
        """Create the new menu panel and return it to work with it."""
        self._menu_options = arcade.SpriteList()
        self._held_towers = arcade.SpriteList()
        self._menu_panel = arcade.SpriteList()
        self._held_towers_original_position = []
        panel = arcade.SpriteSolidColor(constants.SIDE_MENU_WIDTH,constants.SIDE_MENU_HEIGHT,arcade.csscolor.CHOCOLATE)
        panel.position = constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_HEIGHT / 2
        self._menu_panel.append(panel)


        return self._menu_panel


    def draw_held_towers(self):
        """This method will help us to draw the held tower by the player while is been dragging.
        
        Args.
            self : the SideMenu class.
        """
        if len(self._held_towers) > 0:
            self._held_towers[0].draw_radius()
            self._held_towers[0].draw()

    def draw_panel(self):
        """draw the panel"""    
        self._menu_panel.draw()
    
    def set_menu_options(self, options_list):

        for object in options_list:
            self._menu_options.append(object)


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

        # If the tower is relased in the panel, delete it
        if len(in_panel) > 0:
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
        
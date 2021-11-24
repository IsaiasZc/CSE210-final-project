import arcade
from game import constants

class SideMeru():

    def __init__(self):
        """Declare the side meru class to store the differents 
        menu options like, choose the characters
        """
        
        # There are two possible ways:
        # 1.- Store the Class Directly
        # 2.- Store an array [ Class, "name of tower"]
        self._menu_options = []

        # the tower clicked to drag it to the map
        self._held_towers =  []

        # The menu Sprite with its size, color, position
        self.menu_panel = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self._held_towers_original_position = []

        # start the menu_panel

    def set_new_panel(self):
        """Create the new menu panel and return it to work with it."""
        panel = arcade.SpriteSolidColor(constants.SIDE_MENU_HEIGHT,constants.SIDE_MENU_WIDTH,arcade.csscolor.AQUA)
        panel.position = constants.SIDE_MENU_WIDTH / 2, constants.SCREEN_WIDTH / 2
        self.menu_panel.append(panel)

        return self.menu_panel
    
    def draw_held_towers(self):
        """This method will help us to draw the held tower by the player while is been dragging.
        
        Attr.
            self : the SideMenu class.
        """
        if len(self._held_towers) > 0:
            self._held_towers[0].draw_radius()
            self._held_towers[0].draw()

    def on_mouse_press(self, x, y):
        """Recognize when the player has press a tower to drag it
        
        Attr.
            self: The SideMenu class.
            x : the x coordinate of the mouse.
            y . the y coordinate of the mouse.
        """
        towers = arcade.get_sprites_at_point((x,y), self._menu_options)

        # Here I want to know what tower has been clicked, and I have to create
        # duplicate to drag.
        if len(towers) > 0:
            #Create the new tower
            new_tower = towers[0]

            self._held_towers = [new_tower]
            new_tower.selected = True

            # Save the original position
            self._held_towers_original_position = [self._held_towers[0].position]

    def on_mouse_motion(self, x, y):
        """Recognize when the user move the mouse and drag the tower
        if there is a tower in the held cards list.

        """

import arcade
from game import constants
from game.zombie import Zombie
from game.wizard import Wizard

class Director(arcade.Window):
    """The director of the game"""

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # # These are 'lists' that keep track of our sprites. Each sprite should
        # # go into a list.
        # self.wall_list = None
        # self.player_list = None

        # # Separate variable that holds the player sprite
        # self.player_sprite = None
        self.n = 1

        self.bol = None
        self.wizard = None
        self.wizard_list = []
        self.enemy_list = []
        self.background = None # arcade.texture("project/game/images/map_one.png")
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Side bar list
        self.cards_list = None

        # Cards we are dragging with the mouse 
        self.held_cards = None

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = None

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list = None 

        

    def setup(self):

        
        # self.bol = Zombie()
        self.enemy_list = arcade.SpriteList()
        # self.enemy_list.append(self.bol)
        self.wizard = Wizard()
        self.wizard_list = arcade.SpriteList()
        self.wizard_list.append(self.wizard)

        # Load texture
        self.background =arcade.load_texture("project/game/images/map_one.png")

        # for i in range(10):
        #     self.add_enemy(2,Zombie())
        
        # List of cards we are dragging with the mouse
        self.held_cards = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = []# List of cards we are dragging with the mouse

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        
        for i in range(7):
            pile = arcade.SpriteSolidColor(constants.MAT_WIDTH, constants.MAT_HEIGHT, arcade.csscolor.DARK_GRAY)
            pile.position = 0, constants.BOTTOM_Y + i * constants.Y_SPACING
            self.pile_mat_list.append(pile)
        
        


    def on_draw(self):
        arcade.start_render()

        # Draw the bcakground texture
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,self.background)

        # Draw the mat piles
        self.pile_mat_list.draw()

        self.enemy_list.draw()
        for wizard in self.wizard_list:
            wizard.draw_bullet()
        # self.wizard.draw_bullet()
        self.wizard_list.draw()
        # Draw a grid s
        w = constants.SCREEN_WIDTH - 1
        h = constants.SCREEN_HEIGHT - 1
        n = 1
        # for x in range(20, w, 20):
        #      arcade.draw_line(x, 0, x, h, arcade.color.RED)

        # for y in range(20, h,20):
        #     arcade.draw_line(0, y, w, y,arcade.color.RED)

    def on_update(self, delta_time):

        # self.bol.update()
        # self.bol.move()
        maxi = 240
        self.n += 1
        if self.n % 60 ==0 and self.n <= maxi:
            self.add_enemy(3,Zombie())
        
        self.enemy_list.update()
        for enemy in self.enemy_list:
            enemy.move()

        self.wizard_list.update()
        # self.wizard.tower_atack(self.bol)
        for wizard in self.wizard_list:
            wizard.update_bullet()
            for enemy in self.enemy_list:
                wizard.tower_atack(enemy)
        
        for player in self.wizard_list:
            for bullet in player.get_bullet_list():
                for enemy in self.enemy_list:
                    if arcade.check_for_collision(bullet,enemy):
                        self.enemy_list.remove(enemy)
                        player.get_bullet_list().remove(bullet)



    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        towers = arcade.get_sprites_at_point((x,y),self.wizard_list)

        if len(towers) > 0:
            tower = Wizard()

            self.held_cards = [tower]
            # Save the position
            self.held_cards_original_position = [self.held_cards[0].position]

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if len(self.held_cards) == 0:
            return
        # Find the closest pile, in case we are in contact with more than one
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        # See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):
            
            # For each held card, move it to the pile we dropped on
            for i, dropped_card in enumerate(self.held_cards):
                # Move cards to proper position
                dropped_card.position = pile.center_x, pile.center_y

            # Success, don't reset position of cards
            reset_position = False
        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        # We are no longer holding cards
        self.held_cards = []


    
    def on_mouse_motion(self,x : float, y: float, dx: float, dy: float):

        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        for tower in self.held_cards:
            tower.center_x += dx
            tower.center_y += dy


    
    def add_enemy(self,delta_time: float,enemy):
        self.enemy_list.append(enemy)
        
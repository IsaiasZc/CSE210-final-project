import arcade
from game import constants
from game.director import MenuView

def main():
    """Main function"""
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()
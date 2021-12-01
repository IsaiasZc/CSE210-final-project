import arcade
from game import constants
from game.director import Director, InstructionView, MenuView

def main():
    """Main function"""
    # window = Director()
    # window.setup()
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = MenuView()
    window.show_view(start_view)
    # start_view.setup()
    arcade.run()

if __name__ == '__main__':
    main()
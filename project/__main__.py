import arcade
from game.director import Director 

def main():
    """Main function"""
    window = Director()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
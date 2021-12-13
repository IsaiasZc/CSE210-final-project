import arcade
import os

WIDTH = 1200
HEIGHT = 800

FADE_RATE = 5


class FadingView(arcade.View):
    def __init__(self):
        super().__init__()
        self.fade_out = None
        self.fade_in = 255
        self.background = arcade.load_texture("game/images/sand_map.jpg")
        self.instructions_bg = arcade.load_texture("game/images/instructions_bg.jpg")        
        self.game_over_bg = arcade.load_texture("game/images/game_over.jpg")
        self.main_menu_bg = arcade.load_texture("game/images/characters_bg.png")
        # Backgrounds
        self.bg_switch = False
        self.draw_timer = 0
        self.bg_x_timer = 0
        self.bg_x = []
        self.backgrounds = []
        path = "game/images/backgrounds"
        temp_bg = os.listdir(path)
        for bg in temp_bg:
            self.backgrounds.append(arcade.load_texture(path + "/" + bg))

        for i in range(len(self.backgrounds)):
            self.bg_x.append((i * 1200) - 800)

        #Sounds
        self.background_sound = arcade.load_sound("project/game/sounds/Darkling_back_sound.mp3")
     
    def update_fade(self, next_view=None):
        if self.fade_out is not None:
            self.fade_out += FADE_RATE
            if self.fade_out is not None and self.fade_out > 255 and next_view is not None:
                game_view = next_view()
                game_view.setup()
                self.window.show_view(game_view)

        if self.fade_in is not None:
            self.fade_in -= FADE_RATE
            if self.fade_in <= 0:
                self.fade_in = None

    def draw_fading(self):
        if self.fade_out is not None:
            arcade.draw_rectangle_filled(self.window.width / 2, self.window.height / 2,
                                         self.window.width, self.window.height,
                                         (0, 0, 0, self.fade_out))

        if self.fade_in is not None:
            arcade.draw_rectangle_filled(self.window.width / 2, self.window.height / 2,
                                         self.window.width, self.window.height,
                                         (0, 0, 0, self.fade_in))

import random
from game.zombie import Zombie
import arcade


class Waves():

    def __init__(self):
        """The class constructor."""

        max_enemies_in_wave = 20
        wave_number = 0
        wave_life = 0
        enemies_list = []
        enemies_in_wave = arcade.SpriteList()
        generation_timer = 0
        time_between_enemies = 2
    
    def add_new_wave(self):
        self.wave_number += 1
        self.enemies_in_wave.clear()

        # self.max_enemies_in_wave *= 1.3
        for _ in range(self.max_enemies_in_wave - 1):
            #? Do i need a copy.deepcopy() here?
            enemy = random.choice(self.enemies_list)
            self.enemies_in_wave.append(enemy)

    def update_wave(self,delta_time):

        while len(self.enemies_in_wave) < self.max_enemies_in_wave:
            self.generation_timer += delta_time
            if self.generation_timer >= self.time_between_enemies:
                self.new_enemy()
            else:
                break



    def add_point(self):
        pass

    def new_enemy(self):

        enemy = random.choice(self.enemies_list)
        self.enemies_in_wave.append(enemy)

    def reset(self):
        """Set the values as the beggining of the game."""
        # TODO: Call the reset() in the setup to prepare the wave
        self.max_enemies_in_wave = 20
        self.wave_number = 1
        self.wave_life = 3
        self.enemies_list = [Zombie()]
        self.enemies_in_wave.clear()
        self.time_between_enemies = 2
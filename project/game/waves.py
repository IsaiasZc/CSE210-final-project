import random
from game.zombie import Zombie
import arcade
import math


class Waves():

    def __init__(self):
        """The class constructor."""

        self.wave_number = 0
        self.max_enemies_in_wave = 10
        self.enemies_counter = 0
        self.wave_life = 0
        self.enemies_list = []
        self.enemies_in_wave = arcade.SpriteList()
        self.generation_timer = 0
        self.time_between_enemies = 2
        self.multiplayed = 1.2
    
    def add_new_wave(self):
        """Just call this method when the last wave has ended."""
        self.wave_number += 1
        self.enemies_counter = 0
        self.max_enemies_in_wave = math.floor(self.max_enemies_in_wave * self.multiplayed)
        self.wave_life = math.floor(self.wave_life * self.multiplayed)
        self.time_between_enemies = round(self.time_between_enemies / self.multiplayed,2)
        self.enemies_in_wave = arcade.SpriteList()


        # # self.max_enemies_in_wave *= 1.3
        # for _ in range(self.max_enemies_in_wave - 1):
        #     enemy = random.choice(self.enemies_list)
        #     self.enemies_in_wave.append(self.create_enemy(enemy))

    def update_wave(self,delta_time):

        while self.enemies_counter < self.max_enemies_in_wave:
            self.generation_timer += delta_time
            if self.generation_timer >= self.time_between_enemies:
                self.generation_timer = 0
                self.new_enemy()
            else:
                break

        self.enemies_in_wave.update()
        for enemy in self.enemies_in_wave:
            enemy.move()
        
        print(self.enemies_counter)

    def add_point(self):
        pass

    def new_enemy(self):

        enemy = random.choice(self.enemies_list)
        self.enemies_in_wave.append(self.create_enemy(enemy))
        self.enemies_counter += 1

    def reset(self):
        """Set the values as the beggining of the game."""
        # TODO: Call the reset() in the SETUP to prepare the wave
        self.max_enemies_in_wave = 10
        self.wave_number = 1
        self.wave_life = 3
        self.enemies_counter = 0
        self.enemies_list = [Zombie()]
        self.enemies_in_wave = arcade.SpriteList()
        self.time_between_enemies = 2

    def create_enemy(self, enemy):
        if enemy.name == "zombie":
            return Zombie()
    
    def end_wave(self):
        return self.max_enemies_in_wave == self.enemies_counter and len(self.enemies_in_wave) == 0
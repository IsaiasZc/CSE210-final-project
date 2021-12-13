import arcade
import math

class Towers(arcade.Sprite):
    """A code template for the towers will be created in the game. The responsability
    of this class is to interect with enemies to destroy them.
    
    Stereotype:
        Controller
    
    Atributes:
        damage (Number): The damage of the tower for each bullet.
        attack_range (Number): The radius of the range attack.
        _bullet_image (path): the path of the bullet image.
        _bullet_list (List): A SpriteList to store all the bullets.
        bullet_speed (Number): the bullet speed.
        fire_rate (NUmber): The fire rate in seconds.
        selected (Boolean): Store when the tower has been selected from the panel.
        max_attacked (Number): The quantity of enemies can be attacked at same time.
        max_been_attacked (lLst): max enemies been attacked at same time.
        _time_since_last_attack (Number): count the time since last attack.
        in_panel (Boolean): Determine if the tower is upon the panel.
    """

    def __init__(self,image, scale):
        super().__init__(image, scale)


        self.damage = None
        self.attack_range = None
        self._bullet_image = None
        self._bullet_list = arcade.SpriteList()
        self.bullet_speed = None
        self.fire_rate = None
        self.selected = False
        self.max_attacked = None
        self.max_been_attacked = []
        self._time_since_last_attack = 0
        self.in_panel = True
        self.price = None
        self.upgrade_price = None
        self.tower_level = 1
        self.multiplier = 0.3

        self.bullet_sound = None
        self.hit_sound = None

    def tower_atack(self, enemy_list):


        if not self.in_panel:
            # WHere the attack start
            for enemy in enemy_list: 
                if (enemy in self.max_been_attacked) and (self.in_range(enemy) == False):
                    # self.player_b = arcade.play_sound(self.bullet_sound, volume=0.5)
                    self.max_been_attacked.remove(enemy)
                    continue

                if self.can_attack(enemy):
                    self.player_b = arcade.play_sound(self.bullet_sound, volume=0.5)
                    self.max_been_attacked.append(enemy)
                
            for enemy in self.max_been_attacked:
                if enemy.life <= 0:
                    self.max_been_attacked.remove(enemy)
                else:
                    self.attack(enemy)
    
    def attack(self,enemy):
        start_x = self.center_x
        start_y = self.center_y

        # Where the attack ends
        end_x = enemy.center_x
        end_y = enemy.center_y

        # calculate the bullet to destination.
        dif_x = end_x  - start_x
        dif_y = end_y - start_y

        angle = math.atan2(dif_y, dif_x)

        bullet = self.new_bullet()
        bullet.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * self.bullet_speed
        bullet.change_y = math.sin(angle) * self.bullet_speed

        self._bullet_list.append(bullet)


    def on_update(self,delta_time,enemy_list):
        self._time_since_last_attack += delta_time

        if self._time_since_last_attack >= self.fire_rate:
            self._time_since_last_attack = 0
            self.tower_atack(enemy_list)

    def new_bullet(self):

        bullet = arcade.Sprite(self._bullet_image,0.5)
        bullet.center_x = self.center_x
        bullet.center_y = self.center_y
    
        return bullet

    def set_bullet_image(self,image):
        self._bullet_image = image

    # def bullet_sound(self):
    #     if self.can_attack():
    #         self.player_b = arcade.play_sound(self.bullet_sound, volume=0.5)

    def update_bullet(self,wave):
            
        for bullet in self._bullet_list:   
            # self.bullet_sound()
            if bullet.center_x < 0 or bullet.center_x > 1200 or bullet.center_y < 0 or bullet.center_y > 800:
                bullet.kill()
                continue

            for enemy in wave.enemies_in_wave:
                if arcade.check_for_collision(bullet,enemy):
                    enemy.life -= self.damage
                    # *self._bullet_list.remove(bullet)
                    arcade.stop_sound(self.player_b)
                    arcade.play_sound(self.hit_sound)
                    bullet.kill()
                
                if (enemy.life <= 0) and (enemy in self.max_been_attacked):
                    self.max_been_attacked.remove(enemy)
                    
                if enemy.life <= 0:
                    wave.coins += enemy.kill_coins
                    enemy.kill()

            bullet.update()

    def draw_bullet(self):
        for bullet in self._bullet_list:
            bullet.draw()

    def draw_radius(self, path,towers_list):
        in_path = arcade.check_for_collision_with_list(self,path)
        on_other_towers = arcade.check_for_collision_with_list(self,towers_list)

        if (len(in_path) > 0 or len(on_other_towers) > 0) and self.selected:
            arcade.draw_circle_filled(self.center_x,self.center_y, self.attack_range,(255, 80, 0, 60))
        elif self.selected:
            arcade.draw_circle_filled(self.center_x,self.center_y, self.attack_range,(119, 243, 79, 60))

    def in_range(self, enemy):
        return math.dist(enemy.position, self.position) <= self.attack_range

    
    def can_attack(self, enemy):
        
        return (self.in_range(enemy)
        and (len(self.max_been_attacked) < self.max_attacked)
        and enemy.focus == False)
    
    def upgrade(self,multiplicand_list,fire_rate=None):
        #* upgrade_list = [self.damage,self.fire_rate,self.price]

        self.tower_level += 1
        for element in multiplicand_list:
            element = round(element + (element * self.multiplier))
        if fire_rate:
            fire_rate -= (fire_rate * self.multiplier)

    def set_upgrade(self):
        pass
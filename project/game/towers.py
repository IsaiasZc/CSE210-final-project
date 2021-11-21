import arcade
import math

class Towers(arcade.Sprite):
    """Towers template"""

    def __init__(self,image, scale):
        super().__init__(image, scale)


        self.damage = None
        self._frames = 60
        self.attack_range = ""
        self._bullet_image = None
        self._bullet_list = arcade.SpriteList()
        self.bullet_speed = None
        self.count = 0
        self.fire_rate = 1
    
    def tower_atack(self, enemy):
            
        self.count += self.fire_rate

        # WHere the attack start
        start_x = self.center_x
        start_y = self.center_y

        # Where the attack ends
        end_x = enemy.center_x
        end_y = enemy.center_y

        # calculate the bullet to destination.
        dif_x = end_x  - start_x
        dif_y = end_y - start_y

        angle = math.atan2(dif_y, dif_x)

        
        if self.count % self._frames == 0:

            bullet = self.new_bullet()
            bullet.angle = math.degrees(angle)

            bullet.change_x = math.cos(angle) * self.bullet_speed
            bullet.change_y = math.sin(angle) * self.bullet_speed

            self._bullet_list.append(bullet)


    def new_bullet(self):

        bullet = arcade.Sprite(self._bullet_image,0.5)
        bullet.center_x = self.center_x
        bullet.center_y = self.center_y

        return bullet
    
    def set_bullet_image(self,image):
        self._bullet_image = image

    def update_bullet(self):
        for bullet in self._bullet_list:
            if bullet.center_x < 0 or bullet.center_x > 1200 or bullet.center_y < 0 or bullet.center_y > 800:
                bullet.remove_from_sprite_lists()
            bullet.update()

    def draw_bullet(self):
        for bullet in self._bullet_list:
            bullet.draw()
            # self.get_bullet_list()

    def get_bullet_list(self):
        return self._bullet_list


    def on_mouse_pressed(self):
        pass

    def on_mouse_motion(self):
        pass

    def on_mouse_released(self):
        pass

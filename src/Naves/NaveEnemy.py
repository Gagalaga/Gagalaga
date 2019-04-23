import math

import pygame

from src.Naves.Nave import Nave


class NaveEnemy(Nave):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position, velocidade_inicial=0, hardness = 2):
        image_dir = "static/Images/Enemies/Cherry/skull-cherry.png"
        Nave.__init__(self, screen, position, image_dir)

        self.velocity = velocidade_inicial
        self._life = hardness*self._life


    def shoot_user(self, position_to_shoot):
        relative_position = (position_to_shoot[0] - self.position[0],
                             position_to_shoot[1] - self.position[1])
        norm = math.sqrt(relative_position[0]**2 + relative_position[1]**2)
        vector = (relative_position[0]/norm*100,
                  relative_position[1]/norm*100)
        return self.shooting(vector)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity):
        self._velocity = new_velocity

    def updates_position(self, delta_t):
        width, height = pygame.display.get_surface().get_size()
        self._position = (self._velocity[0] * delta_t + self._position[0],
                          self._velocity[1] * delta_t + self._position[1])

        if (self._position[0] < -self._size[0]/2 or self._position[0] + self._size[0]/2 > width):
            self.velocity = (-self.velocity[0], self.velocity[1])
        
        if(self._position[1] < -self._size[1]/2 or self._position[1] + self._size[1]/2 > height): 
            self.velocity = (self.velocity[0], -self.velocity[1])
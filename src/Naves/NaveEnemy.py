import math

import pygame

from src.Naves.Nave import Nave
from src.Shot import BotsShot
from src.GlobalState import GlobalState
from src.Trackable import Trackable


class NaveEnemy(Nave, Trackable):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position, velocidade_inicial=0, hardness = 2):
        image_dir = "static/Images/Enemies/Cherry/skull-cherry.png"
        Nave.__init__(self, screen, position, image_dir)
        Trackable.__init__(self)

        self.velocity = velocidade_inicial
        self._life = hardness*self._life

    def _register_on(self):
        GlobalState.getInstance().add_bot(self)

    def _unregister_on(self):
        GlobalState.getInstance().remove_bot(self)

    def shooting(self):
        position_to_shoot = GlobalState.getInstance().nave.position
        relative_position = (position_to_shoot[0] - self.position[0],
                             position_to_shoot[1] - self.position[1])
        norm = math.sqrt(relative_position[0]**2 + relative_position[1]**2)
        vector = (relative_position[0]/norm*100,
                  relative_position[1]/norm*100)
        shoot = BotsShot((self._position[0] + self._size[0]/2, self._position[1]), vector, self._screen, "static/Images/Enemies/Cherry/cherry-gun.png", (15,30))
        return shoot

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
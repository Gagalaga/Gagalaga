import pygame

from src.Naves.Nave import Nave
from src.Shot import Shot


class NaveUser(Nave):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position):
        image_dir = "static/Images/Player/player.png"
        Nave.__init__(self, screen, position, image_dir)

        self.velocity = (0,0)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity):
        self._velocity = new_velocity

    def shooting(self):
        shoot = Shot((self._position[0] + 50, self._position[1]), (0, -100), self._screen)
        return shoot

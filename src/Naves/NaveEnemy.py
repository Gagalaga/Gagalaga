import pygame

from src.Naves.Nave import Nave


class NaveEnemy(Nave):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position, velocidade_inicial=0):
        image_dir = "static/Images/Enemies/Cherry/skull-cherry.png"
        Nave.__init__(self, screen, position, image_dir)

        self.velocity = velocidade_inicial

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity):
        self._velocity = new_velocity
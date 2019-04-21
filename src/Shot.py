import pygame
import os

from src.Config import color_configs as colors

from src.Drawable import Drawable
from src.Collideable import Collideable


class Shot(Drawable, Collideable):
    """
    A class that encapsulates the logic behind of a shot.
    Being it from an user or an enemy.
    """

    def __init__(self, current_position, current_velocity, screen):
        Drawable.__init__(self, current_position, current_velocity, screen, (5,10))
        self._shotImage = pygame.image.load(os.path.abspath("static/Images/Player/player-gun.png"))
        self._shotImage = pygame.transform.scale(self._shotImage, self._size)
        self._shotImage = self._shotImage.convert()

        Collideable.__init__(self, self._shotImage)


    def draw(self):
        self._screen.blit(self._shotImage, self._position)

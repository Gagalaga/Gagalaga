import pygame

from src.Config import color_configs as colors

from src.Drawable import Drawable


class Shot(Drawable):
    """
    A class that encapsulates the logic behind of a shot.
    Being it from an user or an enemy.
    """

    def __init__(self, current_position, current_velocity, screen):
        Drawable.__init__(self, current_position, current_velocity, screen)

    def draw(self):
        self._surface = pygame.Surface((5, 10))
        self._surface.fill(colors['white'])
        self._screen.blit(self._surface, self._position)

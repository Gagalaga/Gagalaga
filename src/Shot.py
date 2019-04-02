import pygame
import os

from src.Config import color_configs as colors

from src.Drawable import Drawable


class Shot(Drawable):
    """
    A class that encapsulates the logic behind of a shot.
    Being it from an user or an enemy.
    """

    def __init__(self, current_position, current_velocity, screen):
        Drawable.__init__(self, current_position, current_velocity, screen, (5,10))
        self._shotImage = pygame.image.load(os.path.abspath("static/Images/Player/player-gun.png"))
        self._shotImage = pygame.transform.scale(self._shotImage, self._size)
        self._shotImage = self._shotImage.convert()
        pygame.mixer.init()
        shot_sound = pygame.mixer.Sound('./static/sounds/shoot1.wav')
        shot_sound.set_volume(0.01)
        shot_sound.play()

    def draw(self):
        self._screen.blit(self._shotImage, self._position)

from abc import ABC, abstractclassmethod

import pygame
import os

from src.Config import color_configs as colors
from src.GlobalState import GlobalState

from src.Drawable import Drawable
from src.Collideable import Collideable
from src.Trackable import Trackable

class Shot(Drawable, Collideable, ABC):
    """
    A class that encapsulates the logic behind of a shot.
    Being it from an user or an enemy.
    """

    def __init__(self, current_position, current_velocity, screen, archive, size):
        Drawable.__init__(self, current_position, (current_velocity[0], current_velocity[1]) , screen, size)
        self._shotImage = pygame.image.load(os.path.abspath(archive))
        self._shotImage = pygame.transform.scale(self._shotImage, self._size)
        self._shotImage = self._shotImage.convert_alpha()

        pygame.mixer.init()
        shot_sound = pygame.mixer.Sound('./static/sounds/shoot1.wav')
        shot_sound.set_volume(0.5)
        shot_sound.play()

        Collideable.__init__(self)

    def draw(self):
        self._screen.blit(self._shotImage, self._position)

    @property
    def image(self):
        return self._shotImage

    @property
    def position(self):
        return self._position

class BotsShot(Shot, Trackable):
    def __init__(self, current_position, current_velocity, screen, archive, size):
        Shot.__init__(self, current_position, current_velocity, screen, archive, size)
        Trackable.__init__(self)

    def _register_on(self):
        GlobalState.getInstance().add_botsshot(self)

    def _unregister_on(self):
        GlobalState.getInstance().remove_botsshot(self)

class UserShot(Shot, Trackable):
    def __init__(self, current_position, current_velocity, screen, archive, size):
        Shot.__init__(self, current_position, current_velocity, screen, archive, size)
        Trackable.__init__(self)

    def _register_on(self):
        GlobalState.getInstance().add_shot(self)

    def _unregister_on(self):
        GlobalState.getInstance().remove_shot(self)
    

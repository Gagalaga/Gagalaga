import pygame

from abc import ABCMeta, abstractmethod


class Drawable:
    """
    An abstract class that represent all the mobile objects of the game.
    It's subclassed by each drawable element.
    """

    __metaclass__ = ABCMeta

    def __init__(self, current_position, current_velocity, screen):
        self._position = current_position
        self._velocity = current_velocity
        self._screen = screen

    def updates_position(self, delta_t):
        self._position = (self._velocity[0] * delta_t + self._position[0],
                          self._velocity[1] * delta_t + self._position[1])
        return self._position

    @abstractmethod
    def draw(self):
        """
        Warning: Clear screen before updating the components.
        """
        pass

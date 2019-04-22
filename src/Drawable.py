import pygame

from abc import ABCMeta, abstractmethod


class Drawable():
    """
    An abstract class that represent all the mobile objects of the game.
    It's subclassed by each drawable element.
    """

    __metaclass__ = ABCMeta

    def __init__(self, current_position, current_velocity, screen, size):
        self._position = current_position
        self._velocity = current_velocity
        self._screen = screen
        self._size = size

    def updates_position(self, delta_t):
        self._position = (self._velocity[0] * delta_t + self._position[0],
                          self._velocity[1] * delta_t + self._position[1])
        return self._position

    def out_screen(self):
        width, height = pygame.display.get_surface().get_size()
        if (self._position[0] + self._size[0] < 0 or self._position[0] - self._size[0] > width
            or self._position[1] + self._size[1] < 0 or self._position[1] - self._size[1] > height):
            return True
        return False


    @abstractmethod
    def draw(self):
        """
        Warning: Clear screen before updating the components.
        """
        pass

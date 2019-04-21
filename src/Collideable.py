import pygame
from pubsub import pub

from abc import ABCMeta, abstractmethod


class Collideable():
    """
    An abstract class that represent all the objects that may collide.
    The collision engine uses masks.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        self.rect = self.image.get_rect()
        #self.mask = self.image.get_masks()
        self.mask = pygame.mask.from_surface(self.image)

    def update_mask(self):
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    @property
    @abstractmethod
    def image(self):
        pass
        
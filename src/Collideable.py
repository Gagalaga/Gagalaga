import pygame

from abc import ABCMeta, abstractmethod


class Collideable(pygame.sprite.Sprite):
    """
    An abstract class that represent all the objects that may collide.
    The collision engine uses masks.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.position)

    @property
    @abstractmethod
    def image(self):
        pass

    @property
    @abstractmethod
    def position(self):
        pass
        
import pygame

from abc import ABCMeta, abstractmethod


class Collideable(pygame.sprite.Sprite):
    """
    An abstract class that represent all the objects that may collide.
    The collision engine uses masks.
    """

    __metaclass__ = ABCMeta

    def __init__(self, reference_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.update_mask(reference_sprite)

    def update_mask(self, reference_sprite):
        self.rect = reference_sprite.get_rect()
        self.mask = pygame.mask.from_surface(reference_sprite)
        

import pygame
import pubsub

from abc import ABCMeta, abstractmethod


class Collideable():
    """
    An abstract class that represent all the objects that may collide.
    The collision engine uses masks.
    """

    __metaclass__ = ABCMeta

    def __init__(self, image):
        self.mask = pygame.mask.from_surface(image)

    def update_mask(self, reference_sprite):
        self.rect = reference_sprite.get_rect()
        self.mask = pygame.mask.from_surface(reference_sprite)

    def __collided_func(self, sprite_first, sprite_second):
        point = pygame.sprite.collide_mask(sprite_first, sprite_second)
        return point != None

    def collideswith(self, group_collideable):
        collided_sprite = pygame.sprite.spritecollideany(self, group_collideable, self.__collided_func)
        pubsub.sendMessage('remove_shot', bot=collided_sprite)
        
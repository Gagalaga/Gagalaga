from src.Drawable import Drawable
from src.Collideable import Collideable
import pygame

class Bonus(Drawable, Collideable):

    """
    A class that abstracts the bonus for the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position, image_dir):
        """
        Initializes the user's bonus at a given position.
        """
        Drawable.__init__(self, position, (0, 0), screen, (30, 30))

        self._image = pygame.image.load(image_dir)
        self._image = pygame.transform.scale(self._image, self._size)
        self._image = self._image.convert_alpha()
        self._screen.blit(self._image, self._position)

        Collideable.__init__(self)

    def draw(self):
        self._screen.blit(self._image, self._position)

    @property
    def image(self):
        return self._image

    @property
    def position(self):
        return self._position
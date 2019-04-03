import pygame

from src.Drawable import Drawable
from src.Collideable import Collideable
from src.Shot import Shot


class Nave(Drawable, Collideable):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position, image_dir):
        """
        Initializes the user's nave at a given position.
        An example of a position input: position = (30,30).
        """
        Drawable.__init__(self, position, (0, 0), screen, (100, 100))
        pygame.sprite.Sprite.__init__(self)

        self._image = pygame.image.load(image_dir)
        self._image = pygame.transform.scale(self._image, self._size)
        self._screen.blit(self._image, self._position)
        pygame.display.update()

        Collideable.__init__(self, self._image)

    def horizontal_moving(self, movements):
        displacement = movements * (10)
        self._position = (self._position[0] + displacement, self._position[1])

    def vertical_moving(self, movements):
        displacement = movements * (10)
        self._position = (self._position[0], self._position[1] + displacement)
    
    def shooting(self):
        shoot = Shot((self._position[0] + 50, self._position[1]), (0, -100), self._screen)
        return shoot

    def draw(self):
        self.update_mask(self._image)
        self._screen.blit(self._image, self._position)

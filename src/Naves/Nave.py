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
        # This line adjusts the drawing to place the element in the screen, instead of out of that
        position = (position[0] - 50, position[1] - 100)
        
        Drawable.__init__(self, position, (0, 0), screen, (100, 100))

        self._image = pygame.image.load(image_dir)
        self._image = pygame.transform.scale(self._image, self._size)
        self._image = self._image.convert_alpha()
        self._screen.blit(self._image, self._position)
        
        # This variable implements the life in a very simple way
        self._life = 10

        Collideable.__init__(self)

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
        self._screen.blit(self._image, self._position)

    @property
    def image(self):
        return self._image

    @property
    def position(self):
        return self._position

    def should_be_dead(self):
        return self._life <= 0

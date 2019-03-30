import pygame

from src.Drawable import Drawable
from src.Shot import Shot


class NaveUser(Drawable):
    """
    A class that abstracts the nave from the user.
    Inherits from pygame.Sprite.
    """

    def __init__(self, screen, position):
        """
        Initializes the user's nave at a given position.
        An example of a position input: position = (30,30).
        """
        Drawable.__init__(self, position, (0, 0), screen)

        self._image = pygame.image.load("static/Images/Player/player.png")
        self._image = pygame.transform.scale(self._image, (100, 100) )
        self._screen.blit(self._image, self._position)
        pygame.display.update()

        # self.mask = pygame.mask.from_surface(self.image)

    def horizontal_moving(self, movements):
        displacement = movements * (10)
        self._position = (self._position[0] + displacement, self._position[1])

    def vertical_moving(self, movements):
        displacement = movements * (10)
        self._position = (self._position[0], self._position[1] + displacement)
    
    def shooting(self):
        shoot = Shot((self._position[0] + 50, self._position[1] + 100), (0, -50), self._screen)
        return shoot

    def draw(self):
        self._screen.blit(self._image, self._position)

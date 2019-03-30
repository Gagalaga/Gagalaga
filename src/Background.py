import pygame

from src.Drawable import Drawable


class Background(Drawable):
    """
    A class to draw th e background and keep it scrolling
    """

    def __init__(self, screen):
        """
            Keeps the background scrolling
        """
        # Sets the position of the background as the center of the screen
        position = ((1/2)*screen['width'], (1/2)*screen['height'])

        Drawable.__init__(self, position, (0, 0), screen)

        self._image = pygame.image.load("static/Images/Background/background.png")
        # Splits the background image in the screen upgraded by 0.1 in the heigth
        self._image = pygame.transform.scale(self._image, (screen['width'], 1.1*screen['height']))
        self._screen.blit(self._image, self._position)
        
        pygame.display.update()

        # self.mask = pygame.mask.from_surface(self.image)

    def vertical_moving(self, rate):
        displacement = 10*rate
        self._position = (self._position[0], self._position[1] + displacement)

    def draw(self):
        self._screen.blit(self._image, self._position)
        # Here, the rate have to increase according with difficulty
        rate = 1
        self.vertical_moving(rate)
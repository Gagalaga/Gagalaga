import pygame

from src.Drawable import Drawable


class Background(Drawable):
    """
    A class to draw th e background and keep it scrolling
    """

    def __init__(self, screen, reference):
        """
            Keeps the background scrolling
        """
        # Sets the position of the background as the center of the screen
        width, height = pygame.display.get_surface().get_size()
        self._position = (0, -(height + reference*(4*height)))

        Drawable.__init__(self, self._position, (0, 0), screen, (width, int(4*height)))

        self._image = pygame.image.load("static/Images/Background/bacground(1).png")
        # Splits the background image in the screen upgraded by 1 in the heigth
        self._image = pygame.transform.scale(self._image, self._size)
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
    
    def updates_position(self, delta_t):
        self._position = (self._velocity[0] * delta_t + self._position[0],
                          self._velocity[1] * delta_t + self._position[1])
        # Looping Background
        _, height = pygame.display.get_surface().get_size()
        if(self._position[1] == height):
            self._position = (0, -(height + (4*height)))
            
        return self._position
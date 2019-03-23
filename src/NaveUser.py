import pygame

from src.Config import cor_configs as cores

from src.Drawable import Drawable
from src.Tiro import Tiro

class NaveUser(Drawable):
    """
    Uma classe que abstrai a Nave do Usuário.
    Herda de pygame.Sprite.
    """


    def __init__(self, screen, position):
        """
        Initializes the user's nave at a given position.
        An example of a position input: position = (30,30).
        """
        Drawable.__init__(self, position, (0,0), screen)

        self._image = pygame.image.load("static/images/cherry.jpeg")
        self._screen.blit(self._image, self._posicao)
        pygame.display.update()
        #self.mask = pygame.mask.from_surface(self.image)

    def mover_horizontal(self, unidades):
        """
        Move tantas unidades a direita.
        Unidades > 0 => Direita.
        Unidades < 0 => Esquerda.
        """
        deslocamento = unidades * (10)

        self._posicao = (self._posicao[0]+deslocamento, self._posicao[1])


    def atirar(self):
        tiro = Tiro(self._posicao, (0,-50), self._screen)
        return tiro


    def draw(self):
        """"
        Método sobrescrito da classe abstrata Drawable.
        """
        self._screen.blit(self._image, self._posicao)
    
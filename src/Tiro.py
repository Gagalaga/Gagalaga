import pygame

from src.Config import cor_configs as cores

from src.Drawable import Drawable

class Tiro(Drawable):
    """
    Uma classe que encapsula a lógica por trás de um tiro, seja ele
    do usuário ou de um bot
    """


    def __init__(self, posicao_inicial, velocidade_inicial, screen):
        Drawable.__init__(self, posicao_inicial, velocidade_inicial, screen)


    def draw(self):
        self._surface = pygame.Surface((5,10))
        self._surface.fill(cores['white'])
        self._screen.blit(self._surface, self._posicao)

import pygame

from abc import ABCMeta, abstractmethod

class Drawable:
    """
    Uma classe abstrata que representa objetos móveis impressos na tela.
    """

    __metaclass__ = ABCMeta

    def __init__(self, posicao_atual, velocidade_atual, screen):
        self._posicao = posicao_atual
        self._velocidade = velocidade_atual
        self._screen = screen


    def atualiza_posicao(self, delta_t):
        self._posicao = (self._velocidade[0] * delta_t + self._posicao[0],
                         self._velocidade[1] * delta_t + self._posicao[1])
        return self._posicao

    @abstractmethod
    def draw(self):
        """
        Atenção: apague a tela antes de atualizar os componentes.
        """
        pass

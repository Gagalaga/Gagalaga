import pygame

from src.Config import screen_configs as screen

from src.GameEngine import GameEngine

class GUI:
    """
    Uma Interface Gráfica para o Usuário.
    """


    def __init__(self, size=[screen['largura'], screen['altura']]):
        """
        size: default é o screen_configs em Configs.py.
        """

        self.__configure_screen(size)
        self.__configure_sound()


    def __configure_sound(self):
        """
        Configura o som.
        """
        #pygame.mixer.init()
        #player = pygame.mixer.Sound('./../static/sounds/somesong.wav')
        #player.play()


    def __configure_screen(self, size):
        """
        Configura a tela.
        """
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Gagálaga - O Jogo")


    def get_screen(self):
        return self.__screen


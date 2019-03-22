import pygame

from src.GameEngine import GameEngine

class GUI:
    """Uma Interface Gráfica para o Usuário."""


    def __init__(self, size=[1000, 750]):
        """
        size: default é 1000 de largura e 750 de altura.
        """
        self.__size = size

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


    def run(self):
        """
        Dá o pontapé no GameLoop.
        """
        game_engine = GameEngine(self.__screen)
        game_engine.game_loop()

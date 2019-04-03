import pygame

from src.Config import screen_configs as screen


class GUI:
    def __init__(self, size=[screen['width'], screen['height']]):
        """
        size: default is the screen_configs in Configs.py.
        """

        self.__configure_screen(size)
        self.__configure_sound()

    """
    A Graphic User Interface.
    """

    def __configure_sound(self):
        """
        Configures the sound
        """
        # pygame.mixer.init()
        # player = pygame.mixer.Sound('./../static/sounds/somesong.wav')
        # player.play()

    def __configure_screen(self, size):
        """
        Configures the screen
        """
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Gagálaga - O Jogo")

    def get_screen(self):
        return self.__screen

import pygame

from src.Config import screen_configs as screen


class GUI:
    """
    A Graphic User Interface.
    """

    def __init__(self, size=[screen['width'], screen['height']]):
        """
        size: default is the screen_configs in Configs.py.
        """

        self.__configure_screen(size)
        self.__configure_sound()

    def __configure_sound(self):
        """
        Configures the sound
        """
        pygame.mixer.init()
        player = pygame.mixer.Sound('./static/sounds/original_sound_effects/theme_song.wav')
        player.play(0)

    def __configure_screen(self, size):
        """
        Configures the screen
        """
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Gagálaga - O Jogo")

    def get_screen(self):
        return self.__screen

import pygame
from abc import ABCMeta, abstractmethod

class Messenger:
    def __init__(self,screen):
        self.screen = screen

    def text_objects(self, text , color, size):
        font = pygame.font.SysFont('Comic Sans', size)
        textSurface = font.render(text, True , color)
        return textSurface, textSurface.get_rect() 

    def message_to_screen(self, text, color, x_delta =0 ,y_delta = 0 ,size = 50 ):
        textSurf, textRect = self.text_objects(text,color,size)
        textRect.center = self.screen.get_width()/2+x_delta , self.screen.get_height()/2+y_delta
        self.screen.blit (textSurf, textRect)
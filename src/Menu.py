import pygame, os, sys, math, random
from src.MenuInterface import MenuInterface
from src.Messenger import Messenger

class Menu(MenuInterface):
    def __init__(self,screen):
        self.screen = screen
        self.messenger = Messenger(screen)
        self.__select = 0
        self.__inMenu = True
        self.clock = pygame.time.Clock()

    def get_inMenu(self):
        return self.__inMenu
    def get_select(self):
        return self.__select
    def event_handler(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                    self.__select -=1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    self.__select +=1
                if self.__select > 1:
                    self.__select = 0
                elif self.__select < 0:
                    self.__select = 1

                if event.key == pygame.K_RETURN:
                    self.__inMenu = False
                    if self.__select == 0:
                        pass
                    if self.__select == 1:
                        pygame.quit()
                        return

import pygame, os, sys, math, random
from src.Menu import Menu
from src.Retangulo import Retangulo

class MenuInicial:
    def __init__(self,screen):
        self.menu = Menu(screen)
        self.blockList = [Retangulo(screen,"Meter o Gagá!",y_delta = 66)
                    ,Retangulo(screen,"Sugou",y_delta = 132)] 
        self.inicial_menu_loop()

    def inicial_menu_loop(self):
        while (self.menu.get_inMenu()):
            self.menu.clock.tick(10)
            self.menu.screen.fill((0,0,0))
            self.menu.messenger.message_to_screen(text="Gagálaga", color = (254, 200,0),
             x_delta= 0 , y_delta = -200, size=100)
            for ret in self.blockList:
                ret.message_to_screen()
            self.menu.event_handler(pygame.event.get())
            selected = self.blockList[self.menu.get_select()]
            pygame.draw.rect(self.menu.screen, (0,200,0), (selected.x, selected.y, 
            selected.width, selected.height),7)
            pygame.display.update()

    
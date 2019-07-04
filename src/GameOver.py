import pygame, os, sys, math, random
from src.GameOverInterface import GameOverInterface
from src.Menu import Menu
from src.Retangulo import Retangulo
class GameOver( ):
    def __init__(self,screen,score):
        self.menu = Menu(screen)
        self.blockList = [Retangulo(screen,"Cancerizar!",x_delta= -00)
                    ,Retangulo(screen,"Sugou",x_delta=200)]
        self.score = score 
        self.game_over_loop()

    def game_over_loop(self):
        while (self.menu.get_inMenu()):
            self.menu.clock.tick(10)
            self.menu.screen.fill((0,0,0))
            self.menu.messenger.message_to_screen(text ="Você pegou DP!",y_delta = -150 , color = (255,0,0))
            self.menu.messenger.message_to_screen(text ="Seu score foi: " + str(self.score), y_delta = -100,color =(255,255,255), size = 30)
            for ret in self.blockList:
                ret.message_to_screen()
            self.menu.event_handler(pygame.event.get())
                
            selected = self.blockList[self.menu.get_select()]
            pygame.draw.rect(self.menu.screen, (0,200,0), (selected.x, selected.y, selected.width, selected.height),7)
            pygame.display.update()



import pygame, os, sys, math, random

class Menu:
    def __init__(self,screen):
        self.select = 0
        self.screen = screen
        inMenu = True
        clock = pygame.time.Clock()

        while inMenu:
            clock.tick(10)
            screen.fill((0,0,0))
            #self.message_to_screen("Use arrows up and down, and enter to select ", y_delta = -200, color = (255, 255, 255))
            self.blockList = [Menu.Retangulo(screen,"Start",-100)
                    ,Menu.Retangulo(screen,"Best Scores",0)
                    ,Menu.Retangulo(screen,"Exit",100)]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.select -=1
                    elif event.key == pygame.K_DOWN:
                        self.select +=1
                    if self.select > 2:
                        self.select = 0
                    elif self.select < 0:
                        self.select = 2

                    if event.key == pygame.K_RETURN:
                        inMenu =False
                        if self.select == 0:
                            pass
                        if self.select == 1:
                            pass
                        if self.select == 2:
                            pygame.quit()
                            return
               
            selected = self.blockList[self.select]
            pygame.draw.rect(screen, (0,200,0), (selected.x, selected.y, selected.width, selected.height),7)
            pygame.display.update()

    def message_to_screen(self, text, y_delta=0, color = (0,0,0)):
        textSurf, textRect = self.text_objects(text,color)
        textRect.center = self.screen.get_width()/2 , self.screen.get_height()/2+y_delta
        self.screen.blit (textSurf, textRect)

    def text_objects(self, text , color):
            font = pygame.font.SysFont('Comic Sans', 50)
            textSurface = font.render(text, True , (0,0,0))
            return textSurface, textSurface.get_rect()
    
    class Retangulo:
        def __init__ (self, screen, text, y_delta = 0):
            self.screen = screen
            self.width = 300
            self.height = 50
            self.x = self.screen.get_width()/2 - self.width/2
            self.y = self.screen.get_height()/2 - self.height/2 + y_delta
            self.rect = pygame.draw.rect(self.screen, (150,150,150),(self.x,self.y,self.width,self.height))
            self.message_to_screen(text, y_delta)
        def text_objects(self, text , color):
            font = pygame.font.SysFont('Comic Sans', 50)
            textSurface = font.render(text, True , (0,0,0))
            return textSurface, textSurface.get_rect() 
        
        
        def message_to_screen(self, text, y_delta=0, color = (0,0,0)):
            textSurf, textRect = self.text_objects(text,color)
            textRect.center = self.screen.get_width()/2 , self.screen.get_height()/2+y_delta
            self.screen.blit (textSurf, textRect)
"""
pygame.init()
screen = pygame.display.set_mode((750,800))
pygame.display.set_caption("Menu")
menuu = Menu(screen)
pygame.time.delay(1000)
pygame.quit()
quit()
"""
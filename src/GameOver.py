import pygame, os, sys, math, random

class GameOver:
    def __init__(self,screen,score):
        self.select = 0
        self.screen = screen
        inGameOver = True
        clock = pygame.time.Clock()
        #bg = pygame.image.load('static/Images/Background/Menu_Bgnd.png')
        #D = pygame.image.load('static/Images/Degrees/D.png')
        #D = pygame.transform.scale(D, (70,70))
        scr_width, scr_height = (pygame.display.get_surface()).get_size()
        while inGameOver:
            clock.tick(10)
            screen.fill((0,0,0))
            self.message_to_screen("Você pegou DP!",y_delta = -150 )
            self.message_to_screen("Seu score foi: " + str(score), -100, (255,255,255), size = 30)

            #screen.blit(bg, (0,-100))
            #screen.blit(D, (scr_width/2-20,70))
            self.blockList = [GameOver.Retangulo(screen,"Cancerizar!",x_delta= -100)
                    ,GameOver.Retangulo(screen,"Sugou",100)]
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.select -=1
                    elif event.key == pygame.K_RIGHT:
                        self.select +=1
                    if self.select > 1:
                        self.select = 0
                    elif self.select < 0:
                        self.select = 1

                    if event.key == pygame.K_RETURN:
                        inGameOver=False
                        if self.select == 0:
                            pass
                        if self.select == 1:
                            pygame.quit()
                            return
               
            selected = self.blockList[self.select]
            pygame.draw.rect(screen, (0,200,0), (selected.x, selected.y, selected.width, selected.height),7)
            pygame.display.update()

    def message_to_screen(self, text, y_delta=0, color = (226,0,0), size = 40):
        textSurf, textRect = self.text_objects(text,color, size)
        textRect.center = self.screen.get_width()/2 , self.screen.get_height()/2+y_delta
        self.screen.blit (textSurf, textRect)

    def text_objects(self, text , color,size=40):
            font = pygame.font.SysFont('Arial Black', size)
            textSurface = font.render(text, True , color)
            return textSurface, textSurface.get_rect()
    
    class Retangulo:
        def __init__ (self, screen, text, x_delta = 0):
            self.screen = screen
            self.width = 150
            self.height = 50
            self.x = self.screen.get_width()/2 - self.width/2 + x_delta
            self.y = self.screen.get_height()/2 - self.height/2 
            self.rect = pygame.draw.rect(self.screen, (150,150,150),(self.x,self.y,self.width,self.height))
            self.message_to_screen(text, x_delta)
        def text_objects(self, text , color):
            font = pygame.font.SysFont('Comic Sans', 30)
            textSurface = font.render(text, True , (0,0,0))
            return textSurface, textSurface.get_rect() 
        
        
        def message_to_screen(self, text, x_delta=0, color = (0,0,0)):
            textSurf, textRect = self.text_objects(text,color)
            textRect.center = self.screen.get_width()/2 + x_delta , self.screen.get_height()/2
            self.screen.blit (textSurf, textRect)

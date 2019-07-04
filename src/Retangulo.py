import pygame 
from src.Messenger import Messenger
class Retangulo:
        def __init__ (self, screen, text, y_delta = 0, x_delta = 0):
            
            self.messenger = Messenger(screen)
            
            self.screen = screen
            self.text = text 
            self.y_delta = y_delta
            self.x_delta = x_delta
            self.width = 300
            self.height = 50
            self.x = self.screen.get_width()/2 - self.width/2 + x_delta
            self.y = self.screen.get_height()/2 - self.height/2 + y_delta
            self.rect = pygame.draw.rect(self.screen, (150,150,150),(self.x,self.y,self.width,self.height))
            self.message_to_screen()
        
        
        def message_to_screen(self):
            self.rect = pygame.draw.rect(self.screen, (150,150,150),(self.x,self.y,self.width,self.height))
            self.messenger.message_to_screen(self.text,color = (0,0,0), x_delta = self.x_delta,
            y_delta = self.y_delta , size = 50)
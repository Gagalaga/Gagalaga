import pygame

class NaveUser(pygame.sprite.Sprite):
    """
    Uma classe que abstrai a Nave do Usuário.
    Herda de pygame.Sprite.
    """


    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.__screen = screen

        self.image = pygame.image.load("static/images/cherry.jpeg")
        self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)


    def mover_direita(self, unidades):
        """
        Move tantas unidades a direita.
        """
        deslocamento = unidades * (50)
        print("Deslocamento:", deslocamento)
        self.rect.move(deslocamento,0)
        self.__screen.fill((0,0,0))
        self.__screen.blit(self.image, self.rect)
    
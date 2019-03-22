import pygame
import logging

from src.NaveUser import NaveUser

class GameEngine:
    """
    Uma classe fundamental que abstrai o funcionamento dos componentes do jogo.
    """


    def __init__(self, screen):
        self.__screen = screen

        # inicializando apropriadamente o Pygame
        self.__on_init()

        # lidando com burocracias do GameLoop
        self.__clock = pygame.time.Clock()
        self.__fps = 10
        self.__ended = False

        # elementos do jogo propriamente dito
        # MODIFICAR SEM MODERAÇÃO
        self.nave = NaveUser(self.__screen)


    def game_loop(self):
        """
        Um wrapper do funcionamento da GameEngine.
        """
        print("Starting Game Loop at ${0} fps".format(self.__fps))
        self.__clock.tick()
        while not self.__ended:
            self.__frame()


    def __frame(self):
        """
        Função que é executada a cada frame do jogo. 
        fps = frames per second
        """
        print("Updating frame...Now!")
        pygame.display.flip()     

        delta_t = self.__clock.tick(self.__fps)

        # value = pygame.sprite.collide_mask(self.__nave1, self.__nave2)
        # print(value)

        self.__event_handler()


    def __event_handler(self):
        """
        Trata os eventos gerados pelo usuário.
        Teclado: 'D'.
        Tela: 'Quit'.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("pygame.QUIT pressed by user")
                self.__ended = True
                self.__on_quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("Letter D pressed by user")
                    logging.info("Letter D pressed by user")
                    self.nave.mover_direita(1)


    def __collisions(self):
        pass


    def __on_init(self):
        """
        Método privado para lidar com a inicialização específica do PyGame.
        """
        print("Initializing pygame in 3 ... 2 ... 1 ...")
        pygame.init()


    def __on_quit(self):
        """
        Método privado para lidar com a finalização específica do PyGame. 
        """
        print("Quitting pygame in 3 ... 2 ... 1 ...")
        pygame.quit()
        
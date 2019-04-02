import pygame

from src.Background import Background
from src.NaveUser import NaveUser

from src.Config import color_configs as colors


class GameEngine:
    """
    A fundamental class that abstracts the game's components' operation.
    """

    def __init__(self, screen):
        self.__screen = screen

        # Appropriately initializing the game
        self.__on_init()

        # Setting basic features for the game functioning
        self.__clock = pygame.time.Clock()
        self.__fps = 10
        self.__ended = False

        # Particular elements of the game
        # Modifying area
        self.background = [Background(self.__screen, 0), Background(self.__screen, 1)]
        self.nave = NaveUser(self.__screen, (30, 30))

      
        self.bots = []
        self.shots = []

    def game_loop(self):
        """
        A wrapper of the GameEngine's operation
        """
        print("Starting Game Loop at ${0} fps".format(self.__fps))
        self.__clock.tick()
        while not self.__ended:
            self.__frame()

    def __frame(self):
        """

        Executed at each frame
        fps = frames per second.
        1º) Waits the next frame
        2°) Clear screen
        3°) Calculates and plots the new parameters
        4°) Ends the present frame
        """
        delta_t = self.__clock.tick(self.__fps) / 1000

        # Dispite the fact it may looks like trash, it keeps the image atualizing
        self.__screen.fill(colors['black'])

        drawables = self.background + [self.nave] + self.bots + self.shots

        for drawable in drawables:
            drawable.updates_position(delta_t)

        self.__event_handler()
        if self.__ended:
            return

        for drawable in drawables:
            drawable.draw()

        pygame.display.flip()

        # value = pygame.sprite.collide_mask(self.__nave1, self.__nave2)
        # print(value)

        self.__event_handler()

    def __event_handler(self):
        """
        Treats the user generated events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("pygame.QUIT pressed by user")
                self.__ended = True
                self.__on_quit()
                return

        # Keep shoting all the time
        self.shots.append(self.nave.shooting())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.nave.horizontal_moving(1)
        if keys[pygame.K_a]:
            self.nave.horizontal_moving(-1)
        if keys[pygame.K_s]:
            self.nave.vertical_moving(1)
        if keys[pygame.K_w]:
            self.nave.vertical_moving(-1)

    def __collisions(self):
        pass

    def __on_init(self):
        """
        Private method for treating specifically of pygame's initialization.
        """
        print("Initializing pygame in 3 ... 2 ... 1 ...")
        pygame.init()

    def __on_quit(self):
        """
        Private method for treating specifically of pygame's interrupting.
        """
        print("Quitting pygame in 3 ... 2 ... 1 ...")
        pygame.quit()

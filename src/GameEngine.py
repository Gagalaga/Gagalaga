import pygame

from src.Background import Background
from src.GlobalState import GlobalState
from src.Naves.NaveUser import NaveUser
from src.Naves.NaveEnemy import NaveEnemy

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
        self.nave = NaveUser(self.__screen, (300, 300))

        self.state = GlobalState(self.nave)

        self.__initializing_bots(5)

    @property
    def _drawables(self):
        return self.background + [self.nave] + self.state.list_all()

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
        2°) Clears screen
        3°) Recalculates positions
        4°) Handles keyboard interactions
        5°) Prints elements in their new positions
        6°) Calculates collisions
        7°) Calculates off the screen objects
        """
        delta_t = self.__clock.tick(self.__fps) / 1000

        # Dispite the fact it may looks like trash, it keeps the image atualizing
        self.__screen.fill(colors['black'])

        for drawable in self._drawables:
            drawable.updates_position(delta_t)

        self.__event_handler()
        if self.__ended:
            return

        for drawable in self._drawables:
            drawable.draw()

        pygame.display.flip()

        self.__collisions()
        self.__out_screen()

    def __initializing_bots(self, number_bots):
        """
        Instatiates the bots e saves them into the GlobalState
        """
        for i in range(1,number_bots):
            self.state.add_bot(NaveEnemy(self.__screen, (30-100*i, 30), (50, 0)))

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

        # Keep shoting all tyhe time
        self.state.add_shot(self.nave.shooting())

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
        self.state.handle_collisions()

    def __out_screen(self):
        self.state.handle_out_screen()

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

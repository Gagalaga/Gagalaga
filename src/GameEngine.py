import time
import random 

import pygame

from src.Menu import Menu
from src.Background import Background
from src.GlobalState import GlobalState
from src.Naves.NaveUser import NaveUser
from src.Naves.NaveEnemy import NaveEnemy

from src.Config import color_configs as colors
from src.Config import screen_configs

class GameEngine:
    """
    A fundamental class that abstracts the game's components' operation.
    """

    def __init__(self, screen):
        self.shot_limiter = 3
        self.random_limiter = 0
        self.botsshots_limiter = 0

        self.__screen = screen
        self._gameover = False

        # Appropriately initializing the game
        self.__on_init()

        # Setting basic features for the game functioning
        self.__clock = pygame.time.Clock()
        self.__fps = 20
        self.__ended = False

        # Particular elements of the game
        # Modifying area
        self.background = [Background(self.__screen, 0), Background(self.__screen, 1)]
        self.nave = NaveUser(self.__screen, ((1/2)*screen_configs['width'], screen_configs['height']))

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
        6°) Insert random Bot
        7°) Calculates collisions
        8°) Calculates off the screen objects
        """
        self.shot_limiter+=1
        self.random_limiter+=1
        self.botsshots_limiter+=1

        delta_t = self.__clock.tick(self.__fps) / 1000

        # Dispite the fact it may looks like trash, it keeps the image atualizing
        self.__screen.fill(colors['black'])

        for drawable in self._drawables:
            drawable.updates_position(delta_t)

        self.__event_handler()
        
        while self._gameover == True:
            self.__on_game_over

        if self.__ended:
            return

        for drawable in self._drawables:
            drawable.draw()

        pygame.display.flip()

        self.__randomize()

        self.__bots_shooting()
        self.__collisions()
        self.__out_screen()
        

    def __initializing_bots(self, number_bots):
        """
        Instatiates the bots e saves them into the GlobalState
        """
        for i in range(1,number_bots):
            self.state.add_bot(NaveEnemy(self.__screen, (400-100*i, 30), (50, 0)))
        
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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.nave.horizontal_moving(1)
        if keys[pygame.K_a]:
            self.nave.horizontal_moving(-1)
        if keys[pygame.K_s]:
            self.nave.vertical_moving(1)
        if keys[pygame.K_w]:
            self.nave.vertical_moving(-1)
        if keys[pygame.K_SPACE]:
            # Anti-apelation control
            if self.shot_limiter > 3:
                self.state.add_shot(self.nave.shooting())
                self.shot_limiter = 0

    def __randomize(self):
        if self.state.num_random_bots >= 5 or self.random_limiter < 6*self.__fps:
            return

        random_position = random.random() * screen_configs['width'], random.random() * screen_configs['height']

        random_velocity_x_pos = random.randrange(50, 150, 1)
        random_velocity_x_neg = random.randrange(-150, -50, 1)
        random_velocity_y_pos = random.randrange(50, 150, 1)
        random_velocity_y_neg = random.randrange(-150, -50, 1)

        random_velocity = (random.choice([random_velocity_x_pos, random_velocity_x_neg]),
                           random.choice([random_velocity_y_pos, random_velocity_y_neg]))

        bot = NaveEnemy(self.__screen, random_position, random_velocity, 4)
        self.state.add_bot(bot)
        self.state.num_random_bots += 1

        self.random_limiter = 0

    def __bots_shooting(self):
        if self.botsshots_limiter > self.__fps:
            for bot in self.state.bots.sprites():
                if random.random() < 0.2:
                    botshot = bot.shoot_user(self.state.nave.position)
                    self.state.add_botsshots(botshot)
            self.botsshots_limiter = 0
    
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
        Menu(self.__screen)

    def __on_game_over(self):
        self.__screen.display.fill(white)
        self.message_to_screen("Game over, press P to play again or Q to quit", colors['red'])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("pygame.QUIT pressed by user")
                self.__ended = True
                self.__on_quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.__ended = True
                    self.__on_quit()
                if event.key == pygame.K_p:
                    self._gameover = False
                    self.__frame()

    def __on_quit(self):
        """
        Private method for treating specifically of pygame's interrupting.
        """
        print("Quitting pygame in 3 ... 2 ... 1 ...")
        pygame.quit()


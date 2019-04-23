import time
import random 
import math
import pygame

from src.Menu import Menu
from src.Background import Background
from src.GlobalState import GlobalState
from src.Naves.NaveUser import NaveUser
from src.Naves.NaveEnemy import NaveEnemy
from src.GameOver import GameOver

from src.Config import color_configs as colors
from src.Config import screen_configs

class GameEngine:
    """
    A fundamental class that abstracts the game's components' operation.
    """

    def __init__(self, screen):
        self.time = 0
        
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
        

    @property
    def _drawables(self):
        return self.background + [self.nave] + self.state.list_all()

    def game_loop(self):
        """
        A wrapper of the GameEngine's operation
        """
        self.nave = NaveUser(self.__screen, ((1/2)*screen_configs['width'], screen_configs['height']))

        self.state = GlobalState(self.nave, self.__screen, self)

        self.__initializing_bots(5)

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
        self.time += delta_t

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

        self.__print_values()

        pygame.display.flip()

        self.__randomize(self.rate())

        self.__bots_shooting()
        self.__collisions()
        self.__out_screen()
        

    def __initializing_bots(self, number_bots):
        """
        Instatiates the bots e saves them into the GlobalState
        """
        for i in range(1,number_bots):
            self.state.add_bot(NaveEnemy(self.__screen, (400-100*i, 100), (50, 0)))
        
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

    def rate(self):
        return 5 - 4*math.exp(-0.006*self.time)

    def __randomize(self, rate):
        
        lim_min_vel = int(50*rate)
        lim_max_vel = int(150*rate)

        if self.state.num_random_bots >= 5*rate or self.random_limiter < 6*self.__fps:
            return

        random_position = random.random() * screen_configs['width'], random.random() * screen_configs['height']

        random_velocity_x_pos = random.randrange(lim_min_vel, lim_max_vel, 1)
        random_velocity_x_neg = random.randrange(-lim_max_vel, -lim_min_vel, 1)
        random_velocity_y_pos = random.randrange(lim_min_vel, lim_max_vel, 1)
        random_velocity_y_neg = random.randrange(-lim_max_vel, -lim_min_vel, 1)

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

    def on_game_over(self):
        GameOver(self.__screen, self.state.nave.score)
        self.game_loop()

    def __on_quit(self):
        """
        Private method for treating specifically of pygame's interrupting.
        """
        print("Quitting pygame in 3 ... 2 ... 1 ...")
        pygame.quit()

    def __print_values(self):

        image_coin = pygame.image.load("static/Images/coins.png")
        image_coin = pygame.transform.scale(image_coin, (30, 30))
        self.__screen.blit(image_coin, (750-40, 10))

        hearts = int(self.state.nave._life / 10)
        for heart in range(hearts):
            image_heart = pygame.image.load("static/Images/cardiogram.png")
            image_heart = pygame.transform.scale(image_heart, (30, 30))

            self.__screen.blit(image_heart, (30 + heart*30, 10))

        valor = str(self.state.nave.score)
        self.__message_to_screen(valor)


    def __message_to_screen(self, text, color = (226,161,9)):
        textSurf, textRect = self.text_objects(text,color)
        textRect.center = self.__screen.get_width()-80, 30
        self.__screen.blit (textSurf, textRect)

    def text_objects(self, text , color):
            font = pygame.font.SysFont('Arial Black', 40)
            textSurface = font.render(text, True , color)
            return textSurface, textSurface.get_rect()

import pygame
from pubsub import pub 


class GlobalState():

    def __init__(self, nave):
        self.nave = nave
        self.bots = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        self.__subscribe_bots()
        self.__subscribe_shots()

    def __subscribe_bots(self):
        pub.subscribe(lambda bot: self.remove_bot(bot), 'remove_bot')

    def __subscribe_shots(self):
        pub.subscribe(lambda shot: self.remove_shot(shot), 'remove_shot')

    def list_all(self):
        return self.bots.sprites() + self.shots.sprites()

    def add_bot(self, bot):
        self.bots.add(bot)

    def remove_bot(self, bot):
        self.bots.remove(bot)

    def add_shot(self, shot):
        self.shots.add(shot)

    def remove_shot(self, shot):
        self.shots.remove(shot)


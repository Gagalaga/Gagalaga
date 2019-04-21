import pygame
import pubsub


class GlobalState():

    def __init__(self, nave):
        self.nave = nave
        self.bots = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

    def __subscribe_bots(self):
        pubsub.subscribe(lambda bot: self.remove_bot(bot), 'remove_bot')

    def __subscribe_shots(self):
        pubsub.subscribe(lambda shot: self.remove_shot(bot), 'remove_shot')

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


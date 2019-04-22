import pygame


class GlobalState():

    def __init__(self, nave):
        self.nave = nave
        self.bots = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

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

    def handle_collisions(self):
        self.remove_dead_ones()
        self.bots.update()
        self.shots.update()
        bots = pygame.sprite.groupcollide(self.bots, self.shots, False, True, pygame.sprite.collide_mask)
        for bot in bots.keys():
            bot._life = bot._life - 10 

    def handle_out_screen(self):
        for shot in self.shots:
            if shot.out_screen():
                self.remove_shot(shot)

        #for bot in self.bots:
        #    if bot.out_screen():
        #        self.remove_bot(bot)

    def remove_dead_ones(self):
        for bot in self.bots.sprites():
            if bot.should_be_dead():
                self.remove_bot(bot)

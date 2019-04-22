import pygame


class GlobalState():

    def __init__(self, nave):
        self.nave = nave
        self.bots = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.botsshots = pygame.sprite.Group()

    def list_all(self):
        return self.bots.sprites() + self.shots.sprites() + self.botsshots.sprites()

    def add_bot(self, bot):
        self.bots.add(bot)

    def remove_bot(self, bot):
        self.bots.remove(bot)

    def add_botsshots(self, botshot):
        self.botsshots.add(botshot) 

    def remove_botsshots(self, botshot):
        self.botsshots.remove(botshot)

    def add_shot(self, shot):
        self.shots.add(shot)

    def remove_shot(self, shot):
        self.shots.remove(shot)

    def handle_collisions(self):
        self.bots.update()
        self.shots.update()
        self.nave.update()
        self.botsshots.update()
        pygame.sprite.groupcollide(self.bots, self.shots, True, True, pygame.sprite.collide_mask)

        botshot = pygame.sprite.spritecollideany(self.nave, self.botsshots, pygame.sprite.collide_mask)
        if botshot != None:
            print("Puta Que Pariu! Vc ganhou esse bloody jogo")

    @property
    def all_shots(self):
        return self.shots.sprites() + self.botsshots.sprites()

    def handle_out_screen(self):
        for shot in self.all_shots:
            if shot.out_screen():
                self.remove_shot(shot)

        #for bot in self.bots:
        #    if bot.out_screen():
        #        self.remove_bot(bot)

        #print(len(self.shots.sprites()))

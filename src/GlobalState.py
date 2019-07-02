from abc import ABC, abstractclassmethod

import pygame

from src.bonus import Bonus

class GlobalStateAbstract(ABC):
    @abstractclassmethod
    def add_bot(self, bot):
        raise NotImplementedError

    @abstractclassmethod
    def remove_bot(self, bot):
        raise NotImplementedError

    @abstractclassmethod
    def add_botsshot(self, botsshot):
        raise NotImplementedError

    @abstractclassmethod
    def remove_botsshot(self, botsshot):
        raise NotImplementedError

    @abstractclassmethod
    def add_shot(self, shot):
        raise NotImplementedError

    @abstractclassmethod
    def remove_shot(self, shot):
        raise NotImplementedError


class GlobalState():
    instance = None
    def __init__(self, nave, screen, game_engine):
        if not GlobalState.instance:
            GlobalState.instance = GlobalState.__GlobalState(nave, screen, game_engine)

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    @classmethod
    def getInstance(cls):
        return cls.instance

    class __GlobalState(GlobalStateAbstract):        
        def __init__(self, nave, screen, game_engine):
            self.nave = nave
            self.bots = pygame.sprite.Group()
            self.shots = pygame.sprite.Group()
            self.botsshots = pygame.sprite.Group()
            self.bonus = pygame.sprite.Group()
            self.screen = screen

            self.game_engine_reference = game_engine

            self.num_random_bots = 0

        def list_all(self):
            return self.bots.sprites() + self.shots.sprites() + self.botsshots.sprites() + self.bonus.sprites()

        def add_bot(self, bot):
            self.bots.add(bot)

        def remove_bot(self, bot):
            self.bots.remove(bot)

        def add_botsshot(self, botshot):
            self.botsshots.add(botshot) 

        def remove_botsshot(self, botshot):
            self.botsshots.remove(botshot)

        def add_shot(self, shot):
            self.shots.add(shot)

        def remove_shot(self, shot):
            self.shots.remove(shot)

        def handle_collisions(self):
            self.remove_dead_ones()
            self.bots.update()
            self.shots.update()
            self.nave.update()
            self.botsshots.update()
            self.bonus.update()

            bots = pygame.sprite.groupcollide(self.bots, self.shots, False, True, pygame.sprite.collide_mask)
            for bot in bots.keys():
                bot._life = bot._life - 10
                self.nave.score += 5

            botshot = pygame.sprite.spritecollideany(self.nave, self.botsshots, pygame.sprite.collide_mask)
            if botshot != None:
                self.remove_botsshot(botshot)
                if self.nave._life == 10:
                    self.game_engine_reference.on_game_over()
                else:
        
                    self.nave._life -= 10

            bot = pygame.sprite.spritecollideany(self.nave, self.bots, pygame.sprite.collide_mask)
            if bot != None:
                self.remove_bot(bot)
                if self.nave._life == 10:
                    self.game_engine_reference.on_game_over()
                else:
                    self.nave._life -= 10

            bonus_collided = pygame.sprite.spritecollideany(self.nave, self.bonus, pygame.sprite.collide_mask)
            if bonus_collided != None:
                if self.nave._life <= 40:
                    self.nave._life += 10
                self.bonus.remove(bonus_collided)


        @property
        def all_shots(self):
            return self.shots.sprites() + self.botsshots.sprites()

        def handle_out_screen(self):
            for shot in self.all_shots:
                if shot.out_screen():
                    self.remove_shot(shot)

        def remove_dead_ones(self):
            for bot in self.bots.sprites():
                if bot.should_be_dead():
                    self.nave.score += 10
                    self.nave.killed_bots += 1
                    if self.nave.killed_bots > 5:
                        self.bonus.add(Bonus(self.screen, bot.position, "static/Images/Degrees/L.png"))
                        self.nave.killed_bots = 0
                    self.remove_bot(bot)
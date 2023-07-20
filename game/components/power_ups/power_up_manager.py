import pygame

from random import randint
from game.components.power_ups.shield import Shield

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appers = randint(5000, 10000)
        self.duration = randint(3, 5)

    def generate_power_up(self):
        power_up = Shield()
        self.when_appers += randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appers:
            self.generate_power_up()

    def draw(self, screen):
        for power_up in self,power_up()

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appers = randint(now + 5000, now + 10000)
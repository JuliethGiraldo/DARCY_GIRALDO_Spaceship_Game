from game.components.enemies.enemy import Enemy
from game.components.enemies.sapphire import Sapphire

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)
        for sapphire in self.enemies:
            sapphire.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for sapphire in self.enemies:
            sapphire.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)
        if len(self.enemies) < 2:
            sapphire = Sapphire()
            self.enemies.append(sapphire)
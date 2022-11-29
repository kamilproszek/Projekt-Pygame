import random
import Game_Module as gm
import pygame
import player as p

enemy_group = pygame.sprite.Group()


def create_enemy(y):
    enemy = Enemy(y)
    enemy_group.add(enemy)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.kula
        self.rect = self.image.get_rect()
        self.direction = random.choice([-1, 1])
        self._count = 0

        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = gm.SCREEN_WIDTH
        self.rect.y = y

    def update(self, x):

        if self.direction == 1:
            self._animate(gm.saw_r)
        else:
            self._animate(gm.saw_l)

        self.rect.x += self.direction * 8
        # sprawdzanie czy jest ponizej ekranu
        if self.rect.right < 0 or self.rect.left > gm.SCREEN_WIDTH or self.rect.bottom > gm.SCREEN_HEIGHT:
            self.kill()
            create_enemy(x)

    def move(self, x):
        self.rect.y += x

    def _animate(self, image_list):
        self.image = image_list[self._count]
        self._count += 1
        self._count %= 3

import enemy
import platform as p
import random
import Game_Module as gm
import pygame

# twozrenie instancji platformy (grupa)
lvl1_group = pygame.sprite.Group()


class lvl1(p.Platform):
    def __init__(self, x, y, width, moving):
        super().__init__(x, y, width, gm.platform_1)
        self.moving = moving

    def get_move(self):
        return self.moving

def create_platforms():
    p_moving = False
    # p_w = random.randint(100, 150)
    p_w = gm.SCREEN_WIDTH

    platform = lvl1(0, 680, p_w, p_moving)
    lvl1_group.add(platform)

    for p in range(50):
        # 40-60 px
        p_w = random.randint(100, 150)
        p_x = random.randint(0, gm.SCREEN_WIDTH - p_w)
        p_y = platform.rect.y - random.randint(120, 180)

        platform = lvl1(p_x, p_y, p_w, p_moving)
        lvl1_group.add(platform)

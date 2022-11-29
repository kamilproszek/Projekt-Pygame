import pygame.sprite


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (width, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.moving=moving
        # self.move_counter=random.randint(0,50)
        # self.direction=random.choice([-1,1])

    def get_move(self):
        return self.moving

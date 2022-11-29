import Game_Module as gm
import enemy
import lvl1
import pygame
from pygame import mixer

mixer.init()


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(gm.player_stand_r, (130, 134))
        # self.image=gm.player_stand_r
        # rysujemy prostokat, ktory ma takie rozmiary jak nasz obrazek, funkcja get rect pobiera nam rozmiary naszego gracza
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rotate_left = False
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.width = self.image.get_width() - 80
        self.height = self.image.get_height()
        # aktualne polozenie
        # przyciaganie z jaka dziala, moze byc zwiekszone
        self.on_ground = True
        self.jumping = False
        self.vel_y = 0
        # skok
        self.gravity = 1
        # update musk
        self.mask = pygame.mask.from_surface(self.image)
        self.score = 0
        self.go_down_enemy = False

    def get_score(self):
        return self.score

    def reset_score(self, x):
        self.score = x

    def move(self):
        self.movement_x = 0
        self.movement_y = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.movement_x -= 10
            self.rotate_left = True
            self._animate(gm.PLAYER_WALK_LIST_L)
        if key[pygame.K_RIGHT]:
            self.movement_x = 10
            self.rotate_left = False
            self._animate(gm.PLAYER_WALK_LIST_R)
        if key[pygame.K_SPACE]:
            self.jumping = True
            self.jump()

    def update(self):
        # sprawdzanie czy wyjde poza krawedzie
        self._gravitation()
        self.scroll = 0

        # kolizje ze sciankami
        if self.rect.left + self.movement_x < -20:
            self.movement_x = 0
            self.image = gm.player_stand_l
        if self.rect.right + self.movement_x > gm.SCREEN_WIDTH + 50:
            self.movement_x = 0
            self.image = gm.player_stand_r

        if self.movement_x == 0:
            if self.rotate_left:
                self.image = gm.player_stand_l
            else:
                self.image = gm.player_stand_r

        # sprawdzanie kolizji z ziemia
        if self.rect.bottom + self.movement_y > gm.SCREEN_HEIGHT - 0.05:
            pass

        # sprawdz czy gracz jest na wysokosci linii
        if self.rect.top <= 350:
            if self.movement_y < 0:
                # self.rect.bottom+=40
                for i in lvl1.lvl1_group:
                    i.rect.bottom += 12
                    self.score += 0.01
                    # enemy.enemy_group.

                if i.rect.top > gm.SCREEN_HEIGHT:
                    i.kill()

        self.go_down_enemy = False
        # sprawdzanie kolizji z platfromami
        for p in lvl1.lvl1_group:
            if p.rect.colliderect(self.rect.x, self.rect.y + self.movement_y, self.width, self.height):
                if self.rect.bottom < p.rect.centery:
                    self.rect.bottom = p.rect.top + 4
                    self.movement_y = 0
                    self.vel_y = 0
                    self.on_ground = True
                    self.jumping = False

        if self.rect.top > gm.SCREEN_HEIGHT - 1:
            self.all_height = 600

        # aktualizacja pozycji postaci
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

    def get_g_d(self):
        return self.go_down_enemy

    def _gravitation(self):
        self.vel_y += self.gravity
        self.movement_y += self.vel_y

    def jump(self):

        if self.on_ground:
            self.jumping = True
            self.vel_y = -20
            self.on_ground = False
            gm.jump_fx.play()

        if self.rotate_left:
            self.image = gm.player_jump_l
        else:
            self.image = gm.player_jump_r

    def _animate(self, image_list):
        self.image = image_list[self._count]
        self._count += 1
        self._count %= 15

    def draw(self):
        # .rect wspolrzedne tam gdzie obrazek to tam ma sie rysowac
        gm.screen.blit(self.image, self.rect)
        # pomoc w rysowaniu obramowania gracza
        # pygame.draw.rect(gm.screen,gm.DARKGREEN,self.rect,2)

# def sum_score():
#     score+=5

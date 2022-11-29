import random
import pygame, os, menu
import enemy
import player as p
import lvl1
import Game_Module as gm
from enemy import Enemy

pygame.init()
clock = pygame.time.Clock()
FPS = 60
# score=0
fade_counter = 0

pygame.mixer.music.play(-1, 0.0)

# CREATE SCREEN
screen = pygame.display.set_mode((gm.SCREEN_WIDTH, gm.SCREEN_HEIGHT))

# nazwa okienka
pygame.display.set_caption('jumpy')

game_over = True
mozna_obinzac = True

# tworzenie instancji gracza
# szerokosc przez pol a wysokosc naszego gracza -150 od wysokosci okienka
jumpy = p.Player(gm.SCREEN_WIDTH // 2, gm.SCREEN_HEIGHT - 150)

lvl1.create_platforms()

enemy.create_enemy(50)

# petla gry
run = True
while run:
    clock.tick(FPS)

    score = jumpy.get_score()

    if game_over == False:

        jumpy.move()
        screen.blit(gm.bg_image_1, (0, 0))

        # # prog przewijania ekranu
        # pygame.draw.line(screen, gm.DARKGREEN, (0, 350), (gm.SCREEN_WIDTH, 350))

        # rysowanie platform
        lvl1.lvl1_group.draw(screen)
        enemy.enemy_group.draw(screen)

        # rysowanie gracza
        jumpy.draw()

        menu.draw_text(str(int(score)) + " m", gm.font, gm.WHITE, 520, 40)

        # check game over
        if jumpy.rect.centery > gm.SCREEN_HEIGHT:
            gm.game_over.play()
            game_over = True

        if pygame.sprite.spritecollide(jumpy, enemy.enemy_group, False):
            if pygame.sprite.spritecollide(jumpy, enemy.enemy_group, False, pygame.sprite.collide_mask):
                gm.game_over.play()
                game_over = True

    else:

        if fade_counter < gm.SCREEN_WIDTH:
            fade_counter += 10
            pygame.draw.rect(gm.screen, gm.BLACK, (0, 0, fade_counter, gm.SCREEN_HEIGHT))

        menu.display_option()
        menu.draw_text(str(int(score)) + " m", gm.font, gm.WHITE, 320, 240)
        key = pygame.key.get_pressed()

        if key[pygame.K_e]:
            fade_counter = 0
            lvl1.lvl1_group.empty()
            lvl1.create_platforms()
            # enemy.enemy_group.empty()
            # enemy.create_enemy()
            # enemy.enemy_group.update()
            game_over = False
            jumpy.rect.center = gm.SCREEN_WIDTH // 2, gm.SCREEN_HEIGHT - 250
            score = 0
            jumpy.reset_score(0)

        if key[pygame.K_q]:
            run = False

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # aktualizacja okna
    pygame.display.update()

    random_number = random.randint(50, gm.SCREEN_HEIGHT - 300)
    enemy.enemy_group.update(random_number)

    # aktualizowanie gracza
    jumpy.update()

pygame.quit()

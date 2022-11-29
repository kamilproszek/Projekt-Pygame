import pygame, os
from pygame import mixer

mixer.init()
pygame.font.init()

# screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

# CREATE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# nazwa okienka
pygame.display.set_caption('jumpy')

# sound eff
jump_fx = pygame.mixer.Sound('music/jump.mp3')
jump_fx.set_volume(0.5)

game_over = pygame.mixer.Sound('music/game_over.wav')
game_over.set_volume(0.5)

background_track = pygame.mixer.music.load('music/background_sound.mp3')
pygame.mixer.music.set_volume(0.1)

# colors
DARKGREEN = pygame.color.THECOLORS['darkgreen']
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font
font = pygame.font.SysFont("Helvetica", 20)
# Comic Sans MS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# grafika  - wczytywanie grafik
path = os.path.join('images')
file_names = sorted(os.listdir(path))

bg_image_1 = pygame.image.load(os.path.join(path, 'background_1.png')).convert()
# bg_image_2 = pygame.image.load(os.path.join(path, 'background_2.png')).convert()

play = pygame.image.load(os.path.join(path, 'play.png')).convert_alpha()
exit = pygame.image.load(os.path.join(path, 'close.png')).convert_alpha()
score_image = pygame.image.load(os.path.join(path, 'score.png')).convert_alpha()

# enemies
kula = pygame.image.load(os.path.join(path, 'kula.png')).convert_alpha()

for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(bg_image_1)

PLAYER_WALK_LIST_R = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15]
PLAYER_WALK_LIST_L = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15]

saw_l = [ON1, ON2, ON3]
saw_r = [ON1_R, ON2_R, ON3_R]


player_stand_r = pygame.image.load(os.path.join(path, 'stand_r.png')).convert_alpha()
player_stand_l = pygame.image.load(os.path.join(path, 'stand_l.png')).convert_alpha()

player_jump_r = pygame.image.load(os.path.join(path, 'jump_r.png')).convert_alpha()
player_jump_l = pygame.image.load(os.path.join(path, 'jump_l.png')).convert_alpha()

platform_1 = pygame.image.load(os.path.join(path, 'Brown off.png')).convert_alpha()



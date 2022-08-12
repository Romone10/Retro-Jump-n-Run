import pygame
import math
import random
from random import shuffle


pygame.init()

# colors:
white = (255, 255, 255)
pink = (238, 130, 238)
green = (0, 255, 0)
orange = (255, 140, 0)

# Create GUI:
SCREEN_WIDTH = 1192
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Jump'n'Run")
bg = pygame.image.load("C:/Users/Moreno/PycharmProjects/Retro Jump n Run/Pictures/background.png").convert()
bg_width = bg.get_width()

# game variables:
score = 0
player_x = 350
player_y = 389
y_change = 0
gravity = 1
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
obstacles = [1350, 1750, 2150]
obstacle_speed = 10
active = False

# game loop
running = True
while running:

    timer.tick(fps)

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    if not active:
        instruction_text = font.render(f'Press space bar to start and jump!', True, white)
        screen.blit(instruction_text, (250, 515))

    score_text = font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (100, 515))
    player = pygame.draw.rect(screen, pink, [player_x, player_y, 40, 40])

    # define obstacles:
    obstacle0 = pygame.draw.rect(screen, white, [obstacles[0], 359, 40, 70])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 339, 40, 90])
    obstacle2 = pygame.draw.rect(screen, green, [obstacles[2], 379, 40, 50])

    # scroll background
    scroll -= 2

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # obstacles loop
    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(1250, 1350)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) \
                    or player.colliderect(obstacle2):
                active = False

    # event handler:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles = [1350, 1750, 2150]
                shuffle(obstacles)
                player_x = 350
                score = 0
                active = True

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18

    if y_change > 0 or player_y < 389:
        player_y -= y_change
        y_change -= gravity
    if player_y > 389:
        player_y = 389
    if player_y == 389 and y_change < 0:
        y_change = 0

    pygame.display.flip()

pygame.quit()

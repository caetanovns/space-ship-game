import math
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True

pygame.display.set_caption("Exemplo jogo 1")

player = pygame.image.load("res/images/space-ship.png")
enemy = pygame.image.load("res/images/ghost.png")

clock = pygame.time.Clock()

player_x = 370
player_y = 480

enemy_x = 370
enemy_y = 240

player_move_x = 0
player_move_y = 0

def blit_player(x, y):
    screen.blit(player, (x, y))

def blit_enemy(x, y):
    screen.blit(enemy, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_move_x = -5

            if event.key == pygame.K_d:
                player_move_x = 5

            if event.key == pygame.K_w:
                player_move_y = -5
                
            if event.key == pygame.K_s:
                player_move_y = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_move_x = 0
            
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_move_y = 0


    screen.fill((15,19,56))

    player_x += player_move_x
    player_y += player_move_y
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    
    if player_y <= 0:
        player_y = 0
    elif player_y >= 536:
        player_y = 536


    blit_enemy(enemy_x, enemy_y)
    blit_player(player_x, player_y)

    pygame.display.update()

    
    clock.tick(60)

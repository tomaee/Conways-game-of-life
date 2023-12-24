

import pygame

from copy import deepcopy
from random import randint






RES = WIDTH, HEIGHT = 1600, 900
FPS = 10

TILE = 10

W, H = WIDTH // TILE, HEIGHT // TILE

print(W, H)



#initializing pygame

pygame.init()
pygame.mixer.init()

select_sound = pygame.mixer.Sound("sounds/stop-13692.mp3")
select_sound.set_volume(0.2)
unselect_sound = pygame.mixer.Sound("sounds/pick-92276.mp3")
unselect_sound.set_volume(0.2)
pygame.mixer.music.load("sounds/Tartini Violin Sonata in G minor ''Devil's Trill Sonata'' (320 kbps).mp3")
pygame.mixer.music.set_volume(0.3) 
pygame.mixer.music.play() 



surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
start_game = False

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[0 for i in range(W)] for j in range(H)]
start_field = [[0 for i in range(W)] for j in range(H)]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0
    




while True:
    surface.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # Left click
                print('Left mouse button pressed!')
                posx, posy = pygame.mouse.get_pos()
                print(f'Mouse clicked at {posx//TILE}, {posy//TILE}')
                current_field[(posy//TILE)][(posx//TILE)] = 1
                pygame.mixer.Sound.play(select_sound)
                

            elif pygame.mouse.get_pressed()[2]: # Right click
                print('Right mouse button pressed!')
                posx, posy = pygame.mouse.get_pos()
                print(f'Mouse clicked at {posx//TILE}, {posy//TILE}')
                current_field[(posy//TILE)][(posx//TILE)] = 0
                pygame.mixer.Sound.play(unselect_sound)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game = not start_game
    
    #gird
    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    if not start_game:
        for x in range(1, W - 1):
                for y in range(1, H - 1):
                    if current_field[y][x]:
                        pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + 2, y * TILE + 2, TILE -2, TILE - 2))
                

    if start_game:
        #life or death
        
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('black'), (x * TILE + 2, y * TILE + 2, TILE -2, TILE - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(FPS)

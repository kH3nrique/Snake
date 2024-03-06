import random
import pygame
from pygame.locals import *

#same pixel both snake and apple
def on_grid_random():
    x = random.randint(0,500)
    y = random.randint(0,500)
    return (x//10 * 10, y//10 * 10)

def game_over_screen():
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('SE FODEU', True, (225, 225, 225))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (500/2, 10)

    play_again_font = pygame.font.Font('freesansbold.ttf', 32)
    play_again_screen = play_again_font.render('Jogar novamente', True, (225, 225, 225))
    play_again_rect = play_again_screen.get_rect()
    play_again_rect.midtop = (500/2, 300)

    screen.blit(game_over_screen, game_over_rect)
    screen.blit(play_again_screen, play_again_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if play_again_rect.collidepoint(event.pos):
                    return True

#eat the apple
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake')

#snake
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((225, 0, 0))

my_direction = LEFT

#speed snake
clock = pygame.time.Clock()

#score
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    #speed snake
    clock.tick(9)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_w and my_direction != DOWN:
                my_direction = UP
            if event.key == K_s and my_direction != UP:
                my_direction = DOWN
            if event.key == K_a and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_d and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    #collision wich boundaries
    if snake[0][0] == 500 or snake[0][1] == 500 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True

    #if you hit yourself
    if snake[0] in snake[1:]:
        game_over = True

    if game_over:
        if game_over_screen():
            # Reinicia o jogo
            snake = [(200, 200), (210, 200), (220, 200)]
            my_direction = LEFT
            apple_pos = on_grid_random()
            score = 0
            game_over = False
        else:
            break

    snake.pop()

    # Actually make the snake move.
    if my_direction == UP:
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    if my_direction == DOWN:
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    if my_direction == RIGHT:
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))
    if my_direction == LEFT:
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    #add grid
    for x in range(0,500,10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 500))
    for y in range(0,500,10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (500, y))

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (500 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

    while game_over:
        game_over_font = pygame.font.Font('freesansbold.ttf', 75)
        game_over_screen = game_over_font.render('SE FODEU', True, (225, 225, 225))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (500/2, 10)
        screen.blit(game_over_screen, game_over_rect)
        pygame.display.update()
        pygame.time.wait(500)

            
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
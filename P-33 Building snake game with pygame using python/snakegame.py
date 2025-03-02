import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Define colors
red = (255, 0, 0)
blue = (51, 15, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

# Display settings
win_width = 600
win_height = 400

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Function to display the score
def user_score(score):
    number = score_font.render(f"Score: {score}", True, red)
    window.blit(number, [10, 10])

# Function to draw the snake
def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])

# Function to display messages
def message(msg):
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])

# Main game loop
def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not gameOver:
        while gameClose:
            window.fill(grey)
            message("You lost! Press P to Play Again or Q to Quit.")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False  # Fix: Allow quitting properly
                    if event.key == pygame.K_p:  # Fix: Restart game on 'P'
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT and x1_change == 0:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == K_RIGHT and x1_change == 0:
                    x1_change = snake
                    y1_change = 0
                elif event.key == K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = snake

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True  # Fix: Don't set gameOver immediately

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)

        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])

        snake_size = [x1, y1]
        snake_length_list.append(snake_size)

        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)  # Fix: Control game speed

    pygame.quit()
    quit()

game_loop()

# fonts = pygame.font.get_fonts()
# print(fonts)


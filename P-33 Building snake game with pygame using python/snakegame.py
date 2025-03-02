import pygame
from pygame.locals import *
import time 
import random

pygame.init()

#obtain colors
red = (255,0,0)
blue = (51,15,255)
grey = (192,192,192)
green = (51,102,0)

#display define
win_width = 600
win_height = 400

window = pygame.display.set_mode((win_width,win_height))
pygame.diaply.set_caption("Snake Game")
time.sleep(2)

snake = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont("comicsansms",30)

def user_score(score):
    number = score_font.render("Score :" ,score,True,red)
    window.blit(number,[0,0])

def game_snake():
    pass

def message(msg):
    msg = font_style.render(msg,True,red)
    window.blit(msg,[win_width/6,win_height/3])

def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width/2
    y1 = win_height/2

    x1_change =0
    y1_change =0

    snake_length_list =[]
    snake_length = 1

    foodx = round(random.randrange(0,win_width - snake)/10.0) * 10.0
    foody = round(random.randrange(0,win_height-snake)/10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            window.fill(grey)
            message("You lost !! Press P to play the game again and Q  to quit the game")
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = True
                    if event.key == pygame.K_q:
                        game_loop()

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):

# fonts = pygame.font.get_fonts()
# print(fonts)


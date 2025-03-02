import pygame
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


# fonts = pygame.font.get_fonts()
# print(fonts)


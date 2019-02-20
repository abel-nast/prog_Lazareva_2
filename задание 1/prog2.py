import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,360),0,32)
bgColor = (0, 0, 0)
pygame.display.set_caption("Prog2")


mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.fill(bgColor)
    pygame.display.update()


pygame.quit()

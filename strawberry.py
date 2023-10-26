import pygame
from pygame.math import Vector2

import config

import random as r

class Strawberry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = r.randint(0,config.CELL_NUMBER - 1)
        self.y = r.randint(0,config.CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        self.image = pygame.image.load("images/strawberry.png")

    def drawStrawberry(self): 
        strawberryRect = pygame.Rect(int(self.pos.x * config.CELL_SIZE),int(self.pos.y * config.CELL_SIZE), config.CELL_SIZE, config.CELL_SIZE)
        config.screen.blit(self.image, strawberryRect)
import pygame
from pygame.math import Vector2

import config

import random as r

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((config.CELL_NUMBER * config.CELL_SIZE, config.CELL_NUMBER * config.CELL_SIZE))
        self.x = r.randint(0,config.CELL_NUMBER - 1)
        self.y = r.randint(0,config.CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        self.image = pygame.image.load("images/strawberry.png")

    def drawFruit(self): 
        fruitRect = pygame.Rect(int(self.pos.x * config.CELL_SIZE),int(self.pos.y * config.CELL_SIZE), config.CELL_SIZE, config.CELL_SIZE)
        self.screen.blit(self.image, fruitRect)
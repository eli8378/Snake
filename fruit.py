import pygame
from pygame.math import Vector2

import config

import random as r

class Fruit:
    def __init__(self):
        config.cellSize = 40
        config.cellNumber = 20
        self.x = r.randint(0,config.cellNumber - 1)
        self.y = r.randint(0,config.cellNumber - 1)
        self.pos = Vector2(self.x, self.y)

    def drawFruit(self): 
        fruitRect = pygame.Rect(int(self.pos.x * config.cellSize),int(self.pos.y * config.cellSize), config.cellSize, config.cellSize)
        pygame.draw.rect(config.screen, (126,166,114), fruitRect)
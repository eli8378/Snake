import pygame
from pygame.math import Vector2

import random as r

class Fruit:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.x = r.randint(0,self.cellNumber - 1)
        self.y = r.randint(0,self.cellNumber - 1)
        self.pos = Vector2(self.x, self.y)

    def drawFruit(self): 
        fruitRect = pygame.Rect(int(self.pos.x * self.cellSize),int(self.pos.y * self.cellSize), self.cellSize, self.cellSize)
        pygame.draw.rect(self.screen, (240,166,114), fruitRect)
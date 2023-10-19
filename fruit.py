import pygame
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.cellSize = 40
        self.cellNumber = 20
        self.pos = Vector2(self.x, self.y)
        #create an x and y position
        #draw a square

    def drawFruit(self): 
        fruitRect = pygame.Rect(self.pos.x,self.pos.y, self.cellSize, self.cellSize)
        pygame.draw.rect(self.screen, (126,166,114), fruitRect)
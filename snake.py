import pygame
from pygame.math import Vector2
import config



class Snake:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(-1,0)

    def drawSnake(self):
        for block in self.body:
            self.xpos = int(block.x * self.cellSize)
            self.ypos = int(block.y * self.cellSize)
            blockRect = pygame.Rect(self.xpos, self.ypos, self.cellSize, self.cellSize)
            pygame.draw.rect(config.screen, (183,191,122), blockRect)

    def moveSnake(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]
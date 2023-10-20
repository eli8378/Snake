import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.moveInterval = 0.1
        self.moveTimer = 0

    def update(self):
        if self.moveTimer >= self.moveInterval:
            self.moveTimer -= self.moveInterval
            self.moveSnake()

    def drawSnake(self):
        for block in self.body:
            self.xpos = int(block.x * self.cellSize)
            self.ypos = int(block.y * self.cellSize)
            blockRect = pygame.Rect(self.xpos, self.ypos, self.cellSize, self.cellSize)
            pygame.draw.rect(self.screen, (183,191,230), blockRect)

    def moveSnake(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]

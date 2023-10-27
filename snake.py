import pygame
from pygame.math import Vector2

import config


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = [Vector2(10,10), Vector2(11,10), Vector2(12,10)]
        self.direction = Vector2(-1,0)
        self.moveInterval = 1.0
        self.moveTimer = 0
        self.snakeBody = pygame.image.load("images/snakeBody.png")
        self.snakeHead = pygame.image.load("images/snakeHead.png")

    def update(self):
        self.moveTimer += pygame.time.get_ticks() / (self.moveInterval * 1000)
        if self.moveTimer >= self.moveInterval:
            self.moveTimer -= self.moveInterval
            self.moveSnake()

    def drawSnake(self):
        for index,block in enumerate(self.body):
            self.xpos = int(block.x * config.CELL_SIZE)
            self.ypos = int(block.y * config.CELL_SIZE)
            blockRect = pygame.Rect(self.xpos, self.ypos, config.CELL_SIZE, config.CELL_SIZE)
            config.screen.blit(self.snakeBody, blockRect)
            if index == 0:
                config.screen.blit(self.snakeHead, blockRect)
            else:
                config.screen.blit(self.snakeBody, blockRect)
    

            

    def moveSnake(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]

    def snakeLogic(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.direction.y != 1:
                    self.direction = Vector2(0,-1)
            if event.key == pygame.K_s:
                if self.direction.y != -1:
                    self.direction = Vector2(0,1)
            if event.key == pygame.K_a:
                if self.direction.x != 1:
                    self.direction = Vector2(-1,0)
            if event.key == pygame.K_d:
                if self.direction.x != -1:
                    self.direction = Vector2(1,0)

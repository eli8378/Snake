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

    #Prevents snake from accelerating while moving and also moves it
    def update(self):
        self.moveTimer += pygame.time.get_ticks() / (self.moveInterval * 1000)
        if self.moveTimer >= self.moveInterval:
            self.moveTimer -= self.moveInterval
            self.moveSnake()

    #Draws the snake
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

    #Defines movement for snake using arrow keys
    def snakeMovement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.direction.y != 1:
                    self.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if self.direction.y != -1:
                    self.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if self.direction.x != 1:
                    self.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if self.direction.x != -1:
                    self.direction = Vector2(1,0)

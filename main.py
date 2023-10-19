import pygame
from pygame.math import Vector2

import random as r

import sys

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(-1,0)

    def drawSnake(self):
        for block in self.body:
            self.xpos = int(block.x * cellSize)
            self.ypos = int(block.y * cellSize)
            blockRect = pygame.Rect(self.xpos, self.ypos, cellSize, cellSize)
            pygame.draw.rect(screen, (183,191,122), blockRect)

    def moveSnake(self):
        bodyCopy = self.body[:-1]
        bodyCopy.insert(0, bodyCopy[0] + self.direction)
        self.body = bodyCopy[:]


class Fruit:
    def __init__(self):
        self.x = r.randint(0,cellNumber - 1)
        self.y = r.randint(0,cellNumber - 1)
        self.pos = Vector2(self.x, self.y)

    def drawFruit(self): 
        fruitRect = pygame.Rect(int(self.pos.x * cellSize),int(self.pos.y * cellSize), cellSize, cellSize)
        pygame.draw.rect(screen, (126,166,114), fruitRect)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFailure()

    def drawElements(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)

    def checkFailure(self):
        if not 0 <= self.snake.body[0].x < cellNumber:
            pygame.quit()
        elif not 0 <= self.snake.body[0].y < cellNumber:
            pygame.quit() 
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                pygame.quit()


pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
game = Game()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0,1)
            elif event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1,0)
                
    screen.fill((175,215,70))
    game.drawElements()
    pygame.display.update()
    clock.tick(60)
pygame.quit()

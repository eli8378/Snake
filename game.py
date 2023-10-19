from fruit import Fruit
from snake import Snake
import config

import pygame


class Game:
    def __init__(self):
        config.cellSize = 40
        config.cellNumber = 20
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
        if not 0 <= self.snake.body[0].x < config.cellNumber:
            pygame.quit()
        elif not 0 <= self.snake.body[0].y < config.cellNumber:
            pygame.quit() 
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                pygame.quit()
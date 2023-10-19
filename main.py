import pygame
from pygame.math import Vector2

import random as r

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

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

pygame.init()
cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

def main():
    keys = pygame.key.get_pressed()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SCREEN_UPDATE:
                snake.moveSnake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = Vector2(0,-1)
                elif event.key == pygame.K_DOWN:
                    snake.direction = Vector2(0,1)
                elif event.key == pygame.K_LEFT:
                    snake.direction = Vector2(-1,0)
                elif event.key == pygame.K_RIGHT:
                    snake.direction = Vector2(1,0)



        screen.fill((175,215,70))
        fruit.drawFruit()
        snake.drawSnake()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
main()

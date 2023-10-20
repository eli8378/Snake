import pygame
from pygame.math import Vector2

import sys

from game import Game

pygame.init()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
game = Game()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
cellSize = 40
cellNumber = 20
gameActive = True
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))

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
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1,0)
        if event.type == pygame.MOUSEBUTTONUP:


    if gameActive:
        screen.fill((175,215,70))
        game.drawElements()
        pygame.display.update()
    if game.checkFailure() == "failed":
            gameActive = False
            game.gameOverScreen()
    clock.tick(60)

pygame.quit()
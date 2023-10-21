import pygame
from pygame.math import Vector2

import sys

from game import Game
from start import Start
from end import End

pygame.init()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
game = Game()
start = Start()
end = End()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
cellSize = 40
cellNumber = 20
startMenu = True
isPlaying = False
gameOver = False
screen = pygame.display.set_mode((cellNumber * cellSize, cellNumber * cellSize))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            if isPlaying:
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

    if startMenu:
        start.startMenu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            startMenu = False
            isPlaying = True
    if isPlaying:

        screen.fill((175,215,70))
        game.drawElements()
        if game.checkFailure() == "failed":
            gameOver = True
            isPlaying = False
    if gameOver:
        end.gameOverScreen()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
import pygame

import sys

from game import Game
from start import Start
from end import End
import config


pygame.init()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
game = Game()
start = Start()
end = End()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
startMenu = True
isPlaying = False
pausedState = False
gameOver = False
screen = pygame.display.set_mode((config.CELL_NUMBER * config.CELL_SIZE, config.CELL_NUMBER * config.CELL_SIZE))

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            if isPlaying:
                game.update()
        end.endMenu(event)
        end.quitLogic(event)
        end.tryAgainLogic(event)
        start.startLogic(event)
        start.quitLogic(event)
        game.snake.snakeLogic(event)
        
    if startMenu:
        start.startMenu()
        if start.startButtonState is True:
            startMenu = False
            isPlaying = True
        if start.quitButtonState is True:
            running = False
    if isPlaying:
        game.drawElements()
        if game.checkFailure() == "failed":
            gameOver = True
            isPlaying = False
    if gameOver:
        score = game.endGame()
        end.endMenu(score)
        if end.quitState is True:
            running = False
        if end.tryAgainState is True:
            gameOver = False
            isPlaying = True
            game = Game()
            end = End()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
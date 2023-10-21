import pygame

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
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            if isPlaying:
                game.update()
        start.startLogic(event)
        start.quitLogic(event)
        end.quitLogic(event)
        end.tryAgainLogic(event)
        game.snake.snakeLogic(event)

    if startMenu:
        start.startMenu()
        if start.startButtonState == True:
            startMenu = False
            isPlaying = True
        if start.quitButtonState == True:
            running = False
    if isPlaying:
        screen.fill((175,215,70))
        game.drawElements()
        if game.checkFailure() == "failed":
            gameOver = True
            isPlaying = False
    if gameOver:   
        end.endMenu()
        if end.quitState == True:
            running = False
        if end.tryAgainState == True:
            gameOver = False
            isPlaying = True
            game = Game()
            end = End()

    clock.tick(60)
    pygame.display.update()

pygame.quit()
sys.exit()
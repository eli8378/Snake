import pygame

import sys

from game import Game
from start import Start
from end import End
from settings import Settings


pygame.init()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
game = Game()
start = Start()
end = End()
settings = Settings()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
startMenu = True
isPlaying = False
pausedState = False
gameOver = False
settingState = False

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SCREEN_UPDATE:
            if isPlaying:
                game.update()
        end.endMenu(event)
        end.quitLogic(event)
        end.tryAgainLogic(event)
        start.startLogic(event)
        start.quitLogic(event)
        game.snake.snakeLogic(event)
        start.settingsLogic(event)
        settings.backLogic(event)

    if startMenu:
        start.startMenu()
        if start.startButtonState is True:
            startMenu = False
            isPlaying = True
        elif start.quitButtonState is True:
            running = False
        elif start.settingsButtonState is True:
            settingState = True
            startMenu = False
            start.settingsButtonState = False
    elif settingState:
        settingState = Settings()
        settings.settingsMenu()
        if settings.backButtonState is True:
            settingState = False
            startMenu = True
            settings.backButtonState = False
    elif isPlaying:
        pygame.mouse.set_visible(False)
        game.drawElements()
        if game.checkFailure() == "failed":
            gameOver = True
            isPlaying = False
    elif gameOver:
        pygame.mouse.set_visible(True)
        score = game.endGame()
        end.endMenu(score)
        if end.quitState is True:
            running = False
        elif end.tryAgainState is True:
            gameOver = False
            isPlaying = True
            game = Game()
            end = End()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
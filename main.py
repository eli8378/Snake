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
startMenu = True
isPlaying = False
pausedState = False
gameOver = False
settings = False

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SCREEN_UPDATE:
            if isPlaying:
                game.update()

        #Functions that define the events for clicking on buttons and controlling the snake
        end.endMenu(event)
        end.quitLogic(event)
        end.tryAgainLogic(event)
        start.startLogic(event)
        start.quitLogic(event)
        game.snake.snakeLogic(event)
    
    #If start menu is true, run the start menu function which draws all of the start menus elements
    if startMenu:
        start.startMenu()
        if start.startButtonState is True:
            startMenu = False
            isPlaying = True
        elif start.quitButtonState is True:
            running = False
    
    #If isPlaying is True then draw all of games elements
    elif isPlaying:
        pygame.mouse.set_visible(False)
        game.drawElements()
        if game.checkFailure() == "failed":
            gameOver = True
            isPlaying = False

    #If gameOver is True then call the endGame from function from the game class which draws the end screen
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

    #Refresh rate and screen update
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()
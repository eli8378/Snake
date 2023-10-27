from strawberry import Strawberry
from snake import Snake
import config

import pygame


class Game:
    def __init__(self):
        self.pressed = pygame.mouse.get_pressed()
        self.gameFont = pygame.font.Font(None, 25)
        self.snake = Snake()
        self.strawberry = Strawberry()
        self.endScore = 0
        self.bgImage = pygame.image.load("images/snakebackroundupdated.png")
        self.scoreText = str(len(self.snake.body) - 3)

    def update(self):
        self.snake.update()
        self.checkCollision()
        self.checkFailure()

    def drawElements(self):
        config.screen.blit(self.grass, (0,0))
        self.strawberry.drawStrawberry()
        self.snake.drawSnake()
        self.drawScore()

    def checkCollision(self):
        if self.strawberry.pos == self.snake.body[0]:
            self.strawberry = Strawberry()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)
            self.endScore +=1

    
    def endGame(self):
        return str(len(self.snake.body) - 3)

    def checkFailure(self):
        if not 0 <= self.snake.body[0].x < config.CELL_NUMBER:
            return "failed"
        elif not 0 <= self.snake.body[0].y < config.CELL_NUMBER:
            return "failed"
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return "failed"

    def drawScore(self):
        self.scoreText = str(len(self.snake.body) - 3)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (0,0,0))
        self.scorex = int(config.CELL_SIZE * config.CELL_NUMBER - 60)
        self.scorexy = int(config.CELL_SIZE * config.CELL_NUMBER - 40)
        self.scoreRect = self.scoreSurface.get_rect(center = (self.scorex, self.scorexy))
        config.screen.blit(self.scoreSurface, self.scoreRect)

    


        

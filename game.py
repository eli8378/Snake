from fruit import Fruit
from snake import Snake

import pygame


class Game:
    def __init__(self):
        self.pressed = pygame.mouse.get_pressed()
        self.cellSize = 40
        self.cellNumber = 20
        self.gameFont = pygame.font.Font(None, 25)
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.snake = Snake()
        self.fruit = Fruit()
        self.endScore = 0
        self.scoreText = str(len(self.snake.body) - 3)

    def update(self):
        self.snake.update()
        self.checkCollision()
        self.checkFailure()

    def drawElements(self):
        self.screen.fill((175,215,70))
        self.fruit.drawFruit()
        self.snake.drawSnake()
        self.drawScore()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)
            self.endScore +=1
    
    def endGame(self):
        return len(self.snake.body) - 3

    def checkFailure(self):
        if not 0 <= self.snake.body[0].x < self.cellNumber:
            return "failed"
        elif not 0 <= self.snake.body[0].y < self.cellNumber:
            return "failed"
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return "failed"

    def drawScore(self):
        self.scoreText = str(len(self.snake.body) - 3)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (56,74,12))
        self.scorex = int(self.cellSize * self.cellNumber - 60)
        self.scorexy = int(self.cellSize * self.cellNumber - 40)
        self.scoreRect = self.scoreSurface.get_rect(center = (self.scorex, self.scorexy))
        self.screen.blit(self.scoreSurface, self.scoreRect)

    


        

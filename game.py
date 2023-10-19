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

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFailure()

    def drawElements(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()
        self.drawScore()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)

    def checkFailure(self):
        if not 0 <= self.snake.body[0].x < self.cellNumber:
            self.screen.fill((175,215,70))
            self.gameOverScreen()
            pygame.time.wait(1300)
            pygame.quit()
        elif not 0 <= self.snake.body[0].y < self.cellNumber:
            self.screen.fill((175,215,70))
            self.gameOverScreen()
            pygame.time.wait(1300)
            pygame.quit()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.screen.fill((175,215,70))
                self.gameOverScreen()
                pygame.time.wait(1300)
                pygame.quit()

    def drawScore(self):
        self.scoreText = str(len(self.snake.body) - 3)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (56,74,12))
        self.scorex = int(self.cellSize * self.cellNumber - 60)
        self.scorexy = int(self.cellSize * self.cellNumber - 40)
        self.scoreRect = self.scoreSurface.get_rect(center = (self.scorex, self.scorexy))
        self.screen.blit(self.scoreSurface, self.scoreRect)
    
    def gameOverScreen(self):
        self.gameOverSurface = self.gameFont.render("GAME OVER", True, (56,74,12))
        self.showScoreSurface = self.gameFont.render("SCORE: ", True, (56,74,12))
        self.gameOverRect = self.gameOverSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2))
        self.showScoreRect = self.showScoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 18, self.cellSize * self.cellNumber / 2 + 60))
        self.scoreRect = self.scoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 45, self.cellSize * self.cellNumber / 2 + 60))
        self.screen.blit(self.gameOverSurface, self.gameOverRect)
        self.screen.blit(self.showScoreSurface, self.showScoreRect)
        self.screen.blit(self.scoreSurface, self.scoreRect)
        pygame.display.update()

"""
    def quitButton(self):
        quitSurface = self.gameFont.render("QUIT", True, (56,74,12))
        quitRect = quitSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 60))
        self.screen.blit(quitSurface, quitRect)

    def tryAgainButton(self):
        tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (56,74,12))
        tryAgainRect = tryAgainSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 120))
        self.screen.blit(tryAgainSurface, tryAgainRect)

"""
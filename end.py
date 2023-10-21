import pygame

from snake import Snake

class End:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.gameFont = pygame.font.Font(None, 25)
        self.snake = Snake()
        self.scoreText = str(len(self.snake.body) - 3)

    def drawScoreGameOver(self):
        self.scoreText = str(len(self.snake.body) - 3)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (56,74,12))
        self.scoreRect = self.scoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 45, self.cellSize * self.cellNumber / 2 + 60))
        self.screen.blit(self.scoreSurface, self.scoreRect)
    
    def gameOverScreen(self):
        self.screen.fill((175,215,70))
        self.gameOverSurface = self.gameFont.render("GAME OVER", True, (56,74,12))
        self.showScoreSurface = self.gameFont.render("SCORE: ", True, (56,74,12))
        self.gameOverRect = self.gameOverSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2))
        self.showScoreRect = self.showScoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 18, self.cellSize * self.cellNumber / 2 + 60))
        self.drawScoreGameOver()
        self.quitButton()
        self.tryAgainButton()
        self.screen.blit(self.gameOverSurface, self.gameOverRect)
        self.screen.blit(self.showScoreSurface, self.showScoreRect)
        pygame.display.update()

    def quitButton(self):
        self.quitSurface = self.gameFont.render("QUIT", True, (56,74,12))
        self.quitRect = self.quitSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 45, self.cellSize * self.cellNumber / 2 + 120))
        self.screen.blit(self.quitSurface, self.quitRect)

    def tryAgainButton(self):
        tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (56,74,12))
        tryAgainRect = tryAgainSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 41, self.cellSize * self.cellNumber / 2 + 120))
        self.screen.blit(tryAgainSurface, tryAgainRect)
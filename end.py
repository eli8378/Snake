import pygame

from snake import Snake
from game import Game

class End:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.gameFont = pygame.font.Font(None, 25)
        self.snake = Snake()
        self.game = Game()
        self.quitState = False
        self.tryAgainState = False

        self.quitButtonSurface = self.gameFont.render("QUIT", True, (56,74,12))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 45, self.cellSize * self.cellNumber / 2 + 120))
        self.tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (56,74,12))
        self.tryAgainRect = self.tryAgainSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 41, self.cellSize * self.cellNumber / 2 + 120))

    def endMenu(self, score):
        self.screen.fill((175,215,70))
        self.drawScoreOnEnd()
        self.quitButton()
        self.tryAgainButton()
        self.drawScoreGameOver(score)
        self.drawGameOverText()


    def drawScoreGameOver(self, score):
        self.scoreText = str(score)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (56,74,12))
        self.scoreRect = self.scoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 45, self.cellSize * self.cellNumber / 2 + 60))
        self.screen.blit(self.scoreSurface, self.scoreRect)

    def drawGameOverText(self):
        self.gameOverSurface = self.gameFont.render("GAME OVER", True, (56,74,12))
        self.gameOverRect = self.gameOverSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2))
        self.screen.blit(self.gameOverSurface, self.gameOverRect)
    
    def drawScoreOnEnd(self):
        self.screen.fill((175,215,70))
        self.showScoreSurface = self.gameFont.render("SCORE: ", True, (56,74,12))
        self.showScoreRect = self.showScoreSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 18, self.cellSize * self.cellNumber / 2 + 60))
        self.screen.blit(self.showScoreSurface, self.showScoreRect)
        
    def quitLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.quitButtonRect.collidepoint(pos):
                self.quitState = True
            else:
                self.quitState = False

    def quitButton(self):
        self.quitButtonSurface = self.gameFont.render("QUIT", True, (56,74,12))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 - 45, self.cellSize * self.cellNumber / 2 + 120))
        self.screen.blit(self.quitButtonSurface, self.quitButtonRect)

    def tryAgainLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.tryAgainRect.collidepoint(pos):
                self.tryAgainState = True
            else:
                self.tryAgainState = False

    def tryAgainButton(self):
        self.tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (56,74,12))
        self.tryAgainRect = self.tryAgainSurface.get_rect(center = (self.cellSize * self.cellNumber / 2 + 41, self.cellSize * self.cellNumber / 2 + 120))
        self.screen.blit(self.tryAgainSurface, self.tryAgainRect)
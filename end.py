import pygame

from snake import Snake
from game import Game
import config

class End:
    def __init__(self):
        self.gameFont = pygame.font.Font(None, 25)
        self.snake = Snake()
        self.game = Game()
        self.quitState = False
        self.tryAgainState = False

        self.quitButtonSurface = self.gameFont.render("QUIT", True, (0,0,0))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 - 45, config.CELL_SIZE * config.CELL_NUMBER / 2 + 120))
        self.tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (0,0,0))
        self.tryAgainRect = self.tryAgainSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 + 41, config.CELL_SIZE * config.CELL_NUMBER / 2 + 120))

    def endMenu(self, score):
        config.screen.fill((115,221,45))
        self.drawScoreOnEnd()
        self.quitButton()
        self.tryAgainButton()
        self.drawScoreGameOver(score)
        self.drawGameOverText()


    def drawScoreGameOver(self, score):
        self.scoreText = str(score)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (0,0,0))
        self.scoreRect = self.scoreSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 + 45, config.CELL_SIZE * config.CELL_NUMBER / 2 + 60))
        config.screen.blit(self.scoreSurface, self.scoreRect)

    def drawGameOverText(self):
        self.gameOverSurface = self.gameFont.render("GAME OVER", True, (0,0,0))
        self.gameOverRect = self.gameOverSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2))
        config.screen.blit(self.gameOverSurface, self.gameOverRect)
    
    def drawScoreOnEnd(self):
        self.showScoreSurface = self.gameFont.render("SCORE: ", True, (0,0,0))
        self.showScoreRect = self.showScoreSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 - 18, config.CELL_SIZE * config.CELL_NUMBER / 2 + 60))
        config.screen.blit(self.showScoreSurface, self.showScoreRect)
        
    def quitLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.quitButtonRect.collidepoint(pos):
                self.quitState = True

    def quitButton(self):
        self.quitButtonSurface = self.gameFont.render("QUIT", True, (0,0,0))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 - 45, config.CELL_SIZE * config.CELL_NUMBER / 2 + 120))
        self.quitButtonBgRect = pygame.Rect(config.CELL_SIZE * config.CELL_NUMBER / 2-68, config.CELL_SIZE * config.CELL_NUMBER / 2 + 105,50,30)
        pygame.draw.rect(config.screen, (211, 211, 211), self.quitButtonBgRect)
        pos = pygame.mouse.get_pos()
        if self.quitButtonRect.collidepoint(pos):
            pygame.draw.rect(config.screen, (128, 128, 128), self.quitButtonBgRect)
        config.screen.blit(self.quitButtonSurface, self.quitButtonRect)

    def tryAgainLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.tryAgainRect.collidepoint(pos):
                self.tryAgainState = True

    def tryAgainButton(self):
        self.tryAgainSurface = self.gameFont.render("TRY AGAIN", True, (0,0,0))
        self.tryAgainRect = self.tryAgainSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2 + 41, config.CELL_SIZE * config.CELL_NUMBER / 2 + 120))
        self.tryAgainButtonBgRect = pygame.Rect(config.CELL_SIZE * config.CELL_NUMBER / 2-10, config.CELL_SIZE * config.CELL_NUMBER / 2 + 105,100,30)
        pygame.draw.rect(config.screen, (211, 211, 211), self.tryAgainButtonBgRect)
        pos = pygame.mouse.get_pos()
        if self.tryAgainRect.collidepoint(pos):
            pygame.draw.rect(config.screen, (128, 128, 128), self.tryAgainButtonBgRect)
        config.screen.blit(self.tryAgainSurface, self.tryAgainRect)
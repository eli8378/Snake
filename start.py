import pygame

import config


class Start:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.CELL_NUMBER * config.CELL_SIZE, config.CELL_NUMBER * config.CELL_SIZE))
        self.gameFont = pygame.font.Font(None, 25)
        self.startButtonState = False
        self.quitButtonState = False
    
    def startMenu(self):
        self.screen.fill((175,215,250))
        self.drawTitle()
        self.drawStartButton()
        self.drawQuitButton()


    def drawTitle(self):
        self.startSurface = self.gameFont.render("SNAKE GAME", True, (0,0,0))
        self.startRect = self.startSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2))
        self.screen.blit(self.startSurface, self.startRect)

    def startLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.startButtonRect.collidepoint(pos):
                self.startButtonState = True
            else:
                self.startButtonState = False

    def drawStartButton(self):
        self.startButtonSurface = self.gameFont.render("START", True, (0,0,0))
        self.startButtonRect = self.startButtonSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2 + 50))
        self.screen.blit(self.startButtonSurface, self.startButtonRect)

    def quitLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.quitButtonRect.collidepoint(pos):
                self.quitButtonState = True
            else:
                self.quitButtonState = False
    
    def drawQuitButton(self):
        self.quitButtonSurface = self.gameFont.render("QUIT", True, (0,0,0))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2 + 100))
        self.screen.blit(self.quitButtonSurface, self.quitButtonRect)

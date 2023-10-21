import pygame


class Start:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.gameFont = pygame.font.Font(None, 25)
        self.startButtonState = False
        self.quitButtonState = False
    
    def startMenu(self):
        self.screen.fill((175,215,70))
        self.drawTitle()
        self.drawStartButton()
        self.drawQuitButton()
        pygame.display.update()

    def drawTitle(self):
        self.startSurface = self.gameFont.render("SNAKE GAME", True, (56,74,12))
        self.startRect = self.startSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2))
        self.screen.blit(self.startSurface, self.startRect)

    def startLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.startButtonRect.collidepoint(pos):
                self.startButtonState = True
            else:
                self.startButtonState = False

    def drawStartButton(self):
        self.startButtonSurface = self.gameFont.render("START", True, (56,74,12))
        self.startButtonRect = self.startButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 50))
        self.screen.blit(self.startButtonSurface, self.startButtonRect)

    def quitLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.quitButtonRect.collidepoint(pos):
                self.quitButtonState = True
            else:
                self.quitButtonState = False
    
    def drawQuitButton(self):
        self.quitButtonSurface = self.gameFont.render("QUIT", True, (56,74,12))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 100))
        self.screen.blit(self.quitButtonSurface, self.quitButtonRect)
        self.quitButtonRect = self.quitButtonRect
    

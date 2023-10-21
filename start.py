import pygame


class Start:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.gameFont = pygame.font.Font(None, 25)
    
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

    def drawStartButton(self):
        self.startButtonSurface = self.gameFont.render("START", True, (56,74,12))
        self.startButtonRect = self.startButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 50))
        self.startLogic()
        self.screen.blit(self.startButtonSurface, self.startButtonRect)
    
    def startLogic(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.startButtonRect.collidepoint(pos):
                    return "start"
    
    def drawQuitButton(self):
        self.quitButtonSurface = self.gameFont.render("QUIT", True, (56,74,12))
        self.quitButtonRect = self.quitButtonSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2 + 100))
        self.quitButtonBg = pygame.draw.rect(self.screen, (175,5,70), self.quitButtonRect)
        self.quitLogic()
        self.screen.blit(self.quitButtonSurface, self.quitButtonRect)
    
    def quitLogic(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.quitButtonBg.collidepoint(pos):
                    return "quit"

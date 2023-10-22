import pygame

class Paused:
    def __init__(self):
        self.cellSize = 40
        self.cellNumber = 20
        self.screen = pygame.display.set_mode((self.cellNumber * self.cellSize, self.cellNumber * self.cellSize))
        self.gameFont = pygame.font.Font(None, 25)
    
    def pauseScreen(self):
        self.screen.fill((175,215,70))
        self.drawPaused()

    def drawPaused(self):
        self.startSurface = self.gameFont.render("PAUSED", True, (56,74,12))
        self.startRect = self.startSurface.get_rect(center = (self.cellSize * self.cellNumber / 2, self.cellSize * self.cellNumber / 2))
        self.screen.blit(self.startSurface, self.startRect)

import pygame

import config

class Settings:
    def __init__(self):
        self.gameFont = pygame.font.Font(None, 25)

    def settingsMenu(self):
        config.screen.fill((115,221,45))
    
    def drawSettings(self):
        self.startSurface = self.gameFont.render("WASD", True, (0,0,0))
        self.startRect = self.startSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2))
        config.screen.blit(self.startSurface, self.startRect)





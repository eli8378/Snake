import pygame

import config

class Settings:
    def __init__(self):
        self.gameFont = pygame.font.Font(None, 25)
        self.backButtonState = False
        self.backSurface = self.gameFont.render("Back", True, (0,0,0))
        self.backRect = self.backSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2 + 300))


    def settingsMenu(self):
        config.screen.fill((115,221,45))
        self.drawSettings()
        self.drawBackButton()
    
    def drawSettings(self):
        self.settingsSurface = self.gameFont.render("WASD", True, (0,0,0))
        self.settingsRect = self.settingsSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2))
        config.screen.blit(self.settingsSurface, self.settingsRect)
    
    def drawBackButton(self):
        self.backRect = self.backSurface.get_rect(center = (config.CELL_SIZE * config.CELL_NUMBER / 2, config.CELL_SIZE * config.CELL_NUMBER / 2 + 300))
        config.screen.blit(self.backSurface, self.backRect)
    
    def backLogic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.backRect.collidepoint(pos):
                self.backButtonState = True
    
    def WASDButton(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.WASDRect.collidepoint(pos):
                self.WASDButtonState = True







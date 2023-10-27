from strawberry import Strawberry
from snake import Snake
import config

import pygame


class Game:
    def __init__(self):
        self.pressed = pygame.mouse.get_pressed()
        self.gameFont = pygame.font.Font(None, 25)
        self.snake = Snake()
        self.strawberry = Strawberry()
        self.endScore = 0
        self.bgImage = pygame.image.load("images/grass.jpeg")
        self.bgImage = pygame.transform.scale(self.bgImage, (800,800))
        self.scoreText = str(len(self.snake.body) - 3)
        self.eatSound = pygame.mixer.Sound('sounds/crunch.mp3')
        self.eatSound.set_volume(0.3)
        
    #Updates snake and checks for collision/failure
    def update(self):
        self.snake.update()
        self.checkCollision()
        self.checkFailure()

    #Draws everything onto the game screen
    def drawElements(self):
        config.screen.blit(self.bgImage, (0,0))
        self.strawberry.drawStrawberry()
        self.snake.drawSnake()
        self.drawScore()

    #Adds to endscore/snakebody and plays sound if collision
    def checkCollision(self):
        if self.strawberry.pos == self.snake.body[0]:
            self.strawberry = Strawberry()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)
            pygame.mixer.Sound.play(self.eatSound)
            pygame.mixer.music.stop()
            self.endScore +=1
    
    #Returns final score
    def endGame(self):
        return str(len(self.snake.body) - 3)

    #Returns failed if snake hits sides of screen or itself
    def checkFailure(self):
        if not 0 <= self.snake.body[0].x < config.CELL_NUMBER:
            return "failed"
        
        elif not 0 <= self.snake.body[0].y < config.CELL_NUMBER:
            return "failed"
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return "failed"

    #Draws score onto screen on the bottom middle 
    def drawScore(self):
        self.scoreText = str(len(self.snake.body) - 3)
        self.scoreSurface = self.gameFont.render(self.scoreText, True, (0,0,0))
        self.scorex = int(config.CELL_SIZE * config.CELL_NUMBER - 400)
        self.scorexy = int(config.CELL_SIZE * config.CELL_NUMBER - 40)
        self.scoreRect = self.scoreSurface.get_rect(center = (self.scorex, self.scorexy))
        config.screen.blit(self.scoreSurface, self.scoreRect)

    


        

import pygame
import sys
from screenn import Settingss
from frogg import Frogg

class Frog:
    def __init__(self):
        pygame.init()
        self.screenn = Settingss()
        self.screen = pygame.display.set_mode((self.screenn.width, self.screenn.height))
        pygame.display.set_caption('Plate')
        icon = pygame.image.load('logo.ico')
        pygame.display.set_icon(icon)
        self.frogg = Frogg(self.screen)

    def CheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.frogg.isRight = True
                elif event.key == pygame.K_a:
                    self.frogg.isLeft = True
                elif event.key == pygame.K_w:
                    self.frogg.isWhele = True
                elif event.key == pygame.K_s:
                    self.frogg.isSat = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.frogg.isRight = False
                elif event.key == pygame.K_a:
                    self.frogg.isLeft = False
                elif event.key == pygame.K_w:
                    self.frogg.isWhele = False
                elif event.key == pygame.K_s:
                    self.frogg.isSat = False

    def Start(self):
        while True:
            self.CheckEvent()
            self.frogg.update()
            self.screen.fill(self.screenn.colour)
            self.frogg.Blitme()
            pygame.display.flip()


if __name__ == '__main__':
    game = Frog()
    game.Start()

import pygame
class Frogg:
    def __init__(self, screen):
        self.Screen = screen
        self.ScreenRect = self.Screen.get_rect()
        self.image = pygame.image.load("Images/frog1.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.ScreenRect.midbottom
        self.isRight = False
        self.isLeft = False
        self.isWhele = False
        self.isSat = False
    def Blitme(self):
        self.Screen.blit(self.image,self.rect)

    def update(self):
        if self.isRight == True:
            self.rect.x += 1
        if self.isLeft == True:
            self.rect.x -= 1
        if self.isWhele == True:
            self.rect.y -= 1
        if self.isSat == True:
            self.rect.y += 1

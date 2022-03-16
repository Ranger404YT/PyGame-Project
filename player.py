#Мы не несём ответствености при изменении кода игры

import pygame

class Player:

    def __init__(self, screen, model):
        self.screen = screen
        self.image = model
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.centery = float(self.rect.centery)
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mleft=False
        self.mright=False
        self.mup=False
        self.mdown=False

    def output(self):
        self.screen.blit(self.image,self.rect)
        pass

    def update(self):
        if self.mright and self.rect.right < self.screen_rect.right + 2:
            self.centerx += 0.08
        if self.mleft and self.rect.right > 26:
            self.centerx -= 0.08
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 0.08
        if self.mup and self.rect.top > self.screen_rect.top:
            self.centery -= 0.08
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
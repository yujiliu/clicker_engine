import time

import pygame
from pygame.sprite import Sprite
from pygame.color import THECOLORS


class Button(Sprite):
    def __init__(self, screen):
        super(Button, self).__init__()
        self.screen = screen

        self.text = ''
        self.font = pygame.font.Font('data/fonts/Fipps-Regular.otf', 30)

        self.active = False

        self.text_color = THECOLORS['black']
        self.image = pygame.image.load('data/images/start_button_unactive.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - 50

    def output(self):
        self.screen.blit(self.image, self.rect)
        time.sleep(0.05)
        self.text_img = self.font.render(str(self.text), True, self.text_color, None)
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = self.rect.center
        self.center = self.screen_rect.centerx
        self.screen.blit(self.text_img, self.text_rect)

    def update(self):
        pass

    def create_button(self):
        self.center = self.screen_rect.centerx
        self.screen.blit(self.text_img, self.rect)


class StartButton(Button):
    def __init__(self, screen):
        super(StartButton, self).__init__(screen)

        self.mode_menu = True
        self.text = 'START GAME'
        self.image = pygame.image.load('data/images/start_button_unactive.png')

    def update(self):
        super(StartButton, self).update()
        if self.active:
            self.image = pygame.image.load('data/images/start_button_active.png')
            self.active = False
        else:
            self.image = pygame.image.load('data/images/start_button_unactive.png')


class SettingsButton(Button):
    def __init__(self, screen):
        super(SettingsButton, self).__init__(screen)

        self.image = pygame.image.load('data/images/settings.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.right = self.screen_rect.right - 20
        self.rect.top = self.screen_rect.top + 20

    def output(self):
        self.screen.blit(self.image, self.rect)

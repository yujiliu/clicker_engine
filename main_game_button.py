import pygame
import time
from button import Button


class MainGameButton(Button):
    def __init__(self, screen):
        super(MainGameButton, self).__init__(screen)
        self.counter = 0
        self.text = str(self.counter)
        self.image = pygame.image.load('data/images/start_button_unactive.png')

    def update(self):
        super(MainGameButton, self).update()
        if self.active:
            self.image = pygame.image.load('data/images/start_button_active.png')
            self.counter += 1
            self.text = str(self.counter)
            self.active = False
        else:
            self.image = pygame.image.load('data/images/start_button_unactive.png')

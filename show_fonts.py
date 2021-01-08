import pygame
from pygame.locals import *
from collections import namedtuple
from game_screens import Point, Button, GameScreen, MenuScreen

class ShowFonts(GameScreen):
    def __init__(self):
        pygame.init()
        size = Point(600, 600)
        screen = pygame.display.set_mode(size)
        super().__init__(screen, size)
        self.fonts = pygame.font.get_fonts()
        self.fonts_length = len(self.fonts)
        self.font_index = 0
        self.font_size = 20
        self.center = Point(size.x / 2, size.y / 2)

    def keyboard_input(self, event: pygame.event.Event):
        if event.key == K_UP:
            self.font_size += 1
        elif event.key == K_DOWN:
            self.font_size -= 1
            if self.font_size < 1:
                self.font_size = 1
        elif event.key == K_RIGHT:
            self.font_index += 1
            if self.font_index >= self.fonts_length:
                self.font_index %= self.fonts_length
        elif event.key == K_LEFT:
            self.font_index -= 1
            if self.font_index < 0:
                self.font_index = self.font_size - 1

    def update(self):
        super().update()
        font = self.fonts[self.font_index]
        text = pygame.font.SysFont(font, self.font_size).render(f'{font} {self.font_size}', True, (255, 255, 255))
        text_size = Point._make(text.get_size())
        self.screen.blit(text, (self.center.x - text_size.x / 2, self.center.y - text_size.y / 2))

if __name__ == "__main__":
    game = ShowFonts()
    game.run()

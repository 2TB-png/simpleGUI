import pygame
from Tools.pynche.StripViewer import constant


class Element:
    def __init__(self, x, y, width, height, el_type = "element"):

        self.__rect = pygame.Rect(x, y, width, height)
        self.default_screen = None

        self.type = el_type

    def update(self, screen = -1):
        if screen == -1:
            screen = self.default_screen
        ...


    def set_screen(self, screen):
        self.default_screen = screen

    def move(self, x, y):
        self.__rect.move(x, y)

    def get_pos(self):
        return self.__rect.x, self.__rect.y

    def get_rect(self):
        return self.__rect



    def render_debug(self, screen = -1, debug_color="red", border_width=1):
        if screen == -1:
            screen = self.default_screen

        pygame.draw.rect(screen, debug_color, self.__rect, border_width)



    def __str__(self):
        return f"<Element of type {self.type} at {(self.__rect.x, self.__rect.y)}>"

    def __repr__(self):
        return f"<{self.type}( pos={(self.__rect.x, self.__rect.y)}, width={self.__rect.w}, height={self.__rect.h})>"
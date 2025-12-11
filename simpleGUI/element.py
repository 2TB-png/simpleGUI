import pygame


class Element:
    def __init__(self, x: int, y: int, width: int, height: int, el_type: str = "element"):

        self.__rect = pygame.Rect(x, y, width, height)
        self.default_screen = None

        self.type = el_type
        self.tags = []

    def update(self, screen = None):
        if screen is None:
            screen = self.default_screen
        ...

    def set_screen(self, screen):
        self.default_screen = screen

    def move(self, x, y):
        self.__rect.x = x
        self.__rect.y = y

    def get_pos(self):
        return self.__rect.x, self.__rect.y

    def get_dimensions(self):
        return self.__rect.width, self.__rect.height

    def get_rect(self):
        return self.__rect

    def get_id(self):
        return id(self)

    def render_debug(self, screen = None, debug_color=(255, 0, 0), border_width=2):
        if screen is None:
            screen = self.default_screen

        pygame.draw.rect(screen, debug_color, self.__rect, border_width)



    def __str__(self):
        return f"<Element of type {self.type} at {(self.__rect.x, self.__rect.y)}>"

    def __repr__(self):
        return f"<{self.type}( pos={(self.__rect.x, self.__rect.y)}, width={self.__rect.w}, height={self.__rect.h})>"
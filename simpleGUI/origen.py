import pygame

class Origen:
    def __init__(self, x: int, y: int, el_type: str = "origen"):
        self.x = x
        self.y = y
        self.el_type = el_type

        self.default_screen = None

        self.__elements = []


    def add_elements(self, *elements):
        for element in elements:
            self.__elements.append(element)


    def get_elements_by_id(self, el_id: int):
        for element in self.__elements:
            if element.id == el_id:
                return element
        raise Exception(f"Element with id {el_id} not found")

    def update(self, screen = None):
        if screen is None:
            screen = self.default_screen

        for element in self.__elements:
            element_pos = element.get_pos()

            element.move(element_pos[0] + self.x, element_pos[1] + self.y)

            element.update(screen)

            element.move(element_pos[0], element_pos[1])

    def render_debug(self, screen = None, debug_color="red", border_width=1):
        if screen is None:
            screen = self.default_screen

        for element in self.__elements:
            element_pos = element.get_pos()
            element.move(element_pos[0] + self.x, element_pos[1] + self.y)

            element.render_debug(screen, debug_color, border_width)

            element.move(element_pos[0], element_pos[1])


    def set_screen(self, screen):
        self.default_screen = screen


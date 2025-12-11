from simpleGUI.element import Element

import pygame

class Origin:
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

            element.move(element.get_pos()[0] + self.x, element.get_pos()[1] + self.y)

            element.update(screen)

            element.move(element.get_pos()[0] - self.x, element.get_pos()[1] - self.y)

    def render_debug(self, screen = None, debug_color="red", border_width=1):
        if screen is None:
            screen = self.default_screen

        for element in self.__elements:

            element.move(element.get_pos()[0] + self.x, element.get_pos()[1] + self.y)

            element.render_debug(screen, debug_color, border_width)

            element.move(element.get_pos()[0], element.get_pos()[1])

    def set_screen(self, screen):
        self.default_screen = screen

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y


    def get_id(self):
        return id(self)



class Grid(Element):
    def __init__(self, x: int, y: int, width: int, height: int, vertical_nodes, horizontal_nodes, el_type: str = "grid"):
        super().__init__(x, y, width, height, el_type = el_type)

        self.horizontal_nodes = horizontal_nodes
        self.vertical_nodes = vertical_nodes

        self.horizontal_step = width // self.horizontal_nodes
        self.vertical_step = height // self.vertical_nodes

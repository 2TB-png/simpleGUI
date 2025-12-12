import pygame
from simpleGUI import element

pygame.init()

class Label(element.Element):
    def __init__(self, x:int, y:int, width:int, height:int, text:str="Label", text_color:tuple[int,int,int]=(0, 0, 0),
                 font:pygame.font.Font=pygame.font.SysFont('monospace', 32), bg=None, el_type="Label"):

        super().__init__(x, y, width, height, el_type)

        if bg is None:
            color = (150, 150, 150)
            bg = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
            pygame.draw.rect(bg, color, bg.get_rect(), border_radius=min(width, height)//10)

        self.text = text
        self.text_color = text_color
        self.font = font
        self.bg = bg

    def update(self, screen = None, render=True):
        if screen is None:
            screen = self.default_screen

        text_render = self.font.render(self.text, True, (255,255,255))

        text_rect = text_render.get_rect()
        text_x = self.get_pos()[0] + (self.get_rect().w - text_rect.w) // 2
        text_y = self.get_pos()[1] + (self.get_rect().h - text_rect.h) // 2

        if render:
            screen.blit(self.bg, self.get_pos())
            screen.blit(text_render, (text_x, text_y))



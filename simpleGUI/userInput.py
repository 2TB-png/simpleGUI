import pygame
import element

class Button(element.Element):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font, el_type: str = "button", # Basics
                 command=lambda *args:print("Button pressed"), args=(), kwargs=(), # Command setup
                 fg=(150, 150, 150), bg=(100, 100, 100), font_color=(0,0,0), roundness=10, depth=10, push_depth=5): # Style

        super().__init__(x, y, width, height, el_type = el_type)

        # Command control
        self.__text = text
        self.__command = command
        self.__command_args = args
        self.__command_kwargs = kwargs

        # Style
        self.__roundness = roundness
        self.__depth = depth
        self.__push_depth = push_depth
        self.__bg = bg
        self.__fg = fg
        self.__font_color = font_color
        self.__font = font

        # State
        self.__mouse_was_down = False
        self.active = False
        self.hover = False

        self.clicked = False

    def update(self, screen = -1):
        if screen == -1:
            screen = self.default_screen

        self.__do_button_logic()

        self.render_button(screen)


    def __do_button_logic(self):
        mouse = pygame.mouse
        mouse_pos = mouse.get_pos()
        mouse_down = mouse.get_pressed()[0]

        self.clicked = False

        self.hover = self.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])

        if mouse_down and self.hover and not self.__mouse_was_down:
            self.active = True

        if self.active and self.__mouse_was_down and self.hover and not mouse_down :
            self.__command(*self.__command_args)
            self.clicked = True

        if not mouse_down:
            self.active = False

        self.__mouse_was_down = mouse_down


    def render_button(self, screen):

        text = self.__font.render(self.__text, True, self.__font_color)
        text_rect = text.get_rect()
        text_x = self.get_pos()[0] + (self.get_rect().w - text_rect.w)//2
        text_y = self.get_pos()[1] + (self.get_rect().h - text_rect.h)//2


        pygame.draw.rect(screen, self.__bg,
                      pygame.Rect( self.get_rect().x, self.get_rect().y+self.__depth, self.get_rect().w, self.get_rect().h),
                      border_radius=self.__roundness)

        if self.active and self.hover:
            pygame.draw.rect(screen, self.__fg,
                          pygame.Rect(self.get_rect().x, self.get_rect().y + self.__push_depth, self.get_rect().w, self.get_rect().h),
                          border_radius=self.__roundness)

            screen.blit(text, (text_x, text_y + self.__push_depth))

        else:
            pygame.draw.rect(screen, self.__fg, self.get_rect(), border_radius=self.__roundness)

            screen.blit(text, (text_x, text_y))


    def __str__(self):
        return f"<Button with text '{self.__text}' of type {self.type} at {self.get_pos()}>"

    def __repr__(self):
        return f"<Button(type={self.type}, pos={self.get_pos()}, width={self.get_rect().w}, height={self.get_rect().h}, text='{self.__text}', fg={self.__fg}, bg={self.__bg}, font_color={self.__font_color}, roundness={self.__roundness}, depth={self.__depth}, push_depth={self.__push_depth})>"
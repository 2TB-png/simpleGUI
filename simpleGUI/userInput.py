import pygame

from simpleGUI import element, structures

pygame.init()

class Button(element.Element):
    def __init__(self, x: int, y: int, width: int, height: int, text: str = "Text", font = pygame.font.SysFont('monospace', 30), el_type: str = "button", # Basics
                 command=lambda *args:print("Button pressed"), args:tuple=(), kwargs:tuple=(), # Command setup
                 fg: pygame.surface.Surface = None, bg: tuple[int, int, int, int] = (50, 50, 50, 255), font_color = "black", depth:int=10, push_depth:int=5, do_animation: bool = True): # Style

        super().__init__(x, y, width, height, el_type = el_type)

        if fg is None:
            color = (150, 150, 150)
            fg = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
            pygame.draw.rect(fg, color, fg.get_rect(), border_radius=width//10)

        else:
            fg = pygame.transform.scale(fg, (width, height))

        # Command control
        self.__text = text
        self.__command = command
        self.__command_args = args
        self.__command_kwargs = kwargs

        # Style
        self.__depth = depth
        self.__push_depth = push_depth
        self.__bg_color = bg
        self.__fg = fg
        self.__font = font
        self.__font_color = font_color
        self.__do_animation = do_animation

        self.__mask = pygame.mask.from_surface(self.__fg)
        self.__bg = self.__mask.to_surface(setcolor=self.__bg_color, unsetcolor=(0, 0, 0, 0))

        # State
        self.__mouse_was_down = False
        self.active = False
        self.hover = False

        self.clicked = False

    def update(self, screen = None):
        if screen is None:
            screen = self.default_screen

        self.__do_button_logic()

        self.render_button(screen)


    def __do_button_logic(self):
        mouse = pygame.mouse
        mouse_pos = mouse.get_pos()
        mouse_down = mouse.get_pressed()[0]

        relative_x = int(mouse_pos[0] - self.get_pos()[0])
        relative_y = int(mouse_pos[1] - self.get_pos()[1])

        self.clicked = False

        mask_width, mask_height = self.__mask.get_size()

        if 0 <= relative_x < mask_width and 0 <= relative_y < mask_height and self.__mask.get_at((relative_x, relative_y)):
            self.hover = True
        else:
            self.hover = False



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



        screen.blit(self.__bg, (self.get_pos()[0], self.get_pos()[1] + self.__depth))

        if self.active and self.hover and self.__do_animation:
            screen.blit(self.__fg, (self.get_pos()[0], self.get_pos()[1] + self.__push_depth))

            screen.blit(text, (text_x, text_y + self.__push_depth))

        else:
            screen.blit(self.__fg, (self.get_pos()[0], self.get_pos()[1]))

            screen.blit(text, (text_x, text_y))


    def __str__(self):
        return f"<Button with text '{self.__text}' of type {self.type} at {self.get_pos()}>"

    def __repr__(self):
        return f"<Button(type={self.type}, pos={self.get_pos()}, width={self.get_rect().w}, height={self.get_rect().h}, text='{self.__text}', font_color={self.__font_color}, depth={self.__depth}, push_depth={self.__push_depth})>"




class DraggableObject(Button):
    def __init__(self, x: int, y: int, width: int, height: int, text: str = "Text", font=pygame.font.SysFont('monospace', 30), snap_grid: structures.Grid = None, el_type: str = "draggable_object",  # Basics
                 command=lambda *args: print("Button pressed"), args: tuple = (), kwargs: tuple = (),  # Command setup
                 fg: pygame.surface.Surface = None, bg: tuple[int, int, int, int] = (50, 50, 50, 255), font_color="black", depth: int = 10, push_depth: int = 5, do_animation: bool = False):  # Style

        super().__init__(x, y, width, height, text, font, el_type, command, args, kwargs, fg, bg, font_color, depth, push_depth, do_animation)

        self.__relative_x = 0
        self.__relative_y = 0

        self.__snap_grid = snap_grid

        self.__last_pos = (0, 0)


    def update(self, screen = None):
        if screen is None:
            screen = self.default_screen

        self.__do_logic()

        self.render_button(screen)

    def __do_logic(self):
        mouse = pygame.mouse
        mouse_pos = mouse.get_pos()
        mouse_down = mouse.get_pressed()[0]

        self.clicked = False

        self.hover = self.get_rect().collidepoint(mouse_pos[0], mouse_pos[1])

        if mouse_down and self.hover and not self.__mouse_was_down:
            self.active = True
            self.__last_pos = self.get_pos()
            self.__relative_x = mouse_pos[0] - self.get_pos()[0]
            self.__relative_y = mouse_pos[1] - self.get_pos()[1]

        if self.active:
            self.move(mouse_pos[0] - self.__relative_x, mouse_pos[1] - self.__relative_y)

        if not mouse_down:
            self.active = False

            if self.__snap_grid is not None:
                self.handle_snapping()

        self.__mouse_was_down = mouse_down

    def handle_snapping(self):

        pos = self.get_pos()
        self.move(
            int(pos[0] / self.__snap_grid.horizontal_step + 0.5) * self.__snap_grid.horizontal_step,
            int(pos[1] / self.__snap_grid.vertical_step + 0.5) * self.__snap_grid.vertical_step
        )
        pos = self.get_pos()
        grid_pos = self.__snap_grid.get_pos()
        grid_dimensions = self.__snap_grid.get_dimensions()

        if pos[0] < grid_pos[0] or pos[1] < grid_pos[1] or pos[0] >= grid_pos[0] + grid_dimensions[0] or pos[1] >= grid_pos[1] + grid_dimensions[1]:
            self.move(*self.__last_pos)








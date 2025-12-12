import sys
import pygame, simpleGUI.userInput, simpleGUI.structures, simpleGUI.util

pygame.init()

NoN = None

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Simple GUI Test')

f1 = pygame.font.SysFont('monospace', 30)

matrix = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        [NoN, NoN, NoN, NoN, NoN, NoN, NoN, NoN],
        [NoN, NoN, NoN, NoN, NoN, NoN, NoN, NoN],
        [NoN, NoN, NoN, NoN, NoN, NoN, NoN, NoN],
        [NoN, NoN, NoN, NoN, NoN, NoN, NoN, NoN],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

test_image = pygame.image.load("assets/neo/wp.png").convert_alpha()



def main():



    grid = simpleGUI.structures.Grid(100, 100, 800, 800, 8, 8)

    keypad = simpleGUI.util.generate_grid_from_matrix(matrix, 800, 800, separator=0.2, object=simpleGUI.userInput.DraggableObject, snap_grid=grid, do_animation=True)
    keypad.move(100, 100)

    b1 = simpleGUI.userInput.DraggableObject(500, 500, 100, 100, fg = test_image, bg = (0, 0, 0, 10), text = "", snap_grid=grid)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((200, 150, 100))

        grid.render_debug(screen)
        keypad.update(screen)

        b1.update(screen)


        pygame.display.flip()



if __name__ == '__main__':
    main()

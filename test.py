import sys
import pygame, simpleGUI.userInput, simpleGUI.structures, simpleGUI.util

pygame.init()

NoN = None

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Simple GUI Test')

f1 = pygame.font.SysFont('monospace', 30)

def main():

    matrix = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [NoN, '0', NoN],
    ]


    keypad = simpleGUI.util.generate_grid_from_matrix(matrix, 400, 400, f1, object=simpleGUI.userInput.DraggableObject)
    keypad.move(100, 0)
    G = simpleGUI.structures.Grid(100, 100, 800, 800, 8, 8)
    DO = simpleGUI.userInput.DraggableObject(500, 500, 100, 100, "Test", f1, G)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((0,0,0))

        #keypad.update(screen)
        G.render_debug(screen)
        DO.update(screen)

        pygame.display.flip()



if __name__ == '__main__':
    main()

import sys
import pygame, simpleGUI.userInput, simpleGUI.origin, simpleGUI.util

pygame.init()

NoN = None

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple GUI Test')

f1 = pygame.font.SysFont('monospace', 30)

def main():

    matrix = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [NoN, '0', NoN],
    ]


    keypad = simpleGUI.util.generate_button_grid_from_matrix(matrix, 400, 400, f1)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((0,0,0))

        keypad.update(screen)

        pygame.display.flip()



if __name__ == '__main__':
    main()

import simpleGUI.structures, simpleGUI.userInput
import pygame


def generate_grid_from_matrix(matrix, width, height, font, separator: float = 0.1, object = simpleGUI.userInput.Button) -> simpleGUI.structures.Origin:
    rows = len(matrix)
    cols = len(matrix[0])

    vertical_sep = height//rows*separator
    horizontal_sep = width//cols*separator

    button_height = height//rows - vertical_sep
    button_width = width//cols - horizontal_sep

    oby = simpleGUI.structures.Origin(0, 0)

    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] is None:
                continue

            oby.add_elements(
                object(button_width * col + horizontal_sep * (col + 1), button_height * row + vertical_sep * (row + 1),
                                           button_width, button_height,
                                           matrix[row][col], font
                                           )

            )

    return oby

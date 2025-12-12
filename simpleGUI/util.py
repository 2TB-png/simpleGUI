import simpleGUI.structures, simpleGUI.userInput
import pygame


def generate_grid_from_matrix(matrix, width, height, *args, separator: float = 0.1, object = simpleGUI.userInput.Button, **kwargs) -> simpleGUI.structures.Origin:
    rows = len(matrix)
    cols = len(matrix[0])

    vertical_sep = height//rows*separator
    horizontal_sep = width//cols*separator

    obj_height = int(height//rows - vertical_sep)
    obj_width = int(width//cols - horizontal_sep)

    obj = simpleGUI.structures.Origin(0, 0)

    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] is None:
                continue

            obj.add_elements(
                object(obj_width * col + horizontal_sep * (col + 1), obj_height * row + vertical_sep * (row + 1),
                                           obj_width, obj_height,
                                           matrix[row][col], *args, **kwargs
                                           )

            )

    return obj

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print elements in a list of lists in matrix form

    Args:
        matrix: the element that contain list of list

    Returns:
        NULL
    """
    for i in range(len(matrix)):
        if len(matrix[i]) != 0:
            print("{:d} {:d} {:d}".format(matrix[i][0], matrix[i][1], matrix[i][2]))

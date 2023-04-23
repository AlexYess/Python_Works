import doctest


def distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Parameters:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point

    Returns:
        float: Euclidean distance between the two points

    Examples:
        >>> distance(0, 0, 3, 4)
        5.1
        >>> distance(-1, -1, 1, 1)
        2.8284271247461903
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


doctest.testfile("tests.txt")

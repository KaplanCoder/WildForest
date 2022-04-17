from enum import Enum


class Movement(str,Enum):
    Left = "a"
    Right = "d"
    Down = "s"
    Up = "w"


def move(xCoordinate, yCoordinate, moveTypeString):
    """
    It takes  x-y coordinates and returns new coordinates
    based on the move type.
    :param xCoordinate:
    :param yCoordinate:
    :param moveTypeString:
    :return:
    """
    if (moveTypeString == Movement.Left):
        return (xCoordinate - 1, yCoordinate)

    elif (moveTypeString == Movement.Right):
        return (xCoordinate + 1, yCoordinate)

    elif (moveTypeString == Movement.Down):
        return (xCoordinate, yCoordinate + 1)

    elif (moveTypeString == Movement.Up):
        return (xCoordinate, yCoordinate - 1)
    else:
        raise Exception("Move type is not valid!")

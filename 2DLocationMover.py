from enum import Enum


class Movement(str,Enum):
    Left = "a"
    Right = "d"
    Down = "s"
    Up = "w"

def move(currentX,currentY,moveString):
    if (moveString == Movement.Left):
        return (currentX - 1, currentY)
    elif (moveString == Movement.Right):
        return (currentX + 1, currentY)

    elif (moveString == Movement.Down):
        return (currentX, currentY - 1)

    elif (moveString == Movement.Up):
        return (currentX, currentY + 1)
    else:
        raise Exception("Move type is not valid!")

print(move(3,4,"s"))

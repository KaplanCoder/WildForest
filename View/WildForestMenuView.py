from View.WildForestView import WildForestView


class WildForestMenuView:

    def __init__(self,wildForestView:WildForestView):
        self.__wildForestView=wildForestView

    @classmethod
    def printHitWall(cls):
        print("You hit the wall. Try another move!")

    @classmethod
    def printSafeStatus(cls):
        print("You are in a safe room. Don’t worry!")

    @classmethod
    def printStepsTaken(cls,steps):
        print(f"Number of steps taken so far is {steps}")

    @classmethod
    def printWinStatus(cls, name):
        print(f"Yay! You found the {name}!")

    @classmethod
    def printLoseStatus(cls):
        print("Sorry, You died! Game over!")

    @classmethod
    def printWildForest(cls,wildForestView):
        print(wildForestView.getStringFormatOfWildForest())




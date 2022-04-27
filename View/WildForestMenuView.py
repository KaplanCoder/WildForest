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
    def printFound(cls, name):
        print(f"Yay! You found the {name}!")





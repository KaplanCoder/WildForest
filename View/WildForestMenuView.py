from Model.LocationMover import Movement
from View.WildForestView import WildForestView
from Model.WildForest import WildForest
from Model.Creature import Creature

class WildForestMenuView:

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
    def printWildForest(cls,wildForest):
        print(WildForestView.getStringFormatOfWildForest(wildForest))


    @classmethod
    def printNeighboringCreatures(cls,wildForest,rowIndex,columnIndex):
        neighboringCells=wildForest.getNeighboringCells(rowIndex,columnIndex)
        if (len(neighboringCells) == 0):
            cls.printSafeStatus()
            return
        for currentNeighboringCell in neighboringCells:
            assert not currentNeighboringCell.isEmpty()," current neighboring cell can not be empty!"
            currentCreature=currentNeighboringCell.getCreature()
            print("there is a " + str(currentCreature) + " nearby!")

    @classmethod
    def printWelcomeMessage(cls):
        print("Welcome to our WildForest game! \n"
              "In this game, you are a person who is trying to find his brother in the  wild forest \n"
              " There are dangerous monsters here. So,be careful! \n"
              )

    @classmethod
    def getMoveFromTheUser(self):
        print("What is your move?")
        direction=input("Choose right (d), left (a), up (w) or down (s) : ")
        if (isinstance(direction,str)):
           direction=direction.lower()
           enumList=[movementKey.value for movementKey in Movement]
           if (direction in enumList):
               return direction
        raise Exception("There is no such direction! Choose right (d), left (a), up (w) or down (s).")


""" Testing
wild=WildForest(3,3)
c1=Creature(20,30,"Bear")
c2=Creature(40,50,"Tiger")
wild.addCreature(0,1,c1)
wild.addCreature(1,2,c2)
WildForestMenuView.printNeighboringCreatures(wild,2,0)
"""
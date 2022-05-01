from Model.LocationMover import Movement

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
    def printWildForest(cls,wildForestView):
        print(wildForestView.getStringFormatOfWildForest())

    @classmethod
    def printNeighboringCells(cls,wildForestView,rowIndex,columnIndex): # TODO: it will be checked later
        print(wildForestView.getStringFormatOfNeighboringCells(rowIndex,columnIndex))


    @classmethod
    def printNeighboringCreatures(cls,neighboringCreatures):
        for currentCreature in neighboringCreatures:
           print("there is a " + str(currentCreature) + " nearby! \n")

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

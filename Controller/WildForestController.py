
from Model.WildForest import WildForest
from View.WildForestMenuView import WildForestMenuView
from Model.Creature import Creature

# Todo: Controller will handle the move operations of the wild forest
# Todo: It will put creatures to the wild forest randomly.

class WildForestController:


    def __init__(self):
        self.dummyData()


    def dummyData(self):
        self.__wildForest = WildForest(3, 3)  ## model
        self.__playerCreature=Creature(30,0,"Player")
        self.__wildForest.addCreature(0,0,self.__playerCreature)
        self.__playerXcoordinate = 0
        self.__playerYcoordinate = 0
        self.__numberOfSteps = 0


    def updatePlayerCoordinates(self, newCoordinates):
        self.setPlayerXcoordinate = newCoordinates[0]  ## Todo: is it a good approach? Will be checked later
        self.setPlayerYcoordinate = newCoordinates[1]


    def updateStepsTaken(self, newNumberOfSteps):
        self.__numberOfSteps=newNumberOfSteps

    def __createWildForestFromFile(self,wildForestName):
        pass


    def start(self):
        WildForestMenuView.printWelcomeMessage()



    def showMenu(self):
        WildForestMenuView.printNeighboringCreatures(
            self.__wildForest, self.playerXcoordinate, self.playerYcoordinate)
        WildForestMenuView.printStepsTaken(self.numberOfSteps)
        WildForestMenuView.printWildForest(self.__wildForest)
        WildForestMenuView.getMoveFromTheUser()


    def movePlayer(self,moveTypeString):
        moveResult=self.__wildForest.moveCreature(
            self.__playerXcoordinate,self.__playerYcoordinate,moveTypeString)




from Model.WildForest import WildForest
from View.WildForestMenuView import WildForestMenuView
from Model.Creature import Creature
from Model.FightInfo import FIGHTRESULT

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
        self.__playerXcoordinate = newCoordinates[0]  ## Todo: is it a good approach? Will be checked later
        self.__playerYcoordinate = newCoordinates[1]


    def updateStepsTaken(self, newNumberOfSteps):
        self.__numberOfSteps=newNumberOfSteps

    def __createWildForestFromFile(self,wildForestName):
        pass

    def getPlayerCell(self):
        return self.__wildForest.getCell(self.__playerXcoordinate,self.__playerYcoordinate)

    def setDefaultViewOfThePlayerCell(self, newView):
        playerCell= self.getPlayerCell()
        playerCell.setDefaultView(newView)

    def makeVisibleToPlayerCell(self):
        playerCell = self.getPlayerCell()
        playerCell.makeVisible()

    def showNeighboringCells(self):
       neighboringCells= self.__wildForest.getNeighboringCells(self.__playerXcoordinate, self.__playerYcoordinate)
       if (len(neighboringCells) == 0): ## it means no neighboring cells have a creature
           self.setDefaultViewOfThePlayerCell("Safe")
           WildForestMenuView.printSafeStatus()
       else:
           self.setDefaultViewOfThePlayerCell("Dangerous")
           WildForestMenuView.printNeighboringCreatures(neighboringCells)


    def showGameStatus(self):
        self.makeVisibleToPlayerCell()
        self.showNeighboringCells()
        WildForestMenuView.printStepsTaken(self.__numberOfSteps)
        WildForestMenuView.printWildForest(self.__wildForest)



    def showFightStatus(self,fightInfo):
        fightResult = fightInfo.getFightResult()
        if (fightResult == FIGHTRESULT.NOENEMY):
            return
        opponentCreature = fightInfo.getEnemy()
        WildForestMenuView.printFight(opponentCreature)
        if (fightResult == FIGHTRESULT.WON):
            WildForestMenuView.printWinFight(opponentCreature)
        elif (fightResult == FIGHTRESULT.LOST):
            opponentCreature = fightInfo.getEnemy()
            WildForestMenuView.printLoseFight(opponentCreature)
            WildForestMenuView.printLoseGame()  ## when you lose the fight, you lose the game.
        else:
            assert fightResult == FIGHTRESULT.SCORELESS, "Fight result type is not valid!"
            WildForestMenuView.printFightScorelessStatus(opponentCreature)


    def movePlayer(self,moveTypeString):
        try:
            fightInfo=self.__wildForest.moveCreature(
                self.__playerXcoordinate,self.__playerYcoordinate,moveTypeString)
        except Exception: # must be hit wall
            WildForestMenuView.printHitWall()
            return
        newCoordinates=fightInfo.getNewCoordinates()
        self.updatePlayerCoordinates(newCoordinates)
        self.showFightStatus(fightInfo)


    def start(self):
        WildForestMenuView.printWelcomeMessage()
        while (True):
            self.showGameStatus()
            userDirection= WildForestMenuView.getMoveFromTheUser()
            self.movePlayer(userDirection)
            self.updateStepsTaken(self.__numberOfSteps + 1)


w=WildForestController()
w.start()
import time

from Model.WildForest import WildForest
from View.WildForestMenuView import WildForestMenuView
from Model.Creature import Creature
from Model.FightInfo import FIGHTRESULT
from enum import Enum


# Todo: It will put creatures to the wild forest randomly.

class WildForestController:

    class __GAMERESULT(Enum):
        WIN=1,
        LOSE=0

    def __init__(self):
        self.dummyData()


    def dummyData(self):
        self.__wildForest = WildForest(3,3)  ## class attribute
        playerCreature=Creature(30,0,"Your Player")
        m1 = Creature(30, 10, "Bear")
        m2 = Creature(5, 10, "Tiger")
        self.__wildForest.addCreature(0,0,playerCreature)
        self.__creatureToBeFound = Creature(0, 0, "Brother") ## class attribute
        self.__wildForest.addCreature(0, 1, m1)
        self.__wildForest.addCreature(1, 1, m2)
        self.__wildForest.addCreature(2,2,self.__creatureToBeFound)
        self.__playerXcoordinate = 0 ## class attribute
        self.__playerYcoordinate = 0 ## class attribute
        self.__numberOfSteps = 0 ## class attribute


    def calculatePlayerScore(self):
        return 100 / self.__numberOfSteps

    def finishTheGame(self,gameResult):
        playerScore=0
        if (gameResult == self.__GAMERESULT.WIN):
           playerScore=self.calculatePlayerScore()
           WildForestMenuView.printWinGame(self.__creatureToBeFound.getName())
        else:
            assert gameResult == self.__GAMERESULT.LOSE,"Invalid game result!"
            WildForestMenuView.printLoseGame()
        WildForestMenuView.printScore(playerScore)
        exit() # terminate the program

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

    def showPlayerStatus(self):
        playerCell=self.getPlayerCell()
        player=playerCell.getCreature()
        WildForestMenuView.printCreatureStatus(player)

    def showNeighboringCells(self):
        """
        It prints the non-empty neighboring cells of the cell where the player is located.
        However,it doesn't print the neighboring cell containing the creature to be found. \n
        :return:
        """
        neighboringCells= self.__wildForest.getNeighboringCells(self.__playerXcoordinate, self.__playerYcoordinate)
        if (len(neighboringCells) == 0): ## it means no neighboring cells have a creature
           self.setDefaultViewOfThePlayerCell("Safe")
           WildForestMenuView.printSafeStatus()
        else:
           self.setDefaultViewOfThePlayerCell("VoiceHeard")
           WildForestMenuView.printCreaturesVoice(neighboringCells, self.__creatureToBeFound)


    def showGameStatus(self):
        self.showPlayerStatus()
        self.makeVisibleToPlayerCell()
        self.showNeighboringCells()
        WildForestMenuView.printStepsTaken(self.__numberOfSteps)
        WildForestMenuView.printWildForest(self.__wildForest)



    def showFightStatus(self,fightInfo):
        fightResult = fightInfo.getFightResult()
        if (fightResult == FIGHTRESULT.NOENEMY):
            return # no fight to show
        opponentCreature = fightInfo.getEnemy()
        WildForestMenuView.printFight(opponentCreature)
        time.sleep(2)  # added to show fighting process
        if (fightResult == FIGHTRESULT.WON):
            WildForestMenuView.printWinFight(opponentCreature)
        elif (fightResult == FIGHTRESULT.LOST):
            opponentCreature = fightInfo.getEnemy()
            WildForestMenuView.printLoseFight(opponentCreature)
            self.finishTheGame(self.__GAMERESULT.LOSE)
            #  Todo throw exception or return some warning that game is over
        else:
            assert fightResult == FIGHTRESULT.SCORELESS, "Fight result type is not valid!"
            WildForestMenuView.printFightScorelessStatus(opponentCreature)


    def movePlayer(self,moveTypeString):
        try:
            self.updateStepsTaken(self.__numberOfSteps + 1) # Todo: steps must be updated at the beginning or end?
            fightInfo=self.__wildForest.moveCreature(
                self.__playerXcoordinate,self.__playerYcoordinate,moveTypeString)
        except Exception: # must be hit wall Todo: must be custom exception
            WildForestMenuView.printHitWall()
            return
        currentEnemy=fightInfo.getEnemy()
        if (currentEnemy is self.__creatureToBeFound):
            self.finishTheGame(self.__GAMERESULT.WIN)
        newCoordinates=fightInfo.getNewCoordinates()
        self.updatePlayerCoordinates(newCoordinates)
        self.showFightStatus(fightInfo)


    def start(self):
        WildForestMenuView.printWelcomeMessage()
        while (True):
                self.showGameStatus()
                userDirection= WildForestMenuView.getMoveFromTheUser()
                self.movePlayer(userDirection)





w=WildForestController()
w.start()
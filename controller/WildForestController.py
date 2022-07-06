import time

from model.WildForest import WildForest
from view.WildForestMenuView import WildForestMenuView
from model.Creature import Creature
from model.FightInfo import FIGHTRESULT
from customExceptions.InvalidLocationException import InvalidLocationException
from enum import Enum
from model.WildForestFactory import WildForestFactory



# Todo: It will put creatures to the wild forest randomly.


class WildForestController:

    class __GAMERESULT(Enum):
        WIN=1,
        LOSE=0

    def __init__(self,wildForestJsonFileName):
        wildForestFactory=WildForestFactory(wildForestJsonFileName)
        self.__wildForest=wildForestFactory.getWildForest()
        self.__playerXcoordinate =wildForestFactory.getPlayerXcoordinate()
        self.__playerYcoordinate = wildForestFactory.getPlayerYcoordinate()
        self.__creatureToBeFound=wildForestFactory.getCreatureToBeFound()
        self.__numberOfSteps = 0


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
        else:
            assert fightResult == FIGHTRESULT.SCORELESS, "Fight result type is not valid!"
            WildForestMenuView.printFightScorelessStatus(opponentCreature)


    def movePlayer(self,moveTypeString):
        try:
            self.updateStepsTaken(self.__numberOfSteps + 1) # Todo: steps must be updated at the beginning or end?
            fightInfo=self.__wildForest.moveCreature(
                self.__playerXcoordinate,self.__playerYcoordinate,moveTypeString)
        except InvalidLocationException: # must be hit wall
            WildForestMenuView.printHitWall()
            return
        currentEnemy=fightInfo.getEnemy()
        if (currentEnemy is self.__creatureToBeFound):
            self.finishTheGame(self.__GAMERESULT.WIN)
        newCoordinates=fightInfo.getNewCoordinates()
        self.updatePlayerCoordinates(newCoordinates)
        self.showFightStatus(fightInfo)



    def start(self):
        WildForestMenuView.printWelcomeMessage(self.__creatureToBeFound.getName())
        while (True):
                self.showGameStatus()
                userDirection= WildForestMenuView.getMoveFromTheUser()
                self.movePlayer(userDirection)


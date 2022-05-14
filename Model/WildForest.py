import copy

from Model.Creature import Creature
from Model.LocationMover import move,Movement
from Model.Cell import Cell
from Model.FightInfo import FIGHTRESULT, FightInfo


class WildForest:

    def __init__(self,rowSize,columnSize):
        assert rowSize >= 0, "row size can not be negative!"
        assert columnSize >= 0, "column size can not be negative!"
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__wildForestList = [[Cell() for j in range(columnSize)] for i in range(rowSize)]
        # initialize two-dimension array and fill it with empty cells

    def getColumnSize(self):
        return self.__columnSize

    def getRowSize(self):
        return self.__rowSize

    def getWildForestList(self):
        return self.__wildForestList


    def getNeighboringCells(self,rowIndex,columnIndex):
        # Todo: is it  a good approach? Will be checked later \n
        """
        It finds the non-empty neighboring cells of the current cell based on rowIndex and columnIndex \n
        First, It finds the all  new valid x-y coordinates generated after every movement. \n
        Then, It returns all non-empty neighboring cells based on the new x-y coordinates \n
        :param rowIndex:
        :param columnIndex:
        :return:
        """
        neighborsIndex=[]
        neighboringCells=[]
        # rowIndex is a  y-coordinate, columnIndex is at x-coordinae !!!! IMPORTANT
        # we check every movement direction of the current indexes
        neighborsIndex.append(move(columnIndex,rowIndex,Movement.Right))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Left))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Up))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Down))
        copyNeighborsIndex=copy.deepcopy(neighborsIndex)
        # we could  remove the element from the list while looping
        # that's why to prevent conflicts, we use the copy of list
        for neighborsIndexTuple in copyNeighborsIndex:
            newRowIndex=neighborsIndexTuple[1] # rowIndex is a  y-coordinate
            newColumnIndex=neighborsIndexTuple[0] # columnIndex is a x-coordinate
            if not (self.__areIndexesValid(newRowIndex,newColumnIndex)):
                neighborsIndex.remove(neighborsIndexTuple)
            else:
                currentCell=self.__wildForestList[newRowIndex][newColumnIndex]
                if not (currentCell.isEmpty()):
                    neighboringCells.append(currentCell)
        return neighboringCells


    def getCell(self,rowIndex,columnIndex):
        if (self.__areIndexesValid(rowIndex, columnIndex)):
            return self.__wildForestList[rowIndex][columnIndex]
        return None


    def __areIndexesValid(self, rowIndex, columnIndex):
        if (rowIndex >= self.getRowSize() or (rowIndex < 0)):
            return False
        if (columnIndex >= self.getColumnSize() or (columnIndex < 0)):
            return False
        return True

    def findCreature(self, rowIndex,columnIndex):
        currentCell=self.getCell(rowIndex,columnIndex)
        if currentCell is not None:
            return currentCell.getCreature()
        return currentCell

    def makeVisibleToCell(self,rowIndex,columnIndex):
        currentCell = self.__wildForestList[rowIndex][columnIndex]
        currentCell.makeVisible()

    def makeInvisibleToCell(self,rowIndex,columnIndex):
        currentCell = self.__wildForestList[rowIndex][columnIndex]
        currentCell.makeInvisible()


    def addCreature(self,rowIndex, columnIndex,creature):
        assert isinstance(creature, Creature), "Creature object's type is not valid. Program is terminated!"
        if not (self.__areIndexesValid(rowIndex, columnIndex)):
            return False
        currentCell= self.__wildForestList[rowIndex][columnIndex]
        currentCell.setCreature(creature) # TODO: warning occured. will be checked latter
        return True


    def removeCreature(self, rowIndex, columnIndex):
        if not  (self.__areIndexesValid(rowIndex, columnIndex)):
            return False
        else:
            currentCell = self.__wildForestList[rowIndex][columnIndex]
            currentCell.setCreature(None) # creature is removed from the cell as None value is assigned to the cell
            return True


    def __moveOperation(self, currentRowIndex,
                        currentColumnIndex, newRowIndex, newColumnIndex):
        """
        It moves the current creature based on the current and new row-Column index pair. \n
        If current creature encounters an another creature, it fights the another creature \n
        Based on the fight result, fight info object is created and returned. \n
        :param currentRowIndex:
        :param currentColumnIndex:
        :param newRowIndex:
        :param newColumnIndex:
        :return: fight info object
        """
        currentCreature=self.findCreature(currentRowIndex,currentColumnIndex)
        assert currentCreature is not None,"Current creature can not be None!"
        fightInfo = None
        fightResult = None
        opponentCreature=self.findCreature(newRowIndex,newColumnIndex) # It finds the enemy creature
        if opponentCreature is not None: # there is a fight
            fightResult = currentCreature.fight(opponentCreature)
            if (fightResult == FIGHTRESULT.WON):
                # TODO: when no opponent creature exist, same things are done. Code will be reduce later!
                # current creature moves  from current location to the new location
                self.removeCreature(currentRowIndex, currentColumnIndex)
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
                # opponent creature is automatically removed from the new location
                # when current creature is added to the new location.
            elif (fightResult == FIGHTRESULT.LOST):
                # current creature loses and dies so it is removed from the current location
                self.removeCreature(currentRowIndex, currentColumnIndex)
            else:  # fightResult  == 0 --->  replace the creatures' position
                # there is no fight.
                assert fightResult == FIGHTRESULT.SCORELESS, "Invalid fight result!"
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
                self.addCreature(currentRowIndex, currentColumnIndex, opponentCreature)
        else:  # there is no fight.
            # current creature moves  from current location to the new location
            # TODO: when current creature wins the fight, same things are done. Code will be reduce later!
            self.removeCreature(currentRowIndex, currentColumnIndex)
            self.addCreature(newRowIndex, newColumnIndex, currentCreature)
            fightResult = FIGHTRESULT.NOENEMY # it updates the fight result
        newCoordinates=(newRowIndex,newColumnIndex)
        fightInfo=FightInfo(opponentCreature, fightResult,newCoordinates)
        return fightInfo



    def moveCreature(self, rowIndex, columnIndex, moveTypeString):
        """
        It moves the creature from one location to another in the wild forest based on the move type \n
        :param rowIndex:
        :param columnIndex:
        :param moveTypeString:
        :return:
        """
        # rowIndex is a  y-coordinate, columnIndex is a x-coordinate
        newLocations= move(columnIndex, rowIndex, moveTypeString)
        newRowIndex=newLocations[1] # rowIndex is a  y-coordinate
        newColumnIndex=newLocations[0] # columnIndex is a x-coordinate
        if not (self.__areIndexesValid(newRowIndex, newColumnIndex)):
            raise Exception("New locations are not valid  based on the movement. Move operation is cancelled! ")
            # TODO: custom exception will be used
        else:
            fightInfo=self.__moveOperation(rowIndex, columnIndex, newRowIndex, newColumnIndex)
            return fightInfo


#WildForest testing
"""
wildForest=WildForest(2,3)
c1=Creature(50,20,"d")
c2=Creature(20,10,"d")
c3=Creature(30,10,"d")
c4=Creature(60,40,"d")
c5=Creature(50,30,"d")
wildForest.addCreature(0,0,c1)
wildForest.addCreature(0,1,c2)
wildForest.addCreature(0,2,c3)
wildForest.addCreature(1,0,c4)
wildForest.addCreature(1,1,c5)
wildForest.moveCreature(0,0,"s")
wildForest.moveCreature(0,1,"a")
wildForest.moveCreature(0,2,"a")
wildForest.moveCreature(1,1,"w")
n=wildForest.getNeighboringCells(1,1)
print("Worked!")

"""

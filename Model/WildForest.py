import copy

from Model.Creature import Creature
from Model.LocationMover import move,Movement
from Model.Cell import Cell
from Model.MoveInfo import FIGHTRESULT, MoveInfo


class WildForest:

    def __init__(self,rowSize,columnSize):
        assert rowSize >= 0, "row size can not be negative!"
        assert columnSize >= 0, "column size can not be negative!"
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__wildForestList = [[Cell() for j in range(columnSize)] for i in range(rowSize)] # initialize two-dimension empty array


    def getColumnSize(self):
        return self.__columnSize

    def getRowSize(self):
        return self.__rowSize

    def getWildForestList(self):
        return self.__wildForestList


    def getNeighboringCells(self,rowIndex,columnIndex):
        """
        It finds the non-empty neighboring cells of the current cell based on rowIndex and columndIndex

        :param rowIndex:
        :param columnIndex:
        :return:
        """
        neighborsIndex=[]
        neighboringCells=[]
        # rowIndex is a  y-coordinate, columnIndex is a x-coordinate
        # we check every movement direction of the current indexes
        neighborsIndex.append(move(columnIndex,rowIndex,Movement.Right))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Left))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Up))
        neighborsIndex.append(move(columnIndex, rowIndex, Movement.Down))
        copyNeighborsIndex=copy.deepcopy(neighborsIndex)
        for neighbor in copyNeighborsIndex:
            newRowIndex=neighbor[1]
            newColumnIndex=neighbor[0]
            if not (self.__areIndexesValid(newRowIndex,newColumnIndex)):
                neighborsIndex.remove(neighbor)
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
            currentCell.setCreature(None) # cell is removed from the cell
            return True


    def __moveOperation(self, currentCreature, opponentCreature, rowIndex,
                        columnIndex, newRowIndex, newColumnIndex):
        assert currentCreature is not None, "current creature can not be None!"
        moveInfo = None
        fightResult = None
        if opponentCreature is not None:
            fightResult = currentCreature.fight(opponentCreature)
            if (fightResult == FIGHTRESULT.WON):
                self.removeCreature(rowIndex, columnIndex)
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
            elif (fightResult == FIGHTRESULT.LOST):
                self.removeCreature(rowIndex, columnIndex)
            else:  # fightResult  == 0 --->  replace the creatures' position
                assert fightResult == FIGHTRESULT.SCORELESS, "Invalid fight result!"
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
                self.addCreature(rowIndex, columnIndex, opponentCreature)
        else:
            self.removeCreature(rowIndex, columnIndex)
            self.addCreature(newRowIndex, newColumnIndex, currentCreature)
            fightResult = FIGHTRESULT.NOENEMY
        moveInfo=MoveInfo(opponentCreature, fightResult)
        return moveInfo



    def moveCreature(self,rowIndex,columnIndex,moveTypeString):
        currentCreature=self.findCreature(rowIndex,columnIndex)
        if (currentCreature is None):
            raise Exception("Creature is not found! Move operation cancelled!")
        # rowIndex is a  y-coordinate, columnIndex is a x-coordinate
        newLocations= move(columnIndex, rowIndex, moveTypeString)
        newRowIndex=newLocations[1]
        newColumnIndex=newLocations[0]
        if not (self.__areIndexesValid(newRowIndex, newColumnIndex)):
            raise Exception("New locations are not valid  based on the movement. Move operation is cancelled! ")
        else:
            opponentCreature=self.findCreature(newRowIndex,newColumnIndex)
            moveInfo=self.__moveOperation(currentCreature,opponentCreature,rowIndex,
                                    columnIndex,newRowIndex,newColumnIndex)
            return moveInfo




#WildForest testing

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

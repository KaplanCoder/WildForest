from Model.Cell import Cell
from Model.Creature import Creature
from Model.WildForest import WildForest


class WildForestView:

     # TODO: attributes of a class can be changed later. is it a  good approach?

    __wildForestDelimeter = "" # not used for now

    __cellDelimeter = " "

    __cellFillingString = " "

    __cellStringLength = 20

    def __init__(self, wildForest:WildForest):
       self.__wildForest=wildForest


    def getWildForest(self):
        return self.__wildForest


    def getStringFormatOfNeighboringCells(self, rowIndex, columnIndex):
        """
        It returns neighboring cells of the current cell based on the rowIndex and columnIndex
        :param rowIndex:
        :param columnIndex:
        :return: neighboring cells as string format
        """
        infoString=""
        neighboringCells=self.__wildForest.getNeighboringCells(rowIndex, columnIndex)
        for neighboringCell in neighboringCells:
            currentCreature=neighboringCell.getCreature()
            infoString += "there is a " + str(currentCreature) + " nearby! \n"
        return infoString


    def getStringFormatOfCell(self, cell):
        assert isinstance(cell, Cell), "Cell object's type is not valid. Program is terminated"
        cellString= str(cell)
        remainingLength= self.__cellStringLength - len(cellString)
        if (remainingLength <= 0):
            cellString = cellString[:self.__cellStringLength]
        else:
            cellString = cellString + (remainingLength * self.__cellFillingString)
        return self.__cellDelimeter + cellString + self.__cellDelimeter


    def  getStringFormatOfWildForest(self):
        stringFormat=""
        rowSize=self.__wildForest.getRowSize()
        columnSize=self.__wildForest.getColumnSize()
        for row in range(rowSize):
            for column in range(columnSize):
                currentCell=self.__wildForest.getCell(row,column)
                stringFormat += self.getStringFormatOfCell(currentCell) + self.__wildForestDelimeter
            stringFormat += "\n"
        return stringFormat



"""testing
wildForest=WildForest(5, 5)
c1=Creature(20,30,"Monster")
c2=Creature(20,30,"Person")
wildForest.addCreature(0,1,c1)
wildForest.addCreature(1,0,c2)
view=WildForestView(wildForest)
print(view.getStringFormatOfWildForest())
print(view.getStringFormatOfNeighboringCells(1, 1))
"""
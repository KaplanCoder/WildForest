from Model.Cell import Cell
from Model.Creature import Creature
from Model.WildForest import WildForest


class WildForestView:

    __rowDelimeter = "-"

    __columnDelimeter = "|"

    __rowDelimeterLength = 10

    __columnDelimeterLength = 5

    __cellStringLength = 10

    @classmethod
    def getStringFormatOfCell(cls, cell , isDelimeterAllowed= True):
        assert isinstance(cell, Cell), "Cell object's type is not valid. Program is terminated"
        cellString= str(cell)
        remainingLength= cls.__cellStringLength - len(cellString)
        if (remainingLength <= 0):
            cellString = cellString[:cls.__cellStringLength]
        elif (isDelimeterAllowed):
            cellString = cellString + (remainingLength * cls.__rowDelimeter)
        return cellString


    @classmethod
    def  getStringFormatOfWildForest(cls,wildForest):
        stringFormat=""
        rowSize=wildForest.getRowSize()
        columnSize=wildForest.getColumnSize()
        for row in range(rowSize):
            for column in range(columnSize):
                currentCell=wildForest.getCell(row,column)
                stringFormat += cls.getStringFormatOfCell(currentCell) + cls.__cellDelimeter
            stringFormat += "\n"

        return stringFormat



"""testing
wildForest=WildForest(5, 5)
c1=Creature(20,30,"Monster")
c2=Creature(20,30,"Person")
wildForest.addCreature(0,1,c1)
wildForest.addCreature(1,0,c2)
print(WildForestView.getStringFormatOfWildForest(wildForest))
"""
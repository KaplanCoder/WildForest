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
    def __getColumnDelimeterLine(cls,columnSize):
        columnDelimeterLineSize= ((columnSize - 1 ) * cls.__rowDelimeterLength) \
                                 + (columnSize *  cls.__cellStringLength)
        columnDelimeterLine=" " * columnDelimeterLineSize
        delimeterLineList=list(columnDelimeterLine)
        delimeterLineLength=len(delimeterLineList)
        currentIndex= 0
        while (currentIndex < delimeterLineLength):
            delimeterLineList[currentIndex] = cls.__columnDelimeter
            currentIndex += cls.__rowDelimeterLength + cls.__cellStringLength
        columnDelimeterLine = "".join(delimeterLineList)
        columnDelimeterLine += "\n"
        columnDelimeterLine = columnDelimeterLine * cls.__columnDelimeterLength
        return columnDelimeterLine




    @classmethod
    def  getStringFormatOfWildForest(cls,wildForest):
        stringFormat=""
        rowSize=wildForest.getRowSize()
        columnSize=wildForest.getColumnSize()
        columnDelimeterLine = cls.__getColumnDelimeterLine(columnSize)
        for rowIndex in range(rowSize):
            cellDelimeter=cls.__rowDelimeter * cls.__rowDelimeterLength
            isDelimeterAllowed = True
            for columnIndex in range(columnSize):
                currentCell=wildForest.getCell(rowIndex,columnIndex)
                if (columnIndex == columnSize - 1): # if current cell is a last cell, delimeter wil not be added
                    isDelimeterAllowed=False
                    cellDelimeter=""
                stringFormat += cls.getStringFormatOfCell(currentCell,isDelimeterAllowed)
                stringFormat += cellDelimeter
            stringFormat += "\n"
            stringFormat = stringFormat + columnDelimeterLine if (rowIndex != rowSize - 1) else stringFormat

        return stringFormat



"""testing
wildForest=WildForest(5, 5)
c1=Creature(20,30,"Monster")
c2=Creature(20,30,"Person")
wildForest.addCreature(0,1,c1)
wildForest.addCreature(1,0,c2)
print(WildForestView.getStringFormatOfWildForest(wildForest))
"""
from Model.Cell import Cell
from Model.Creature import Creature
from Model.WildForest import WildForest


class WildForestView:

    __rowDelimiter = "-"  # delimiter between the cells in a row

    __columnDelimiter = "|" # delimiter between the cells in a column

    __rowDelimiterLength = 10

    __columnDelimiterLineSize = 5 # not column delimiter length, but number of lines using the column delimiter !!!

    __cellDefaultLength = 12

    @classmethod
    def getStringFormatOfCell(cls, cell, isRowDelimiterAllowed= True):
        """
         It returns the cell as a string format. \n
         If cell string length is smaller than the default length and row delimiter is allowed \n
        then row delimiter is added to  end of the string to reach the default length\n
        :param cell: Cell object
        :param isRowDelimiterAllowed:
        :return:
        """
        assert isinstance(cell, Cell), "Cell object's type is not valid. Program is terminated"
        cellString= str(cell)
        remainingLength= cls.__cellDefaultLength - len(cellString)
        if (remainingLength <= 0):
            cellString = cellString[:cls.__cellDefaultLength]
        elif (isRowDelimiterAllowed):
            cellString = cellString + (remainingLength * cls.__rowDelimiter)
        return cellString


    @classmethod
    def __getColumnDelimiterLine(cls,columnSize):
        """
        It creates the delimiter line to seperate the cells based on the column.
        :param columnSize: number of cells(columns) per row
        :return:
        """
        columnDelimiterLineSize= ((columnSize - 1 ) * cls.__rowDelimiterLength) \
                                 + (columnSize * cls.__cellDefaultLength)
        columnDelimiterLine=" " * columnDelimiterLineSize # empty delimiter line
        # to parse the string, it is converted to the list
        delimeterLineList=list(columnDelimiterLine)
        delimeterLineLength=len(delimeterLineList)
        currentIndex= 0
        while (currentIndex < delimeterLineLength):
            delimeterLineList[currentIndex] = cls.__columnDelimiter
            currentIndex += cls.__rowDelimiterLength + cls.__cellDefaultLength
        columnDelimiterLine = "".join(delimeterLineList) # convert the list back to string
        columnDelimiterLine += "\n"
        columnDelimiterLine = columnDelimiterLine * cls.__columnDelimiterLineSize
        return columnDelimiterLine




    @classmethod
    def  getStringFormatOfWildForest(cls,wildForest):
        """
        It returns the wild forest as a string format
        :param wildForest:
        :return:
        """
        stringFormat=""
        rowSize=wildForest.getRowSize()
        columnSize=wildForest.getColumnSize()
        columnDelimiterLine = cls.__getColumnDelimiterLine(columnSize)
        for rowIndex in range(rowSize):
            cellDelimiter=cls.__rowDelimiter * cls.__rowDelimiterLength
            isRowDelimiterAllowed = True
            for columnIndex in range(columnSize):
                currentCell=wildForest.getCell(rowIndex,columnIndex)
                if (columnIndex == columnSize - 1): # if current cell is a last cell, delimiter wil not be added
                    isRowDelimiterAllowed=False
                    cellDelimiter=""
                stringFormat += cls.getStringFormatOfCell(currentCell,isRowDelimiterAllowed)
                stringFormat += cellDelimiter
            stringFormat += "\n"
            # if current line is  a last line, column delimiter line will not be added
            stringFormat = stringFormat + columnDelimiterLine if (rowIndex != rowSize - 1) else stringFormat

        return stringFormat



"""testing
wildForest=WildForest(5, 5)
c1=Creature(20,30,"Monster")
c2=Creature(20,30,"Person")
wildForest.addCreature(0,1,c1)
wildForest.addCreature(1,0,c2)
print(WildForestView.getStringFormatOfWildForest(wildForest))
"""
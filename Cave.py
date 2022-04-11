from Creature import Creature


class Cave:

    __emptyObject=None

    def __init__(self,rowSize,columnSize):
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__caveList = [[self.__emptyObject for j in range(columnSize)] for i in range(rowSize)] # initialize two-dimension empty array

    def getColumnSize(self):
        return self.__columnSize

    def getRowSize(self):
        return self.__rowSize

    def getCaveList(self):
        return self.__caveList

    def areIndexesValid(self,rowIndex, columnIndex):
        length=len(self.getCaveList())
        if (rowIndex >= length or (rowIndex < 0)):
            return False
        if (columnIndex >= length or (columnIndex < 0)):
            return False
        return True

    def findCreature(self, rowIndex,columnIndex):
        caveList = self.getCaveList()
        if (self.areIndexesValid(rowIndex, columnIndex)):
            return caveList[rowIndex][columnIndex]
        return None


    def addCreature(self, creature, rowIndex, columnIndex):
        assert isinstance(creature, Creature), "Creature object's type is not valid. Program is terminated!"
        if not (self.areIndexesValid(rowIndex,columnIndex)):
            return False
        caveList = self.getCaveList()
        caveList[rowIndex][columnIndex]= creature # TODO: warning occured. will be checked latter
        return True

    def removeCreature(self, rowIndex, columnIndex):
        caveList = self.getCaveList()
        if not  (self.areIndexesValid(rowIndex, columnIndex)):
            return False
        else:
            caveList[rowIndex][columnIndex]=self.__emptyObject
            return True

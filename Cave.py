import CaveObject


class Cave:


    def __init__(self,rowSize,columnSize):
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__caveList = [[None for j in range(columnSize)] for i in range(rowSize)] # initialize two-dimension empty array


    def getCaveList(self):
        return self.__caveList

    def areIndexesValid(self,rowIndex, columnIndex):
        length=len(self.getCaveList())
        if (rowIndex >= length or (rowIndex < 0)):
            return False
        if (columnIndex >= length or (columnIndex < 0)):
            return False
        return True

    def getCaveObject(self,index):
        caveList = self.getCaveList()
        self.areIndexesValid(index, caveList, )
        return caveList[index]


    def addCaveObject(self, caveObject,rowIndex,columnIndex):
        if not (isinstance(caveObject,CaveObject)):
            return False
        if not (self.areIndexesValid(rowIndex,columnIndex)):
            return False
        caveList = self.getCaveList()
        caveList[rowIndex][columnIndex]=caveObject
        return True

    def removeCaveObject(self,rowIndex,columnIndex):
        caveList = self.getCaveList()
        if not  (self.areIndexesValid(rowIndex, columnIndex)):
            return False
        else:
            caveList[rowIndex][columnIndex]=None
            return True

    def print(self):
        pass # TODO: print function will be added






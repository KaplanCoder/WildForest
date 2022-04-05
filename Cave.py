import CaveObject


class Cave:


    def __init__(self,rowSize,columnSize):
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__caveList = [["0" for j in range(columnSize)] for i in range(rowSize)] # initialize two-dimension empty array


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
            self.__caveList[rowIndex][columnIndex]=0 # can be used "None" instead of 0 value
            return True

    def print(self):
        pass # TODO: print function will be added






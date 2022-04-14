from Creature import Creature
import LocationMover

class WildForest:

    __emptyObject=None

    def __init__(self,rowSize,columnSize):
        assert rowSize >= 0, "row size can not be negative!"
        assert columnSize >= 0, "column size can not be negative!"
        self.__rowSize=rowSize
        self.__columnSize=columnSize
        self.__wildForestList = [[self.__emptyObject for j in range(columnSize)] for i in range(rowSize)] # initialize two-dimension empty array


    def getColumnSize(self):
        return self.__columnSize

    def getRowSize(self):
        return self.__rowSize

    def getWildForestList(self):
        return self.__wildForestList

    def areIndexesValid(self,rowIndex, columnIndex):
        if (rowIndex >= self.getRowSize() or (rowIndex < 0)):
            return False
        if (columnIndex >= self.getColumnSize() or (columnIndex < 0)):
            return False
        return True

    def findCreature(self, rowIndex,columnIndex):
        wildForestList = self.getWildForestList()
        if (self.areIndexesValid(rowIndex, columnIndex)):
            return wildForestList[rowIndex][columnIndex]
        return None


    def addCreature(self,rowIndex, columnIndex,creature):
        assert isinstance(creature, Creature), "Creature object's type is not valid. Program is terminated!"
        if not (self.areIndexesValid(rowIndex,columnIndex)):
            return False
        wildForestList = self.getWildForestList()
        wildForestList[rowIndex][columnIndex]= creature # TODO: warning occured. will be checked latter
        return True

    def removeCreature(self, rowIndex, columnIndex):
        wildForestList = self.getWildForestList()
        if not  (self.areIndexesValid(rowIndex, columnIndex)):
            return False
        else:
            wildForestList[rowIndex][columnIndex]=self.__emptyObject
            return True


    def __moveOperation(self,currentCreature,anotherCreature,rowIndex,
                        columnIndex,newRowIndex,newColumnIndex):
        assert currentCreature is not None, "current creature can not be None!"
        moveResult = None
        if anotherCreature is not None:
            fightResult = currentCreature.fight(anotherCreature)
            if (fightResult == 1):
                self.removeCreature(rowIndex, columnIndex)
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
            elif (fightResult == -1):
                self.removeCreature(rowIndex, columnIndex)
            else:  # fightResult  == 0 --->  replace the creatures
                self.addCreature(newRowIndex, newColumnIndex, currentCreature)
                self.addCreature(rowIndex, columnIndex, anotherCreature)
            moveResult = fightResult
        else:
            self.removeCreature(rowIndex, columnIndex)
            self.addCreature(newRowIndex, newColumnIndex, currentCreature)
            moveResult = 1
        return moveResult



    def moveCreature(self,rowIndex,columnIndex,moveTypeString):
        currentCreature=self.findCreature(rowIndex,columnIndex)
        if (currentCreature is None):
            raise Exception("Creature is not found! Move operation cancelled!")
        # rowIndex is a  y-coordinate, columnIndex is a x-coordinate
        newLocations=LocationMover.move(columnIndex,rowIndex,moveTypeString)
        newRowIndex=newLocations[1]
        newColumnIndex=newLocations[0]
        if not (self.areIndexesValid(newRowIndex,newColumnIndex)):
            raise Exception("New locations are not valid  based on the movement. Move operation is cancelled! ")
        else:
            anotherCreature=self.findCreature(newRowIndex,newColumnIndex)
        return self.__moveOperation(currentCreature,anotherCreature,rowIndex,
                                    columnIndex,newRowIndex,newColumnIndex)




"""WildForest testing

wildForest=WildForest(2,3)
c1=Creature(50,20)
c2=Creature(20,10)
c3=Creature(30,10)
c4=Creature(60,40)
c5=Creature(50,30)
wildForest.addCreature(0,0,c1)
wildForest.addCreature(0,1,c2)
wildForest.addCreature(0,2,c3)
wildForest.addCreature(1,0,c4)
wildForest.addCreature(1,1,c5)
wildForest.moveCreature(0,0,"s")
wildForest.moveCreature(0,1,"a")
wildForest.moveCreature(0,2,"a")
wildForest.moveCreature(1,1,"w")
wildForest.moveCreature(0,0,"d")
wildForest.moveCreature(0,0,"s")
wildForest.moveCreature(-1,0,"s")
print("Worked!")

"""
from Cave import Cave
from Creature import Creature


class CaveView:
     # TODO: attributes of a class can be changed later. is it a  good approach?
    __caveDelimeter = "-" * 5

    __creatureDelimeter = " " * 5

    __emptyCreatureString = "Empty"

    __creatureFillingString = " "

    __creatureStringLength = 10

    def __init__(self,cave:Cave):
       self.__cave=cave

    def getCave(self):
        return self.__cave

    def getStringFormatOfCreature(self, creature):
        creatureString=self.__emptyCreatureString
        if (creature is not None):
            assert isinstance(creature, Creature), "Creature object's type is not valid. Program is terminated"
            creatureString= creature.getStringFormat()
        remainingLength=self.__creatureStringLength - len(creatureString)
        if (remainingLength <= 0):
            creatureString = creatureString[:self.__creatureStringLength]
        else:
            creatureString = creatureString + (remainingLength * self.__creatureFillingString)
        return self.__creatureDelimeter + creatureString + self.__creatureDelimeter


    def  getStringFormatOfCave(self):
        cave=self.getCave()
        stringFormat=""
        rowSize=cave.getRowSize()
        columnSize=cave.getColumnSize()
        caveList=cave.getCaveList()
        for row in range(rowSize):
            for column in range(columnSize):
                currentCreature=caveList[row][column]
                stringFormat += self.getStringFormatOfCreature(currentCreature)  + self.__caveDelimeter
            stringFormat += "\n"
        return stringFormat


cave=Cave(4,5)
c1=Creature(2,3)
cave.addCreature(c1,3,1)
view=CaveView(cave)
print(view.getStringFormatOfCave())
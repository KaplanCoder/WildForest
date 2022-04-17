from Model.WildForest import WildForest
from Model.Creature import Creature


class WildForestView:

     # TODO: attributes of a class can be changed later. is it a  good approach?

    __wildForestDelimeter = "" # not used for now

    __creatureDelimeter = " "

    __emptyCreatureString = "Safe"  # it means safe

    __creatureFillingString = " "

    __creatureStringLength = 10

    def __init__(self, wildForest:WildForest):
       self.__wildForest=wildForest

    def getWildForest(self):
        return self.__wildForest

    def getStringFormatOfCreature(self, creature):
        creatureString=self.__emptyCreatureString
        if (creature is not None):
            assert isinstance(creature, Creature), "Creature object's type is not valid. Program is terminated"
            creatureString= creature.getViewFormat()
        remainingLength=self.__creatureStringLength - len(creatureString)
        if (remainingLength <= 0):
            creatureString = creatureString[:self.__creatureStringLength]
        else:
            creatureString = creatureString + (remainingLength * self.__creatureFillingString)
        return self.__creatureDelimeter + creatureString + self.__creatureDelimeter


    def  getStringFormatOfWildForest(self):
        wildForest=self.getWildForest()
        stringFormat=""
        rowSize=wildForest.getRowSize()
        columnSize=wildForest.getColumnSize()
        wildForestList=wildForest.getWildForestList()
        for row in range(rowSize):
            for column in range(columnSize):
                currentCreature=wildForestList[row][column]
                stringFormat += self.getStringFormatOfCreature(currentCreature)  + self.__wildForestDelimeter
            stringFormat += "\n"
        return stringFormat


wildForest=WildForest(5, 5)
c1=Creature(2,3,"Monster")
c2=Creature(2,3,"Person")
wildForest.addCreature(3,1,c1)
wildForest.addCreature(4,2,c2)
view=WildForestView(wildForest)
print(view.getStringFormatOfWildForest())
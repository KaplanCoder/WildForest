from Model.Creature import Creature

class Cell:

    __emptyStringFormat= "Safe"

    def __init__(self, creature = None):
        self.__creature=creature
        self.__isViewAllowed=False

    def setCreature(self,newCreature):
        self.__creature=newCreature

    def getCreature(self):
        return self.__creature

    def isEmpty(self):
        return (self.__creature is None)

    def makeVisible(self):
        self.__isViewAllowed=True

    def makeInvisible(self):
        self.__isViewAllowed=False

    def __str__(self):
        stringFormat=self.__emptyStringFormat if (self.__creature is None) else self.__creature.getName()
        return stringFormat if self.__isViewAllowed else "Unknown"

"""
Testing
c1=Cell(Creature(40,50,"Example"))
print(c1.isEmpty())
c1.setCreature(None)
print(c1.isEmpty())

"""
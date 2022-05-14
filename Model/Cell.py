from Model.Creature import Creature

class Cell:

    __defaultView="Empty" # if there is no creature in the cell, the default view will be shown

    def __init__(self, creature = None):
        self.__creature=creature
        self.__isViewAllowed=False


    def setDefaultView(self,newView):
        self.__defaultView=newView


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
        stringFormat=self.__defaultView if (self.__creature is None) else self.__creature.getName()
        return stringFormat if self.__isViewAllowed else "Unknown"

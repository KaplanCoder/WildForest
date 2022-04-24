

class Cell:

    __emptyStringFormat= "Safe"

    def __init__(self, creature = None):
        self.__creature=creature
        self.__isViewAllowed=False

    def setCreature(self,newCreature):
        self.__creature=newCreature

    def getCreature(self):
        return self.__creature

    def makeVisible(self):
        self.__isViewAllowed=True

    def makeInvisible(self):
        self.__isViewAllowed=False

    def __str__(self):
        stringFormat=self.__emptyStringFormat if (self.__creature is None) else str(self.__creature)
        return stringFormat if self.__isViewAllowed else "Unknown"


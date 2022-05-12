
from Model.FightInfo import FIGHTRESULT


class Creature:

    def __init__(self,health,point,name):
        assert isinstance(name,str),"name must be string"
        assert point >= 0, "creature's point can not be negative!"
        assert health >= 0, "creature's health can not be negative!"
        self.__health = health
        self.__point = point
        self.__name = name

    def setName(self,newName):
        self.__name=newName


    def getName(self):
        return self.__name

    def isAlive(self):
        return (self.__health > 0)

    def setPoint(self,newPoint):
        self.__point=newPoint

    def getPoint(self):
        return self.__point

    def setHealth(self,newHealth):
        self.__health = newHealth

    def getHealth(self):
        return self.__health

    def fight(self, anotherCreature):
        """
        Todo: fight will be explained
        :param anotherCreature:
        :return:
        """
        assert isinstance(anotherCreature, Creature), "Creature object's type is not valid. Program is terminated!"
        anotherObjectHealth=anotherCreature.getHealth()
        currentHealth=self.getHealth()
        currentPoint = self.getPoint()
        anotherObjectPoint = anotherCreature.getPoint()
        if (currentHealth  > anotherObjectHealth):
            self.setPoint(currentPoint + anotherObjectPoint)
            self.setHealth(currentHealth - anotherObjectHealth)
            anotherCreature.setHealth(0) # It means that  another creature is death.
            return FIGHTRESULT.WON
        elif (currentHealth < anotherObjectHealth):
            anotherCreature.setPoint(currentPoint + anotherObjectPoint)
            anotherCreature.setHealth(anotherObjectHealth - currentHealth)
            self.setHealth(0) # It means that  current creature is death.
            return FIGHTRESULT.LOST
        else: # currentHealth == anotherObjectHealth
            # two creatures neither gain points nor lose  health.
            return FIGHTRESULT.SCORELESS


    def __str__(self):
        return f'{self.__name} (Health:{self.__health},Point:{self.__point})'

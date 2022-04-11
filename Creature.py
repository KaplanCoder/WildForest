
class Creature:

    def __init__(self,health,point):
        assert health >= 0, "creature's health can not be negative!"
        assert self.__health >= 0, "creature's point can not be negative!"
        self.__health=health
        self.__point=point

    def setPoint(self,newPoint):
        self.__point=newPoint

    def getPoint(self):
        return self.__point

    def setHealth(self,newHealth):
        self.__health=newHealth

    def getHealth(self):
        return self.__health

    def encounter(self, anotherCreature):
        assert isinstance(anotherCreature, Creature), "Creature object's type is not valid. Program is terminated!"
        anotherObjectHealth=anotherCreature.getHealth()
        currentHealth=self.getHealth()
        currentPoint = self.getPoint()
        anotherObjectPoint = anotherCreature.getPoint()
        if (currentHealth  > anotherObjectHealth):
            self.setPoint(currentPoint + anotherObjectPoint)
            self.setHealth(currentHealth - anotherObjectHealth)
            anotherObjectHealth.setHealth(0) # # It means that  another creature is death.
        elif (currentHealth < anotherObjectHealth):
            anotherCreature.setPoint(currentPoint + anotherObjectPoint)
            anotherObjectHealth.setHealth(anotherObjectHealth - currentHealth)
            self.setHealth(0) # It means that  current creature is death.

    def getStringFormat(self): # TODO: is it necessary? Will be checked later
       return f"(Health:{self.getHealth()},Point:{self.getPoint()})"


class Creature:

    def __init__(self,health,point):
        assert health >= 0, "creature's health can not be negative!" # Todo: bug will be fixed later
        assert self.__health >= 0, "creature's point can not be negative!"
        self.__health=health
        self.__point=point

    def isAlive(self):
        return (self.__health > 0)

    def setPoint(self,newPoint):
        self.__point=newPoint

    def getPoint(self):
        return self.__point

    def setHealth(self,newHealth):
        self.__health=newHealth

    def getHealth(self):
        return self.__health

    def fight(self, anotherCreature):
        """
        :param anotherCreature:
        :return: it returns true if current creature wins the fight, otherwise it returns false
        """
        assert isinstance(anotherCreature, Creature), "Creature object's type is not valid. Program is terminated!"
        anotherObjectHealth=anotherCreature.getHealth()
        currentHealth=self.getHealth()
        currentPoint = self.getPoint()
        anotherObjectPoint = anotherCreature.getPoint()
        if (currentHealth  > anotherObjectHealth):
            self.setPoint(currentPoint + anotherObjectPoint)
            self.setHealth(currentHealth - anotherObjectHealth)
            anotherObjectHealth.setHealth(0) # It means that  another creature is death.
            return True
        elif (currentHealth < anotherObjectHealth):
            anotherCreature.setPoint(currentPoint + anotherObjectPoint)
            anotherObjectHealth.setHealth(anotherObjectHealth - currentHealth)
            self.setHealth(0) # It means that  current creature is death.
            return False
        else: # currentHealth == anotherObjectHealth
            # two creatures neither gain points nor lose  health.
            return False

    def getStringFormat(self): # TODO: is it necessary? Will be checked later
       return f"(Health:{self.getHealth()},Point:{self.getPoint()})"

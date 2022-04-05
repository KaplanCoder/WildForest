
class Creature:

    def __init__(self,power,point):
        self.__power=power
        self.__point=point

    def setPoint(self,newPoint):
        self.__point=newPoint

    def getPoint(self):
        return self.__point

    def setPower(self,newPower):
        self.__power=newPower

    def getPower(self):
        return self.__power

    def encounter(self, anotherCreature):
        assert isinstance(anotherCreature, Creature), "Creature object's type is not valid. Program is terminated!"
        anotherObjectPower=anotherCreature.getPower()
        currentPower=self.getPower()
        currentPoint = self.getPoint()
        anotherObjectPoint = anotherCreature.getPoint()
        if (currentPower  > anotherObjectPower):
            self.setPoint(currentPoint + anotherObjectPoint)
        elif (currentPower < anotherObjectPower):
            anotherCreature.setPoint(currentPoint + anotherObjectPoint)

    def getStringFormat(self): # TODO: is it necessary? Will be checked later
       return f"(Power:{self.getPower()},Point:{self.getPoint()})"

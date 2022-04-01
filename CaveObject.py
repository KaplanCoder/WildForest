
class CaveObject:

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

    def encounter(self,anotherCaveObject):
        assert isinstance(anotherCaveObject,CaveObject), "Cave object's type is not valid. Program is terminated!"
        anotherObjectPower=anotherCaveObject.getPower()
        currentPower=self.getPower()
        currentPoint = self.getPoint()
        anotherObjectPoint = anotherCaveObject.getPoint()
        if (currentPower  > anotherObjectPower):
            self.setPower(currentPoint + anotherObjectPoint)
        elif (currentPower < anotherObjectPower):
            anotherCaveObject.setPoint(currentPoint + anotherObjectPoint)
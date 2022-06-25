

from model.Creature import Creature
from model.WildForest import WildForest
import random
import itertools
from externalLibraries.FileHandler import FileHandler

class WildForestFactory:

    def __init__(self,wildForestJsonFileName):
        wildForestJsonString=FileHandler.readJsonFromFile(wildForestJsonFileName)
        self.__wildForest=self.__createWildForestFromJsonString(wildForestJsonString["wildForest"])
        self.__playerXcoordinate=-1 # initialize the attribute
        self.__playerYcoordinate=-1 # initialize the attribute
        self.__creatureToBeFound=None# initialize the attribute
        xcoordinates = [i for i in range(self.__wildForest.getRowSize())]
        ycoordinates = [i for i in range(self.__wildForest.getColumnSize())]
        self.__coordinatesProduct=list(itertools.product(xcoordinates,ycoordinates)) # possible coordinates for wild forest
        self.__addCreaturesToWildForest(wildForestJsonString["creatures"])


    def getWildForest(self):
        return self.__wildForest

    def getPlayerXcoordinate(self):
        return self.__playerXcoordinate

    def getPlayerYcoordinate(self):
        return self.__playerYcoordinate

    def getCreatureToBeFound(self):
        return self.__creatureToBeFound


    @classmethod
    def __createCreatureFromJsonString(cls,creatureJsonString):
        # Todo: jsonString's attributes are static. Is it a good approach?
        creatureName=creatureJsonString["name"]
        creatureHealth=creatureJsonString["health"]
        creaturePoint=creatureJsonString["point"]
        return Creature(creatureHealth,creaturePoint,creatureName)


    def __addCreatureToWildForest(self,wildForest,creatureJsonString):
        newCreature = self.__createCreatureFromJsonString(creatureJsonString)
        xCoordinate=creatureJsonString.get("xCoordinate",-1) # if key not found,returns -1
        yCoordinate = creatureJsonString.get("yCoordinate", -1) # if key not found,returns -1
        coordinates=(xCoordinate,yCoordinate)
        if (xCoordinate == -1) or (yCoordinate == -1): # if coordinates are not given
            coordinates=random.choice(self.__coordinatesProduct) # coordinates will be chosed randomly from coordinates list.
            #Todo: assertion will be added to make sure that coordinates have two elements
            xCoordinate=coordinates[0]
            yCoordinate=coordinates[1]
        isPlayer = creatureJsonString.get("isPlayer", False) # if attribute not found,return false
        isToBeFound=creatureJsonString.get("isToBeFound", False) # if attribute not found,return false
        if (isPlayer):
            self.__playerXcoordinate=xCoordinate
            self.__playerYcoordinate=yCoordinate
        elif (isToBeFound):
            self.__creatureToBeFound=newCreature
        # Todo: player and creature to be found can not be same. Assertion may be added later.
        wildForest.addCreature(xCoordinate,yCoordinate,newCreature)
        self.__coordinatesProduct.remove(coordinates) # chosen coordinates are removed from the coordinates list



    def __addCreaturesToWildForest(self,creaturesJsonString):
        for creatureJson in creaturesJsonString:
            self.__addCreatureToWildForest(self.__wildForest,creatureJson)


    def __createWildForestFromJsonString(self,wildForestJsonString):
        rowSize=wildForestJsonString["rowSize"]
        columnSize=wildForestJsonString["columnSize"]
        return WildForest(rowSize,columnSize)




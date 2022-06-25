
import json


class FileHandler:


    @classmethod
    def readJsonFromFile(cls, fileName):
        with open(fileName,"r") as jsonFile:
            fileData=json.load(jsonFile)
            return fileData


    @classmethod
    def saveJSonToFile(self,jsonString,fileName):
        with open(fileName, "w") as jsonFile:
           json.dump(jsonString,jsonFile)
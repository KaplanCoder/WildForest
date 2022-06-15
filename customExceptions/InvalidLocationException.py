



class InvalidLocationException(Exception):

    def __init__(self,*args):
        self.__errorMessage=""
        if (args) :
            self.__errorMessage=args[0]

    def setErrorMessage(self,newErrorMessage):
        self.__errorMessage=newErrorMessage

    def __str__(self):
        if (len(self.__errorMessage) != 0):
            return self.__errorMessage
        return "Invalid Location error occured"
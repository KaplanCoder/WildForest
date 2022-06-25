
from model.LocationMover import Movement
from view.WildForestView import WildForestView
from model.WildForest import WildForest
from model.Creature import Creature

# Todo: it will print fight status after move operation of the wild forest

class WildForestMenuView:

    @classmethod
    def printHitWall(cls):
        print("You hit the wall. Try another move!")

    @classmethod
    def printSafeStatus(cls):
        print("You are in a safe room. Don’t worry!")

    @classmethod
    def printStepsTaken(cls,steps):
        print(f"Number of steps taken so far is {steps}")

    @classmethod
    def printWinGame(cls, name):
        print(f"Yay! You found the {name}!")
        print(f"Congratulations!!! You have won the game!")

    @classmethod
    def printScore(cls,score):
        print(f"Your score is = {score}")

    @classmethod
    def printLoseGame(cls):
        print("Sorry, You died! Game over!")

    @classmethod
    def printCreatureStatus(cls,creature):
        print(f"{creature.getName()}'s current health = {creature.getHealth()}")
        print(f"{creature.getName()}'s current point = {creature.getPoint()}")




    @classmethod
    def printWildForest(cls,wildForest):
        print(WildForestView.getStringFormatOfWildForest(wildForest))


    @classmethod
    def printCreaturesVoice(cls, cells, hiddenCreature):
        """
        :param cells:
        :param hiddenCreature: hidden creature's voice is not printed
        :return:
        """
        for currentCell in cells:
            assert not currentCell.isEmpty()," current cell can not be empty!"
            currentCreature=currentCell.getCreature()
            if (currentCreature is hiddenCreature):
                continue
            print(str(currentCreature) + " voice heard nearby!")

    @classmethod
    def printWelcomeMessage(cls):
        print("-" * 8) # Todo static number is used. Will be refactored later.
        print("Welcome to our WildForest game! \n"
              "In this game, you are a person who is trying to find his brother in the  wild forest \n"
              "There are dangerous monsters here. So,be careful! \n"
              "If you win the game, your score will be calculated as (100 / number of steps taken) \n"
              "If you die and lose the game, your score will be 0"
              )
        print("-" * 8) # Todo static number is used. Will be refactored later.

    @classmethod
    def printFight(cls,opponentCreature,):
        print(f"Opps! You have encountered the {opponentCreature.getName()}")
        print(f"You are fighting it right now...")

    @classmethod
    def printWinFight(cls,opponentCreature):
        print(f"Congratulations!! You have won the fight against {opponentCreature.getName()}! ")

    @classmethod
    def printLoseFight(cls,opponentCreature):
        print(f"Sorry! Unfortunately you have lost the fight against {opponentCreature.getName()}!")

    @classmethod
    def printFightScorelessStatus(cls,opponentCreature):
        print(f"Nobody won this fight! You and your opponent "
              f"that is {opponentCreature.getName()} whose places "  f"have been swapped!")

    @classmethod
    def getMoveFromTheUser(self):
        while (True):
            print("What is your move?")
            direction=input("Choose right (d), left (a), up (w) or down (s) : ")
            print() # added for new line
            if (isinstance(direction,str)):
               direction=direction.lower()
               enumList=[movementKey.value for movementKey in Movement]
               if (direction in enumList):
                    break # everything is ok
            print("There is no such direction! Choose right (d), left (a), up (w) or down (s).")
        return direction

""" Testing
wild=WildForest(3,3)
c1=Creature(20,30,"Bear")
c2=Creature(40,50,"Tiger")
wild.addCreature(0,1,c1)
wild.addCreature(1,2,c2)
WildForestMenuView.printNeighboringCreatures(wild,2,0)
"""
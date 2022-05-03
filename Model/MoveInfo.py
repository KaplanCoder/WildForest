

from enum import Enum

class FIGHTRESULT(Enum):
    # int values of enums  are not used for now
    WON = 1
    LOST = -1
    SCORELESS = 0
    NOENEMY = 2  # no enemies to fight


class MoveInfo:

    def __init__(self,enemyToFight,fightResult: FIGHTRESULT):
        if (enemyToFight is None):
            assert fightResult == FIGHTRESULT.NOENEMY,"If there is no enemy to fight, fight result must be 'NOENEMY'"
        self.__enemyToFight=enemyToFight
        self.__fightResult=fightResult

    def getFightResult(self):
        return self.__fightResult

    def getEnemy(self):
        return self.__enemyToFight
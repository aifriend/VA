from enum import Enum


class Environment(Enum):
    DEV = 0
    PRE_PRO = 1
    PRO = 2
    TEST = 3


class Config:
    ENV = Environment.DEV

    def isDev(self):
        return self.ENV == Environment.DEV

    def isPrePro(self):
        return self.ENV == Environment.PRE_PRO

    def isPro(self):
        return self.ENV == Environment.PRO

    def isTest(self):
        return self.ENV == Environment.TEST

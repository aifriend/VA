from enum import Enum


class Environment(Enum):
    DEV = 0
    PRE_PRO = 1
    PRO = 2
    TEST = 3


class Config:
    ENV = Environment.DEV

    if ENV == Environment.DEV:
        CONFIG_MODULE_ENDPOINT = 'http://127.0.0.1:9000/get_module_config'
        CONFIG_CONFIDENCE_ENDPOINT = 'http://127.0.0.1:9000/get_confidence_config'
    else:
        CONFIG_MODULE_ENDPOINT = 'http://configuration_service:9000/get_module_config'
        CONFIG_CONFIDENCE_ENDPOINT = 'http://configuration_service:9000/get_confidence_config'

    def isDev(self):
        return self.ENV == Environment.DEV

    def isPrePro(self):
        return self.ENV == Environment.PRE_PRO

    def isPro(self):
        return self.ENV == Environment.PRO

    def isTest(self):
        return self.ENV == Environment.TEST

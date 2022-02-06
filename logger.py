import logging
import sys

class Logger(object):

    """
        Static instance for Singleton

        :static:
        :type __instance: Logger
    """
    __instance = None

    def getInstance():
        """ 
            Static access method
        """
        if Logger.__instance == None:
            Logger()
        return Logger.__instance
   
    def __init__(self):
        """
            Virtually private constructor
        """
        if Logger.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self

    def loadLogger(self, appName : str = "WeatherApp", criticalFile : str = "./critical.log", infoFile : str = "./info.log", level : int = 20):
        """
            Loading loggers data

            :param appName: The name of the application
            :type appName: str
            :param criticalFile: Critical file full path (relative or absolute)
            :type criticalFile: str
            :param infoFile: Info file full path (relative or absolute)
            :type infoFile: str
            :param level: The level from logging
            :type level: int
        """
        self.__logger = logging.getLogger(appName)
        
        # Logs Formatting
        formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

        # Handler for messages (critical and errors in one file, info in another and eventually debug in the stdout)
        handler_critic = logging.FileHandler(criticalFile, mode="a", encoding="utf-8")
        handler_info = logging.FileHandler(infoFile, mode="a", encoding="utf-8")
        handler_debug = logging.StreamHandler(sys.stdout)

        # Setting the format for every handler
        handler_critic.setFormatter(formatter)
        handler_info.setFormatter(formatter)
        handler_debug.setFormatter(formatter)

        # Configuring the levels
        handler_debug.setLevel(logging.DEBUG)
        handler_info.setLevel(logging.INFO)
        handler_critic.setLevel(logging.CRITICAL)

        # Set the current level in conformity with the settings and add all handlers
        self.__logger.setLevel(level)
        self.__logger.addHandler(handler_critic)
        self.__logger.addHandler(handler_info)
        self.__logger.addHandler(handler_debug) # HACK : TO BE COMMENTED IN FINAL VERSION

import logging
import sys

class Logger(object):

    """
        Static instance for Singleton

        :meta static:
        :type __instance: Logger
    """
    __instance = None

    def getInstance():
        """ 
            Static access method

            :meta static:
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

    def debug(self, value : str) -> None:
        """
            Print in debug level

            :param value: The text to print
            :type value: str
        """
        self.__logger.debug(value)

    def info(self, value : str) -> None:
        """
            Print in info level

            :param value: The text to print
            :type value: str
        """
        self.__logger.info(value)

    def warning(self, value : str) -> None:
        """
            Print in warning level

            :param value: The text to print
            :type value: str
        """
        self.__logger.warning(value)
    
    def error(self, value : str) -> None:
        """
            Print in error level

            :param value: The text to print
            :type value: str
        """
        self.__logger.error(value)

    def critical(self, value : str) -> None:
        """
            Print in critical level

            :param value: The text to print
            :type value: str
        """
        self.__logger.critical(value)


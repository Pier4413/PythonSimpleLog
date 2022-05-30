import logging
import os
import sys

class Logger(object):
    """
        This class manage logs using a Singleton via three files critical, infos and sys.stdout

        :author: Panda <panda@delmasweb.net>
        :date: February 7, 2022
        :version: 1.0
    """

    """
        Static instance for Singleton

        :meta static:
        :type __instance: Logger
    """
    __instance = None

    def get_instance():
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
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self
            self.load_logger() # Load an empty logger in case we did load nothing
    
    def create_folders(self, filename : str) -> None:
        """
            Create the folder and all subfolders of the log file to avoid problems

            :param filename: The path of the file (relative or absolute)
            :type filename:
        """
        file_folders = filename.split("/")
        file_folder_path = ""

        for f in file_folders[:len(file_folders)-1]:
            file_folder_path = file_folder_path + f + "/"

        os.makedirs(os.path.join(file_folder_path), exist_ok=True)

    def load_logger(self, app_name : str = "", critical_file : str = None, info_file : str = None, console : bool = False, level : int = 20):
        """
            Loading loggers data

            :param appName: The name of the application
            :type appName: str
            :param criticalFile: Optional; Default : None; Critical file full path (relative or absolute). If None no crit file
            :type criticalFile: str
            :param infoFile: Optional; Default : None; Info file full path (relative or absolute). If None no info file
            :type infoFile: str
            :param console: Optional; Default : False; Print the logs in the console or not
            :type console: bool
            :param level: The level from logging
            :type level: int
        """
        self.__logger = logging.getLogger(app_name)
        self.__logger.setLevel(level)

        # Logs Formatting
        formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

        # Handler for messages (critical and errors in one file, info in another and eventually debug in the stdout)
        if(critical_file is not None):
            self.create_folders(critical_file)
            handler_critic = logging.FileHandler(critical_file, mode="a", encoding="utf-8")
            handler_critic.setFormatter(formatter)
            handler_critic.setLevel(logging.CRITICAL)
            self.__logger.addHandler(handler_critic)
        
        if(info_file is not None):
            self.create_folders(info_file)
            handler_info = logging.FileHandler(info_file, mode="a", encoding="utf-8")
            handler_info.setFormatter(formatter)
            handler_info.setLevel(logging.INFO)
            self.__logger.addHandler(handler_info)
        
        if(console is True):
            handler_debug = logging.StreamHandler(sys.stdout)
            handler_debug.setFormatter(formatter)
            handler_debug.setLevel(logging.DEBUG)
            self.__logger.addHandler(handler_debug)

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


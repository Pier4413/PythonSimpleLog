# PythonSimpleLog

This is a simple wrapper for logging that create a CRITICAL file, an INFO file and also print in the console (sys.stdout)

## To create a new logger

```
from <modules>.logger import Logger

app_name = "TEST" # The app name
critical_file = "./critical.log" # The path of the critical logging file (ERROR and CRITICAL)
info_file = "./info.log" # The path of the info logging file (INFO, WARN, ERROR and CRITICAL)
files_max_size = 1 # The files max size for the rotation in MB
backup_count = 10 # The number of files to keep for the rotation
console = True # Print to the console (DEBUG, INFO, WARN, ERROR and CRITICAL)
level = 10 # The level of the data to print

Logger.get_instance().load_logger(app_name, critical_file, info_file, files_max_size, backup_count, console, level) # Load the logger. You have to do it only once in your app
Logger.debug(cls, f"TEST") # Print a message in debug from the class cls (could be None if no class)
Logger.info(cls, f"TEST") # Print a message in info from the class cls (could be None if no class)
Logger.warning(cls, f"TEST") # Print a message in warning from the class cls (could be None if no class)
Logger.error(cls, f"TEST") # Print a message in error from the class cls (could be None if no class)
Logger.critical(cls, f"TEST") # Print a message in critical from the class cls (could be None if no class)
```

Please note this module depends on :

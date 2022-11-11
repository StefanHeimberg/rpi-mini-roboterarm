# Stefan Heimberg Tools
#
# Version 0.1
# Datum 14.11.2021
#

import utime
import _thread

LEVEL_OFF: int = 0
LEVEL_ERROR: int = 1
LEVEL_WARN: int = 2
LEVEL_INFO: int = 3
LEVEL_DEBUG: int = 4
LEVEL_TRACE: int = 5
LEVEL_ALL: int = 99

default_logging_level = LEVEL_OFF
logger_logging_level = {}

def setDefaultLoggingLevel(level: int):
    global default_logging_level
    default_logging_level = level
    
def setLoggingLevel(logger: str, level: int):
    global logger_logging_level
    logger_logging_level[logger] = level
    
def getLoggingLevel(logger: str):
    global logger_logging_level
    global default_logging_level
    if logger in logger_logging_level:
        return logger_logging_level[logger]
    else:
        return default_logging_level

class Logger:
    
    def __init__(self, name: str):
        self.__name = name

    def __levelName(self, level: int):
        nameMapping: dict = {
            LEVEL_OFF: 'OFF',
            LEVEL_ERROR: 'ERROR',
            LEVEL_WARN: 'WARN',
            LEVEL_INFO: 'INFO',
            LEVEL_DEBUG: 'DEBUG',
            LEVEL_TRACE: 'TRACE'
        }
        return nameMapping.get(level, 'UNKNOWN_' + str(level))

    def isLevelEnabled(self, level: int):
        return level <= getLoggingLevel(self.__name)

    def log(self, level: int, message: str):
        if self.isLevelEnabled(level=level):
            now = utime.ticks_ms()
            level = self.__levelName(level=level)
            thread = _thread.get_ident()
            print('{time} [{level: <5}] {thread} {name: <20} - {message}'.format(time=now, level=level, thread=thread, name=self.__name, message=message))

    def isErrorEnabled(self):
        global LEVEL_ERROR
        return self.isLevelEnabled(level=LEVEL_ERROR)
    
    def error(self, message: str):
        global LEVEL_ERROR
        if self.isErrorEnabled():
            self.log(level=LEVEL_ERROR, message=message)

    def isWarnEnabled(self):
        global LEVEL_WARN
        return self.isLevelEnabled(LEVEL_WARN)
    
    def warn(self, message: str):
        global LEVEL_WARN
        if self.isWarnEnabled():
            self.log(level=LEVEL_WARN, message=message)

    def isInfoEnabled(self):
        global LEVEL_INFO
        return self.isLevelEnabled(level=LEVEL_INFO)
    
    def info(self, message: str):
        global LEVEL_INFO
        if self.isInfoEnabled():
            self.log(level=LEVEL_INFO, message=message)

    def isDebugEnabled(self):
        global LEVEL_DEBUG
        return self.isLevelEnabled(level=LEVEL_DEBUG)
    
    def debug(self, message: str):
        global LEVEL_DEBUG
        if self.isDebugEnabled():
            self.log(level=LEVEL_DEBUG, message=message)

    def isTraceEnabled(self):
        global LEVEL_TRACE
        return self.isLevelEnabled(level=LEVEL_TRACE)
    
    def trace(self, message: str):
        global LEVEL_TRACE
        if self.isTraceEnabled():
            self.log(level=LEVEL_TRACE, message=message)
        
    def testLog(self):
        self.error("Error Testlog")
        self.warn("Warn Testlog")
        self.info("Info Testlog")
        self.debug("Debug Testlog")
        self.trace("Trace Testlog")

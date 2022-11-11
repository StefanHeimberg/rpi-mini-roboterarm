from logger import *
from roboterarm import *

# ====================================================
# Logging
# ====================================================

setDefaultLoggingLevel(level=LEVEL_ALL)

# ====================================================
# Roboterarm
# ====================================================

motoren_laden('motoren.txt')

script_ausfuehren('reset.txt')

script_ausfuehren('test1.txt')
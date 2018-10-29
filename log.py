import os
import inspect
from Logger import logger

DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4

def create(filename, message, type_logger):
    # INFO: create instance of Logger
    log = logger.Logger(filename)

    current_file_name = os.path.basename(__file__)
    current_line_number = inspect.currentframe().f_back.f_lineno
    
    log.generate(message, current_file_name, current_line_number, type_logger)

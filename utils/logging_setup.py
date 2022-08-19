import logging 
import os 

from logging.handlers import RotatingFileHandler


def setup_logger(env: str) -> None:
    """sets up logger details based on selected environment.
    The name logging name is hardcoded.
    
    Args:
        env (str): either 'production' or 'debug'
        if env parameter is set to 'debug', logging.debug can be used.
    Returns: None 
    """
    # logging info
    log_filename = "logs/macrom_bots.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    if env == 'production':
        logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)s:%(message)s')
    elif env == 'debug':
        file_handler = logging.FileHandler(log_filename, mode="w", encoding=None, delay=False)
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(lineno)s:%(message)s')  # for debugging
    
    log = logging.getLogger()
    # When the size is about to be exceeded, the file is closed and a new file is silently opened for output
    # backupCount: log1, log2 .etc..
    handler = RotatingFileHandler(
        log_filename, maxBytes=50*1024*1024, backupCount=10)
    log.addHandler(handler)
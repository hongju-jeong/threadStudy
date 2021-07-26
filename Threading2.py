import logging
import threading

def get_logger():
    logger = logging.getLogger("Thread Example")
    logger.setLevel(logging.DEBUG)

    fh = logging.StreamHandler()
    fmt = ''
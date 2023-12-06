import time

import pyautogui
import logging
from logging.handlers import RotatingFileHandler
import sys

LOG_PATH = "/Users/fung.mak/dev/bee/clicker/log/away_listener.log"
IDLE_TIME_IN_S = 5


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = RotatingFileHandler(LOG_PATH, maxBytes=1024 * 1024 * 10,
                                  backupCount=20)
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger


logger = setup_custom_logger('myapp')


def start():
    noticed_idle = False
    noticed_resume = False

    idle_start_time = None
    previous_pos = None
    while True:
        x, y = pyautogui.position()
        if previous_pos == [x, y]:
            current_time = time.time()
            if idle_start_time is None:
                idle_start_time = current_time
            if current_time - idle_start_time > IDLE_TIME_IN_S and not noticed_idle:
                noticed_idle = True
                noticed_resume = False
                logger.info("start idle")
        else:
            if idle_start_time is not None:
                idle_start_time = None
            if not noticed_resume:
                noticed_idle = False
                noticed_resume = True
                logger.info("start resume")

        previous_pos = [x, y]
        time.sleep(1)


if __name__ == '__main__':
    start()

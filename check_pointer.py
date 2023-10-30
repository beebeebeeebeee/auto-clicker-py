import time

import pyautogui


def check_pointer():
    x, y = pyautogui.position()
    print("{}, {}".format(x, y))


if __name__ == '__main__':
    time.sleep(1)
    check_pointer()

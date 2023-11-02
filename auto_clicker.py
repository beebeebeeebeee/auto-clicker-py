import time
import pyautogui
from steps import click_steps


def start():
    for step in click_steps:
        if step is None:
            pyautogui.click()
        elif type(step) == int or type(step) == float:
            time.sleep(step)
        elif hasattr(step, "__len__") and len(step) == 2:
            x, y = step
            pyautogui.moveTo(x, y)


if __name__ == '__main__':
    start()

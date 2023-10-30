import time

import pyautogui

# pointer: [x, y]
# sleep: 2
# click: None
click_steps = [
    [1162, -1030],
    None,
    [1308, -584],
    None,
    2,
    [2257, -781],
    None
]


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

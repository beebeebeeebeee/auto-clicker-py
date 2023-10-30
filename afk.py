import pyautogui

start_pos = [100, 100]
second_pos = [100, 500]


def is_in_start_pos() -> bool:
    x, y = pyautogui.position()
    return [x, y] == start_pos


def start():
    pyautogui.moveTo(start_pos)
    while is_in_start_pos():
        pyautogui.moveTo(second_pos)
        pyautogui.moveTo(start_pos)


if __name__ == '__main__':
    start()

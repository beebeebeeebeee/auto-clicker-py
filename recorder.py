import time
from pynput import mouse


def record():
    click_steps = []
    last_timestamp = None

    def on_click(x, y, button, pressed):
        nonlocal last_timestamp
        if pressed:
            if button == mouse.Button.left:
                current_timestamp = time.time()
                if last_timestamp is not None:
                    click_steps.append(current_timestamp - last_timestamp)
                last_timestamp = current_timestamp
                click_steps.append([x, y])
                click_steps.append(None)
            else:
                f = open("steps.py", "w")
                f.write("click_steps = {}".format(click_steps))
                f.close()
                return False

    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()


if __name__ == '__main__':
    record()

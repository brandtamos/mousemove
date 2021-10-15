import pyautogui
import time
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while(1):

        pyautogui.moveTo(random.randint(0,2000),random.randint(0, 1000), duration = 1)
        pyautogui.moveTo(random.randint(0,2000),random.randint(0, 1000), duration = 1)
        # time.sleep(10)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

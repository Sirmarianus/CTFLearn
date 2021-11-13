import pyautogui as pag
import time

for i in range(100):
    name = str(i) + '.jpg'
    pag.screenshot(name)
    time.sleep(0.05)
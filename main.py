import webbrowser
from pynput.keyboard import Key, Controller
import time

webbrowser.open('http://google.com')
keyboard = Controller()

time.sleep(1)
num_of_tabs = 1
for x in range(0, num_of_tabs):
    keyboard.press(Key.cmd)
    keyboard.press('w')
    time.sleep(1)
    keyboard.release(Key.cmd)
    keyboard.release('w')

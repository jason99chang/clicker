import webbrowser
from pynput.keyboard import Key, Controller
import time
import os

links = open("links.txt")

for x in links:
    x = x.rstrip()
    webbrowser.open(url=x)

keyboard = Controller()

numTabs = len(open("links.txt").readlines())

links.close()

input("Press enter to continue...")
if os.name == 'nt':
    for y in range(0, numTabs):
        time.sleep(0.5)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release(Key.ctrl)
        keyboard.release('w')
else:
    for y in range(0, numTabs):
        time.sleep(0.5)
        keyboard.press(Key.cmd)
        keyboard.press('w')
        keyboard.release(Key.cmd)
        keyboard.release('w')

print("Sucessfully clicked then closed all links")
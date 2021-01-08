import pyautogui
import time

from time import sleep
from pyautogui import typewrite
from pyautogui import press

sleep(5)

f = open("beemovie", 'r')
for word in f:
    typewrite(word)
    sleep(0.5)
    press("enter")
    sleep(0.5)
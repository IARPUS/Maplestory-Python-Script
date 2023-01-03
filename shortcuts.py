import pydirectinput
import keyboard
import time
from pynput.keyboard import Key, Controller 

distanceMap = 6

def jumpAttack():
    pydirectinput.press('space')
    pydirectinput.press('e')
    pydirectinput.press('e')
    pydirectinput.press('e')
    pydirectinput.press('e')

def oneShot():
    time.sleep(.01)
    pydirectinput.press('3')
    time.sleep(.01)
    pydirectinput.press('4')
    time.sleep(.01)
    pydirectinput.press('t')
    time.sleep(.01)

def ults():
    pydirectinput.press('s')
    time.sleep(4.75)
    pydirectinput.press('pagedown')
    time.sleep(4.75)

def buffs():
    pydirectinput.press('1')
    time.sleep(2.75) 
    pydirectinput.press('2')
    time.sleep(.75)
    pydirectinput.press('pageup')
    time.sleep(.75)
    pydirectinput.press('home')
    time.sleep(.75)
    pydirectinput.press('end')
    time.sleep(.75)

def jump():
    pydirectinput.press('space') 
    time.sleep(.008)     
    pydirectinput.press('space') 
    time.sleep(.008) 
    pydirectinput.press('space')
    time.sleep(.2)      

def vaporBladeJump():
    time.sleep(1)
    pydirectinput.press('f')
    pydirectinput.press('r')
    pydirectinput.press('space')
    time.sleep(.3)

def dash():
    time.sleep(.05)
    pydirectinput.press('d')
    time.sleep(.02)
    pydirectinput.press('e')

def collectMeso():
    pydirectinput.press('right')
    for jumps in range(int(distanceMap/2)):
        jump()
    pydirectinput.press('left')
    vaporBladeJump()
    vaporBladeJump()
    vaporBladeJump()
    for jumps in range(distanceMap-1):
        jump()
    time.sleep(1)
    pydirectinput.press('right')
    pydirectinput.press('6')
    for dashes in range(distanceMap+1):
        dash()
        time.sleep(.5)
    pydirectinput.press('6')
    pydirectinput.press('left')
    pydirectinput.press('6')
    for jumps in range(int(distanceMap/2)-1):
        dash()
    pydirectinput.press('6')
    pydirectinput.press('f')
    pydirectinput.press('r')

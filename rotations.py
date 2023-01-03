import shortcuts
import pydirectinput
import keyboard
import time
from pynput.keyboard import Key, Controller

def rotation1():
    while True:
        keyboard.wait('f1')
        buffTimer1 = time.perf_counter()
        healTimer1 = time.perf_counter()
        while True:
            #going right
            stop = False
            for jumps in range(9):
                if keyboard.is_pressed('f2'):
                    stop = True
                    break
                pydirectinput.keyDown('right')
                shortcuts.jumpAttack()
                pydirectinput.keyUp('right')
                if(jumps == 4):
                    pydirectinput.keyUp('right')
                    buffTimer2 = time.perf_counter()
                    if(buffTimer2 - buffTimer1 >= 130):
                        shortcuts.buffs()
                        shortcuts.ults()
                        buffTimer1 = time.perf_counter()
                    shortcuts.oneShot()
                    pydirectinput.keyDown('right')
            if(stop):
                break
            pydirectinput.keyUp('right')
            #going left
            for jumps in range(9):
                if keyboard.is_pressed('f2'):
                    stop = True
                    break
                pydirectinput.keyDown('left')
                shortcuts.jumpAttack()
                pydirectinput.keyUp('left')
                if(jumps == 4):
                    pydirectinput.keyUp('left')
                    buffTimer2 = time.perf_counter()
                    if(buffTimer2 - buffTimer1 >= 130):
                        shortcuts.buffs()
                        shortcuts.ults()
                        buffTimer1 = time.perf_counter()
                    shortcuts.oneShot()
                    pydirectinput.keyDown('left')
            if(stop):
                    break
            pydirectinput.press('space')
            pydirectinput.press('t')
            pydirectinput.keyUp('left')
            pydirectinput.press('5')
            #buff up, ult, and heal after 130 sec
            if keyboard.is_pressed('f2'):
                break

def rotation2():
    pydirectinput.press('right')
    pydirectinput.press('space')
    time.sleep(.01)
    pydirectinput.press('3')
    time.sleep(6)
    pydirectinput.press('left')
    pydirectinput.press('space')
    time.sleep(.01)
    pydirectinput.press('4')
    time.sleep(4)
    pydirectinput.press('space')
    time.sleep(.01)
    pydirectinput.press('t')
    time.sleep(4)
  
def rotation3():
    pydirectinput.press('right')
    time.sleep(.01)
    pydirectinput.press('3')
    time.sleep(1)
    pydirectinput.press('4')
    time.sleep(.01)
    time.sleep(6)
    pydirectinput.press('left')
    pydirectinput.press('t')
    time.sleep(3)
    time.sleep(.01)

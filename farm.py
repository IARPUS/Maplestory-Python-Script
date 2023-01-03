import pydirectinput
import keyboard
import time
from pynput.keyboard import Key, Controller 
import shortcuts
import rotations

while True:
    keyboard.wait('f1')
    try:
        healTimer1 = time.perf_counter()
        mesoTimer1 = time.perf_counter()
        buffTimer1 = time.perf_counter()
        first = True
        while True:
            if first:
                shortcuts.buffs()
                first = False
            healTimer2 = time.perf_counter()
            mesoTimer2 = time.perf_counter()
            buffTimer2 = time.perf_counter()
            #rotations.rotation2()
            rotations.rotation3()
            if(healTimer2-healTimer1>= 45):
                pydirectinput.press('5')
                healTimer1 = time.perf_counter()
            if(mesoTimer2-mesoTimer1>=90):
                shortcuts.collectMeso()
                time.sleep(1)
                mesoTimer1 = time.perf_counter()
            if(buffTimer2-buffTimer1 >= 180):
                shortcuts.ults()
                shortcuts.buffs()
                buffTimer1 = time.perf_counter()
    except KeyboardInterrupt:
        pass
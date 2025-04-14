from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
defeat=0
time.sleep(5)
while True:
#Assault maps
#hanamura code:
    defeat=0
    if pyautogui.locateOnScreen('hanamura.PNG', confidence=0.8) != None:
        print("Its hanamura")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackhanamura.PNG',grayscale=True, confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     
#horizon code:
    if pyautogui.locateOnScreen('horizon.png',region=(830,908,360,94), confidence=0.88) != None:
        print("Its horizon")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackhorizon.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     
#paris code:
    if pyautogui.locateOnScreen('paris.png',region=(1300,908,360,94), confidence=0.8) != None:
        print("Its paris")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackparis.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Temple of anubis code:
    if pyautogui.locateOnScreen('temple.png',region=(1000,908,320,94), confidence=0.8) != None:
        print("Its temple of anubis")
        time.sleep(4)
        if pyautogui.locateOnScreen('attacktemple.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Volskaya code:
    if pyautogui.locateOnScreen('volskaya.png',region=(900,908,320,94), confidence=0.8) != None:
        print("Its volskaya")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackvolskaya.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#control maps
#busan code:
    if pyautogui.locateOnScreen('busan.png',region=(1290,910,360,94), confidence=0.8) != None:
        print("Its busan")
        time.sleep(4)
        print("Its attack")
        while True:
            pyautogui.moveTo(410,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1   
            pyautogui.moveTo(470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(950,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1350,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1520,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            if defeat==1:
                break     


#ilios code:
    if pyautogui.locateOnScreen('ilios.png',region=(1340,910,360,94), confidence=0.8) != None:
        print("Its ilios")
        time.sleep(4)
        print("Its attack")
        while True:
            pyautogui.moveTo(410,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1   
            pyautogui.moveTo(470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(950,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1350,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1520,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            if defeat==1:
                break   

#lijiang code:
    if pyautogui.locateOnScreen('lijiang.png',region=(1100,908,360,94), confidence=0.8) != None:
        print("Its lijiang")
        time.sleep(4)
        print("Its attack")
        while True:
            pyautogui.moveTo(410,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1   
            pyautogui.moveTo(470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(950,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1350,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1520,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            if defeat==1:
                break   
#nepal code:
    if pyautogui.locateOnScreen('nepal.png',region=(1380,908,270,94), confidence=0.8) != None:
        print("Its nepal")
        time.sleep(4)
        print("Its attack")
        while True:
            pyautogui.moveTo(410,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1   
            pyautogui.moveTo(470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(950,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1350,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1470,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            pyautogui.moveTo(1520,890)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1350,500)
            pyautogui.click
            pyautogui.mouseDown()
            pyautogui.keyDown('w')
            time.sleep(.3)
            pyautogui.keyUp('w')
            time.sleep(.3)
            pyautogui.mouseUp()
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                defeat=1
            if defeat==1:
                break   
#oasis code:
    if pyautogui.locateOnScreen('oasis.png',region=(1300,908,360,94), confidence=0.8) != None:
        print("Its oasis")
        time.sleep(4)
        print("Its attack")
        pyautogui.press('esc')
        pyautogui.moveTo(959,642)
        pyautogui.click(clicks=2, interval=0.25)
        pyautogui.moveTo(1011,563)
        pyautogui.click(clicks=2, interval=0.25)
        time.sleep(5)
        pyautogui.moveTo(1277,515)
        pyautogui.click(clicks=2, interval=0.25)         
#ESCORT MAPS            
#Dorado code:
    if pyautogui.locateOnScreen('dorado.png', region=(1300,908,360,94), confidence=0.8) != None:
        print("Its Dorado")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackdorado.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Escort maps
#Havana code:
    if pyautogui.locateOnScreen('havana.png',region=(1300,908,360,94), confidence=0.8) != None:
        print("Its Havana")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackhavana.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Junkertown code:
    if pyautogui.locateOnScreen('junkertown.png',region=(1160,908,360,94), confidence=0.8) != None:
        print("Its Junkertown")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackjunkertown.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Rialto code:
    if pyautogui.locateOnScreen('rialto.png',region=(1300,908,360,94), confidence=0.8) != None:
        print("Its Rialto")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackrialto.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Route 66 code:
    if pyautogui.locateOnScreen('route66.png',region=(1265,908,360,94), confidence=0.8) != None:
        print("Its Route 66")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackroute66.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Watchpoint: Gibraltar code:
    if pyautogui.locateOnScreen('watchpoint.png',region=(830,908,360,94), confidence=0.8) != None:
        print("Its Watchpoint: Gibraltar")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackgibralter.PNG', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Hybird maps
#Hollywood code:
    if pyautogui.locateOnScreen('hollywood.png',region=(1190,908,360,94), confidence=0.8) != None:
        print("Its hollywood")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackhollywood.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Numbani code:
    if pyautogui.locateOnScreen('numbani.png',region=(1278,908,360,94), confidence=0.8) != None:
        print("Its numbani")
        time.sleep(4)
        if pyautogui.locateOnScreen('attacknumbani.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Blizzard World code:
    if pyautogui.locateOnScreen('blizzardworld.png',region=(1060,908,360,94), confidence=0.8) != None:
        print("Its Blizzard World")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackblizzardworld.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#King's Row code:
    if pyautogui.locateOnScreen('kingsRow.png',region=(1170,908,320,94), confidence=0.8) != None:
        print("Its King's Row")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackkingsRow.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     

#Eichenwalde code:
    if pyautogui.locateOnScreen('eichenwalde.png',region=(1150,908,320,94), confidence=0.8) != None:
        print("Its Eichenwalde")
        time.sleep(4)
        if pyautogui.locateOnScreen('attackeichenwalde.png', confidence=0.8) != None:
            print("Its attack")
            pyautogui.press('esc')
            pyautogui.moveTo(959,642)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.moveTo(1011,563)
            pyautogui.click(clicks=2, interval=0.25)
            time.sleep(5)
            pyautogui.moveTo(1277,515)
            pyautogui.click(clicks=2, interval=0.25)
        else:
            print("Its defence")
            while True:
                pyautogui.moveTo(410,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1   
                pyautogui.moveTo(470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(950,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1350,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1470,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                pyautogui.moveTo(1520,890)
                pyautogui.click(clicks=2, interval=0.25)
                pyautogui.moveTo(1350,500)
                pyautogui.click
                pyautogui.mouseDown()
                pyautogui.keyDown('w')
                time.sleep(.3)
                pyautogui.keyUp('w')
                time.sleep(.3)
                pyautogui.mouseUp()
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
                if pyautogui.locateOnScreen('defeat.png', confidence=0.8) != None:
                    defeat=1
                if defeat==1:
                    break     
            
    if keyboard.is_pressed("l"):
        pyautogui.mouseUp()
        print("l pressed, ending loop")
        break


            

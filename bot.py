#from PIL import ImageGrab
import pyautogui
import time

class Cordinates():
    replayBtn = (340, 490)
    dino = (260, 490)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')


restartGame()
time.sleep(1)
jump()

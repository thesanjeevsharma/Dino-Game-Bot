from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    #These cordiantes will change as per your screen.
    replayBtn = (340, 310)
    dino = (90, 315)
    #330
    #90
    
def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dino[0]+(150),Cordinates.dino[1],Cordinates.dino[0]+(150)+40,Cordinates.dino[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!= 1538):
            jump()
            time.sleep(0.1)


main()

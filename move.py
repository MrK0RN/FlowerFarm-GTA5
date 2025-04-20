import mouse
from time import sleep
import keyboard

def run(time):
    keyboard.press('w')
    keyboard.press('shift')
    sleep(time)
    keyboard.release('shift')
    keyboard.release('w')
def go_forward(time):
    keyboard.press('w')
    sleep(time)
    keyboard.release('w')
def turn():
    mouse.move(-6, 0, False, 0.01)

def turn_snake(a):
    mouse.move(a*2, 0, False, 1)
def press(a):
    keyboard.press(a)
    sleep(0.2)
    keyboard.release(a)


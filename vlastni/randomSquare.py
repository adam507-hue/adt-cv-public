import tkinter
import math
import time
import random

root = tkinter.Tk()
canvas = tkinter.Canvas(height=600, width=600)
canvas.pack()

maxX = 600
maxY = 600

while True:
    x = random.randint(0, maxX)
    y = random.randint(0, maxY)
    canvas.create_rectangle(x,y,x+1,y+1)
    time.sleep(0.001)
    canvas.update()
import tkinter
import math

root = tkinter.Tk()
canvas = tkinter.Canvas(height=600, width=600)

center_x = 300
center_y = 300

def getPointAngle(x: float, y: float) -> float:
    return(math.tan(x/y) * math.pi/180)

def getPointDis(x: float, y: float) -> float:
    return(math.sqrt(x*x + y*y))

def drawPolarPoint(angle:float, distance: float):
    x_pixel = center_x + (distance * math.cos(angle))
    y_pixel = center_y + (distance * math.sin(angle))

    canvas.create_rectangle(x_pixel, y_pixel, x_pixel+1, y_pixel+1)


for i in range(1,1000):
    drawPolarPoint(getPointAngle(i, math.sin(i)), getPointDis(i, math.sin(i)))

canvas.pack()
root.mainloop()

from tkinter import *
from decimal import getcontext
from coordinates import *
import tasks
from motion import *
from table import Table, AsyncTableController
import asyncio

root = Tk()
getcontext().prec = 20

controller = AsyncTableController()
controller.draw()

w = 1000
h = 1000
x = quarter(w, True)
y = quarter(h, False)
x0 = quarter(w, False)
y0 = quarter(h, True)


canvas = Canvas(master=root, width=w, height=h)
canvas.pack()
#hid = HID(canvas, display_mouse_x, display_mouse_y)
#hid.draw()
canvas.config(width=w, height=h)
cor = Coords(canvas, x0, y0, x, y, x0, y0, Direction.UP.value, Direction.RIGHT.value)
cor.push(canvas)
ref = ReferenceSystem(cor)
print(x0, y0)
print(ref.to_real())
ref.set_new_offset_loyal(20, -20)
print(ref.current())
print(ref.to_real())
#Motion.draw_trajectory(canvas, 10, 20)
dot = canvas.create_oval(300, 300, 300, 300)
root.bind("<Motion>", lambda: asyncio)
root.mainloop()
from tkinter import *
from decimal import getcontext
from coordinates import *
import tasks
from motion import *
from table import Table
import asyncio

getcontext().prec = 20

w = 1000
h = 1000
x = quarter(w, True)
y = quarter(h, False)
x0 = quarter(w, False)
y0 = quarter(h, True)

class App():
    async def exec(self):
        self.window = Window()
        await self.window.activate()

class Window(Tk):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(master=self.root, width=w, height=h)
        self.canvas.pack()
        self.canvas.config(width=w, height=h)
        self.cor = Coords(self.canvas, x0, y0, x, y, x0, y0, Direction.UP.value, Direction.RIGHT.value)
        self.cor.push(self.canvas)
        self.ref = ReferenceSystem(self.cor)
        self.root.mainloop()

    async def activate(self):
        self.table = Table(asyncio.get_event_loop(), "Table", "800", "800", tasks.display_mouse_coordinates)
        self.root.bind(sequence="<Motion>", func=lambda event: self.table.loop.create_task(self.table.update(event)))

asyncio.run(App().exec())

#hid = HID(canvas, display_mouse_x, display_mouse_y)
#hid.draw()

#print(x0, y0)
#print(ref.to_real())
#ref.set_new_offset_loyal(20, -20)
#print(ref.current())
#print(ref.to_real())
#Motion.draw_trajectory(canvas, 10, 20)
#dot = canvas.create_oval(300, 300, 300, 300)
#root.bind("<Motion>", lambda:  controller.run())

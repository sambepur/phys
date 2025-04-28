from decimal import Decimal
import math
from enum import Enum
from tkinter import Canvas
from motion import *

class Direction(Enum):
    DOWN = -1
    UP = 1
    LEFT = -1
    RIGHT = 1

def quarter(coord: int, _R_T: bool):
    return coord//4*3 if _R_T else coord//4
    

class Coords():
    def __init__(self, canvas: Canvas, x0: int, y0: int, scale_x: int, scale_y: int, start_y: int, start_x: int, direction_x: int, direction_y: int) -> None:
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.start_x = start_x
        self.start_y = start_y
        self.line_y_id = self.canvas.create_line(x0, y0, x0, scale_y, width = 2)
        self.line_x_id = self.canvas.create_line(x0, y0, scale_x, y0, width = 2)
        print(f"line x created: {self.line_x_id}\nline y created: {self.line_y_id}")

    def zeros(self):
        return self.x0, self.y0

    def push(self, canvas: Canvas):
        canvas.itemconfig(self.line_x_id)
        canvas.itemconfig(self.line_y_id)

    def get_direction(self):
        return self.direction_x, self.direction_y
    
    def move_to(self, object_id: int, x: int, y: int):
        self.canvas.move(object_id, x, y)
    
    def mouse_coords(event):
        x, y = event.x, event.y
        print(x, y)

class ReferenceSystem():
    g = Motion.acceleration_of_free_fall(Constant.G.value, Constant.M_e.value, Constant.R_e.value)
    def __init__(self, coords: Coords):
        self.current_x = 0
        self.current_y = 0
        self.x0_real, self.y0_real = coords.zeros()
        self.direction_x, self.direction_y = coords.get_direction()

    def current(self):
        return self.current_x, self.current_y

    def to_real(self):
        return self.current_x+self.x0_real, self.current_y+self.y0_real

    def set_new_offset_loyal(self, next_x: int, next_y:int):
        self.current_x += (next_x*self.direction_x)
        print(f"DEBUG {self.current_x}")
        self.current_y += (next_y*self.direction_y)
        print(f"DEBUG {next_y*self.direction_y}")
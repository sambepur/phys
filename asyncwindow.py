import asyncio
from tkinter import *
import typing

class AsyncWindow(Tk):
    def __init__(self, loop: asyncio.unix_events._UnixSelectorEventLoop, name: str, width: str, height: str, *coroutines: typing.Coroutine):
        self.loop = loop
        self.root = Tk()
        self.root.title(name)
        self.root.geometry(width+"x"+height)
        self.coroutines = coroutines        

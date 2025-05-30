from tkinter import Label, Tk
from asyncwindow import AsyncWindow
import tasks
import typing
import asyncio

class Table(AsyncWindow):
    def __init__(self, loop: asyncio.unix_events._UnixSelectorEventLoop, name: str, width: str, height: str, *coroutines: typing.Coroutine):
        super().__init__(loop, name, width, height, coroutines)
        self.labels: list[Label] = list()
        self.root.mainloop()

    def draw(self):
        for t in range(len(self.coroutines)):
            label = Label(master=self.root, font=("TimesNewRoman", 40), borderwidth=2, relief="solid")
            label.grid(column=t, row=0)
            self.labels.append(label)

    async def update(self, event):
        for coroutine, label in self.coroutines, self.labels:
            label.config(text= await self.loop.create_task(coroutine(event)))


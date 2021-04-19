#!/usr/bin/env python3
'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product
import gettext

gettext.install("click", ".", names=("ngettext",))

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''

class App(Application):
    def increaseText(self):
        global clicks
        clicks += 1
        self.text.set(ngettext("%d time clicked", "%d times clicked", clicks) % (clicks,))

    def create_widgets(self):
        super().create_widgets()
        self.text = tk.StringVar()
        self.B = tk.Button(self, text=_("Press me"), command=self.increaseText)
        self.Label = tk.Label(self, textvariable=self.text)
        self.B.grid()
        self.Label.grid()

clicks = 0
app = App(title="Sample application")
app.mainloop()
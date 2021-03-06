#!/usr/bin/env python3
'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product

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
    def create_widgets(self):
        super().create_widgets()
        self.C = tk.Canvas(self)
        self.C.grid()
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid()
        '''
        colors = ['red', 'green', 'blue']
        self.T.insert("end", 'red', ('red',))
        for c in colors:
            self.T.tag_add(c)
            self.T.tag_config(c, foreground=c)
        '''

app = App(title="Sample application")
app.mainloop()
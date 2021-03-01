import subprocess
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def quitButton(self):
		"""<docstring> Plug for exit button"""
		pass


	def createWidgets(self):
		#self.quitButton = tk.Button(self, text='Quit', command=quitButton)
		#self.quitButton.grid()
		pass

app = Application()
app.master.title('Display commands application')
app.mainloop()
import subprocess
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def quitButton(self):
		"""Handler for exit button."""
		pass


	def createWidgets(self):
		self.quitButton = tk.Button(self, text='Quit', command=self.quitButton)
		self.Label = tk.Label(self, text='<MenuItem>')
		self.Label.grid(row=0)
		self.quitButton.grid(row=1)
		pass

app = Application()
app.master.title('Display commands application')
app.mainloop()
import subprocess
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.dir = tk.StringVar()
		#self.date = 
		#self.git = 
		self.dirButton = tk.Button(self, text='dir')
		self.dateButton = tk.Button(self, text='date')
		self.gitButton = tk.Button(self, text='git')
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.Label = tk.Label(self, text=subprocess.run(["dir"], capture_output=True).stdout)
		self.dirButton.grid(row=0, column=0)
		self.dateButton.grid(row=0, column=1)
		self.gitButton.grid(row=0, column=2)
		self.quitButton.grid(row=1, column=1)
		self.Label.grid(row=2, column=1)

app = Application()
app.master.title('Display commands application')
app.mainloop()
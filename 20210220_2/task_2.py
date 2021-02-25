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
		self.timeButton = tk.Button(self, text='Time')
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.Label = tk.Label(self, text=subprocess.run(["dir"], capture_output=True).stdout)
		self.timeButton.grid()
		self.quitButton.grid(row=0, column=1)
		self.Label.grid(columnspan=2)

app = Application()
app.master.title('Display commands application')
app.mainloop()
import subprocess
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def dirText(self):
		self.text.set(subprocess.run(['dir'], capture_output=True).stdout)

	def dateText(self):
		self.text.set(subprocess.run(['date'], capture_output=True).stdout)

	def gitText(self):
		self.text.set(subprocess.run(['git'], capture_output=True).stdout)

	def createWidgets(self):
		self.text = tk.StringVar()
		self.dirButton = tk.Button(self, text='dir', command=self.dirText)
		self.dateButton = tk.Button(self, text='date', command=self.dateText)
		self.gitButton = tk.Button(self, text='git', command=self.gitText)
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.Label = tk.Label(self, textvariable=self.text)
		self.dirButton.grid(row=0, column=0)
		self.dateButton.grid(row=0, column=1)
		self.gitButton.grid(row=0, column=2)
		self.quitButton.grid(row=1, column=1)
		self.Label.grid(row=2, column=1)

app = Application()
app.master.title('Display commands application')
app.mainloop()
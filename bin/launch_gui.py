#!/user/bin/python

import tkinter

# Create a Class for GUI
class simpleapp_tk(tkinter.Tk):
	def __init__(self, parent):
		tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	# Initialize Function will have 
	# Buttons, widgets etc.
	def initialize(self):
		self.grid()

		self.entryVariable = tkinter.StringVar()
		self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0,row=0,sticky='EW')

		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here.")

		button = tkinter.Button(self,text=u"Click me !", 
							command=self.OnButtonClick)
		button.grid(column=1,row=0)

		self.labelVariable = tkinter.StringVar()
		label = tkinter.Label(self,textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky='EW')

		self.labelVariable.set(u"Hello !")

		self.grid_columnconfigure(0,weight=1)

		self.resizable(True,False)

	def OnButtonClick(self):
		#self.labelVariable.set("You clicked the button !")
		self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
		print ("You clicked the button !")
	
	def OnPressEnter(self,event):
		#self.labelVariable.set("You pressed enter !")
		self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
		print ("You pressed enter !")


# Create Main
if __name__ == "__main__":
	
	# Create the Tk app instance
	app = simpleapp_tk(None)
	
	# Title for the GUI app
	app.title('my application')

	print("Starting GUI Application")
	print("Going in Event Loop")

	# Start the main loop
	app.mainloop()

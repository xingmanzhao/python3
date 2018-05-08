#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'training of tkinter'

__author__ = 'xingman zhao'

from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()



app = Application()
app.master.title('Hello world')
app.mainloop()

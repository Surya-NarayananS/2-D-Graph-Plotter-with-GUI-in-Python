'''
This is a simple 2-D Line Graph Plotter Application with GUI
Python 3.6
This Source Code uses modules like Tkinter, Matplotlib, Numpy, Math, Webbrowser, TTKThemes, etc
Coded by Surya Narayanan, 2019
Feel Free to Use, edit, make changes, etc to the code
'''

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import math
import webbrowser as wb
from tkinter import messagebox



def guiWindow():
		root = ThemedTk(theme="scid themes") #Application Window
		root.title("2-D Graph Plotter")


		can_height = 550
		can_width = 1000

		canvas = Canvas(root, height=can_height, width=can_width)
		canvas.pack()


		#Common Styling for buttons, labels, etc
		s = ttk.Style()
		s.configure('TButton', font='Courier, 15', background='#006bb3', foreground='black')
		s.configure('ab.TButton', font='Courier, 13', background='#006bb3', foreground='black')
		s.configure('TFrame', background='#99d6ff')
		s.configure('TLabelframe', background='#99d6ff')
		s.configure('TLabel', background='#99d6ff', foreground='black')
		s.configure('TPanedwindow', background='#d9d9d9', foreground='black')
		s.configure('TCombobox', background='#bfbfbf', font='Courier 10')



		def exitfunc():
			quit()

		
		#Menu Bar and its menus:-
		menubar = Menu(root)

		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command = exitfunc)
		#Save As... is at the bottom
		menubar.add_cascade(label="File", menu=filemenu)
		global lstyle
		lstyle = "-"	#default plot line style
		global lcolor
		lcolor = "red"	#default plot line color
		global gridlinestyle
		gridlinestyle = '--'

		def linestylefunc(): #Style for the plot line
			global lstyle
			linestylewin = ThemedTk(theme="scid themes")
			linestylewin.title("Line Style")
			labels = ttk.Label(linestylewin, text="Choose the style of plot line :  ", style='TLabel')
			labels.pack(side='left')
			choices = ["- - - -", "_______(Default)"]

			variables = StringVar()
			

			choice = ttk.Combobox(linestylewin, textvariable=variables, values=choices, style='TCombobox')
			choice.set("_______(Default)")
			choice.pack(side='left')
			choice.bind("<<ComboboxSelected>>")
			def linestylefunc2():
				global lstyle
				temp = choice.get()
				if temp == "_______(Default)":
					lstyle = "-"
				elif temp == "- - - -":
					lstyle = "--"
				root.update()
				linestylewin.destroy()
			button0 = ttk.Button(linestylewin, text="Save", style='TButton', command=linestylefunc2)
			button0.pack(side='left')
			linestylewin.mainloop()



		def linecolorfunc(): #Color of the plot line
			global lcolor
			linecolorwin = ThemedTk(theme="scid themes")
			linecolorwin.title("Line Color")
			labelc = ttk.Label(linecolorwin, text="Choose the color of plot line :  ", style='TLabel')
			labelc.pack(side='left')
			choices = ["Default(Red)", "Orange", "Blue", "Black", "Green"]

			variables = StringVar()
			

			choice = ttk.Combobox(linecolorwin, textvariable=variables, values=choices, style='TCombobox')
			choice.set("Default(Red)")
			choice.pack(side='left')
			choice.bind("<<ComboboxSelected>>")
			def linecolorfunc2():
				global lcolor
				temp = choice.get()
				if temp == "Default(Red)":
					lcolor = "red"
				elif temp == "Orange":
					lcolor = "#d35400"
				elif temp == "Blue":
					lcolor = "blue"
				elif temp == "Black":
					lcolor = "black"
				elif temp == "Green":
					lcolor = "green"
				root.update()
				linecolorwin.destroy()
			button0 = ttk.Button(linecolorwin, text="Save", style='TButton', command=linecolorfunc2)
			button0.pack(side='left')
			linecolorwin.mainloop()


		def gridlinestylefunc(): #Grid line style
			global gridlinestyle
			gridlinestylewin = ThemedTk(theme="scid themes")
			gridlinestylewin.title("Grid Line Style")
			labelg = ttk.Label(gridlinestylewin, text="Choose the style of grid line :  ", style='TLabel')
			labelg.pack(side='left')
			choices = ["------(Default)", "______"]

			variables = StringVar()
			

			choice = ttk.Combobox(gridlinestylewin, textvariable=variables, values=choices, style='TCombobox')
			choice.set("------(Default)")
			choice.pack(side='left')
			choice.bind("<<ComboboxSelected>>")
			def gridlinestylefunc2():
				global gridlinestyle
				temp = choice.get()
				if temp == "______":
					gridlinestyle = "-"
				elif temp == "------(Default)":
					gridlinestyle = "--"
				root.update()
				gridlinestylewin.destroy()
			button0 = ttk.Button(gridlinestylewin, text="Save", style='TButton', command=gridlinestylefunc2)
			button0.pack(side='left')
			gridlinestylewin.mainloop()


		settingsmenu = Menu(menubar, tearoff=0)
		settingsmenu.add_command(label="Plot Line Style", command = linestylefunc)
		settingsmenu.add_command(label="Plot Line Color", command = linecolorfunc)
		settingsmenu.add_command(label="Grid Line Style", command= gridlinestylefunc)
		menubar.add_cascade(label="Settings", menu=settingsmenu)


		global customx
		global customy
		customx = "x - axis"	#default x, y labels for custom plot
		customy = "y - axis"


		def getxy():	#x, y labels for custom plot
			global customx
			global customy
			getxy = ThemedTk(theme="scid themes")
			getxy.title("Axes Labels")
			labelx = ttk.Label(getxy, text="Enter the label of x - axis :  ", style='TLabel')
			labelx.grid(row=0, column=0)
			entryx = ttk.Entry(getxy)
			entryx.grid(row=0, column=1)
			labely = ttk.Label(getxy, text="Enter the label of y - axis :  ", style='TLabel')
			labely.grid(row=1, column=0)
			entryy = ttk.Entry(getxy)
			entryy.grid(row=1, column=1)
			def getxyfunc2():
				global customx
				global customy
				customx = entryx.get()
				customy = entryy.get()
				root.update()
				getxy.destroy()
			buttonx = ttk.Button(getxy, text="Save", style='TButton', command=getxyfunc2)
			buttonx.grid(row=3, column=1)
			getxy.mainloop()
			


		def masterhelp():	#help from menu bar
			helpwin = ThemedTk(theme="scid themes")
			helpwin.title("Master Help")
			helplabel = ttk.Label(helpwin, text="""This is a 2-D graph plotter Application. It contains two panes: Graph Pane and Menu Pane.
The Menu Pane is where you will be working with, while the Graph Pane displays the Graph.\n
To quit app: File-->Exit
To save the Graph: File-->Save As...
Every Menu Pane contains a 'Help Me' to assist you if you need.\n
The Menu Pane starts with two(2) buttons: Common Math Functions and Custom Plot.\n
Common Math Functions:-\n      Here, you can view the graph of most commonly used mathematical functions.\n
Custom Plot:-\n      Here, you can plot a graph with your custom coordinates(x, y). Note: You can plot atmost Five(5) coordinates.\n
In Common Math Functions pane, choose a function from the drop-down list box. Then, click on 'Plot' to view its graph.
You can save the graph by selecting (File-->Save As...) in .png format. Note: You need not enter '.png'.
If the function you selected sounds unfamiliar, click on 'Google this function' to view more about the function in your Computer's default Web Browser.
Note: This function requires an internet connection.
To jump back to the Main Menu, click on 'Go Back'\n
In Custom Plot pane, Choose the number of coordinates(x, y) to plot from the drop-down list box. Then click on 'OK'. Enter your (x,y) coordinates and click on 'Plot' to view the graph.
You can save the graph by selecting (File-->Save As...) in .png format.
To jump back to the Main Menu, click on 'Go Back'.\n
Finally, if you want to know more about this Application and Developer, choose (About-->About this App or About-->About the Developer).""", style='TLabel')
			helplabel.pack(anchor='nw')
			helpwin.mainloop()


		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help!", command = masterhelp)
		menubar.add_cascade(label="Help", menu=helpmenu)


		def aboutapp():	#about the app
			appwin = ThemedTk(theme="scid themes")
			appwin.title("About this Application")
			applabel = ttk.Label(appwin, text="""2-D Graph Plotter can be used to do a quick plot of your coordinates. Also, this application can be used to view the Graphs of the basic, yet most commonly used mathematical functions.
'2-D Graph Plotter' is Open-Source and is free to use, copy, modify, merge, publish, distribute, etc. It is copyrighted under MIT License.

MIT License
Copyright (c) 2019 Surya Narayanan""", style='TLabel')
			applabel.pack(anchor='nw')
			appwin.mainloop()

		def aboutdev():	#about the developer
			devwin = ThemedTk(theme="scid themes")
			devwin.title("About the Developer")
			devlabel = ttk.Label(devwin, text="""I'm Surya Narayanan from India and I coded this app entirely independent. This is my first ever Open-Source project.
Please feel free to review, edit and make changes to the code.
You can view the source code here: https://github.com/Surya-NarayananS/2-D-Graph-Plotter-with-GUI-in-Python.git
You can contact me: suryanarayanansg@gmail.com
Hoping this application is useful in some way!""", style='TLabel')
			devlabel.pack(anchor='nw')
			devwin.mainloop()

		aboutmenu = Menu(menubar, tearoff=0)
		aboutmenu.add_command(label="About this App", command = aboutapp)
		aboutmenu.add_command(label="About the Developer", command = aboutdev)
		menubar.add_cascade(label="About", menu=aboutmenu)

		#Left Pane:-
		left_pane = ttk.PanedWindow(root, style='TPanedwindow')
		left_pane.place(relx=0, relheight=1, relwidth=0.65)



		def functioncoosefunc(functionchoose):	#All Common Math Functions. Depending on the function chosen, gives x, y, title, rtc
			global x, y, functionlegend, functiontitle, functionxlabel, functionylabel, ylimit, xlim, ylim

			if functionchoose == 'Linear Function':
				x = np.arange(-3, 4, 1)
				y = 2*x
				functionlegend = '2x'
				functiontitle = "Linear Function"
				functionxlabel = "x"
				functionylabel = "y = mx+b"
				ylimit = False

			elif functionchoose == 'Square Function':
				x = np.arange(-20, 21, 1)
				y = x**2
				functionlegend = 'x^2'
				functiontitle = "Square Function"
				functionxlabel = "x"
				functionylabel = "y = x^2"
				ylimit = False

			elif functionchoose == 'Cubic Function':
				x = np.arange(-400, 401, 1)
				y = x**3
				functionlegend = 'x^3'
				functiontitle = "Cubic Function"
				functionxlabel = "x"
				functionylabel = "y = x^3"
				ylimit = False


			elif functionchoose == 'Square Root Function':
				x = np.arange(0, 80, 1)
				y = [math.sqrt(num) for num in x]
				functionlegend = '√x'
				functiontitle = "Square Root Function"
				functionxlabel = "x"
				functionylabel = "y = √x"
				ylimit = False

			elif functionchoose == 'Reciprocal Function':
				x = np.arange(-50,51,1)
				y = [1/num for num in x]
				functionlegend = '1/x'
				functiontitle = "Reciprocal Function"
				functionxlabel = "x"
				functionylabel = "y = 1/x"
				ylimit = False

			elif functionchoose == 'Absolute Function':
				x = np.arange(-3, 4, 1)
				y = abs(x)
				functionlegend = '|x|'
				functiontitle = "Absolute Function"
				functionxlabel = "x"
				functionylabel = "|x|"
				ylimit = False

			elif functionchoose == 'Sine Function':
				x = np.arange(0, 2 * 3.14, 0.0001)
				y = np.sin(x)
				functionlegend = 'sin(x)'
				functiontitle = "Sine Function"
				functionxlabel = "x"
				functionylabel = "y = sin(x)"
				ylimit = False


			elif functionchoose == 'Cosine Function':
				x = np.arange(0, 2 * 3.14, 0.0001)
				y = np.cos(x)
				functionlegend = 'cos(x)'
				functiontitle = "Cosine Function"
				functionxlabel = "x"
				functionylabel = "y = cos(x)"
				ylimit = False

			elif functionchoose == 'Tangent Function':
				x = np.arange(0, (2 * 3.14), 0.0001)
				y = np.tan(x)
				functionlegend = 'tan(x)'
				functiontitle = "Tangent Function"
				functionxlabel = "x"
				functionylabel = "y = tan(x)"
				ylimit = True
				xlim = -6
				ylim = 6

			elif functionchoose == 'Cosecant Function':
				x = np.arange(0, 2 * 3.14, 0.0001)
				y = 1/(np.sin(x))
				functionlegend = 'cosec(x)'
				functiontitle = "Cosecant Function"
				functionxlabel = "x"
				functionylabel = "y = cosec(x)"
				ylimit = True
				xlim = -6
				ylim = 6


			elif functionchoose == 'Secant Function':
				x = np.arange(0, 2 * 3.14, 0.0001)
				y = 1/(np.cos(x))
				functionlegend = 'sec(x)'
				functiontitle = "Secant Function"
				functionxlabel = "x"
				functionylabel = "y = sec(x)"
				ylimit = True
				xlim = -6
				ylim = 6


			elif functionchoose == 'Cotangent Function':
				x = np.arange(0, 2 * 3.14, 0.0001)
				y = 1/(np.tan(x))
				functionlegend = 'cot(x)'
				functiontitle = "Cotangent Function"
				functionxlabel = "x"
				functionylabel = "y = cot(x)"
				ylimit = True
				xlim = -6
				ylim = 6

			elif functionchoose == 'Logarithmic Function':
				x = np.arange(1,100,1)
				y = [math.log(num) for num in x]
				functionlegend = 'ln(x)'
				functiontitle = "Logarithmic Function"
				functionxlabel = "x"
				functionylabel = "y = ln(x)"
				ylimit = False


			elif functionchoose == 'Exponential Function':
				x = np.arange(-3, 10, 1)
				y = [math.exp(num) for num in x]
				functionlegend = 'e^x'
				functiontitle = "Exponential Function"
				functionxlabel = "x"
				functionylabel = "y = e^x"
				ylimit = False

			

		def ylimfunction(ylimit): #Checks if ylimit needs to be given for common math functions
				global fig
				if ylimit == False:
					fig = plt.figure(dpi=100)
					fig.add_subplot(xlabel=functionxlabel, ylabel=functionylabel, title=functiontitle).plot(x, y, color=lcolor, linestyle=lstyle)
					fig.legend([functionlegend])
					plt.grid(True, linestyle=gridlinestyle)
					fig.set_facecolor('#d9d9d9')


				elif ylimit == True:
					fig = plt.figure(dpi=100)
					fig.add_subplot(111, ylim=(xlim,ylim), xlabel=functionxlabel, ylabel=functionylabel, title=functiontitle).plot(x, y, color=lcolor, linestyle=lstyle)
					fig.legend([functionlegend])
					plt.grid(True, linestyle=gridlinestyle)
					fig.set_facecolor('#d9d9d9')


		def drawgraph(fig):	#Displays graph of the math function chosen
			try:
				plt.close('all')
			except:
				pass
			grapharea = FigureCanvasTkAgg(fig, master=left_pane)
			grapharea.draw()
			grapharea.get_tk_widget().place(relheight=1, relwidth=1)

		

		def customdrawgraph(xlist, ylist):	#Displays custom graph
			try:
				plt.close('all')
			except:
				pass
			global fig
			fig = plt.figure(dpi=100)
			fig.add_subplot(xlabel=customx, ylabel=customy, title="Graph").plot(xlist, ylist, color=lcolor, linestyle=lstyle, 
				marker='o', markersize=4, markerfacecolor='black',markeredgecolor='black')
			fig.set_facecolor('#d9d9d9')
			plt.grid(True, linestyle=gridlinestyle)
			grapharea = FigureCanvasTkAgg(fig, master=left_pane)
			grapharea.draw()
			grapharea.get_tk_widget().place(relheight=1, relwidth=1)
			customframe.update()


		def checkfloat(l): 	#Checks for any invalid entry in custom plot
			global xlist, ylist
			try:
				try:	#Displays blank space on top of invalid entry to hide it
					label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
					label16.place(relx=0.5, rely=0.5)
				except:
					pass
				list1 = []
				for item in l:
					list1.append(float(item))
				halfcount = int(len(list1)/2) 
				xlist = list1[0:halfcount]
				ylist = list1[halfcount:]


				
			except:
				label15 = ttk.Label(customframe, text="Invalid Entry!", font=('Courier, 13'))
				label15.place(relx=0.5, rely=0.5)



		def customgraph():	#Gets user's coordinates for custom Plot
			global xlist, ylist, noofcoor
			x1, x2, x3, x4, x5, y1, y2, y3, y4, y5 = 0,0,0,0,0,0,0,0,0,0
			l = [x1, x2, x3, x4, x5, y1, y2, y3, y4, y5]

			if noofcoor == '1':
				l=[x1,y1]
				x1=entry1.get()
				y1=entry2.get()
				l[0] = x1
				l[1] = y1

			elif noofcoor == '2':
				l=[x1, x2, y1, y2]
				x1=entry1.get()
				y1=entry2.get()
				l[0] = x1
				l[2] = y1
				x2=entry3.get()
				y2=entry4.get()
				l[1] = x2
				l[3] = y2

			elif noofcoor == '3':
				l=[x1, x2, x3, y1, y2, y3]
				x1=entry1.get()
				y1=entry2.get()
				l[0] = x1
				l[3] = y1
				x2=entry3.get()
				y2=entry4.get()
				l[1] = x2
				l[4] = y2
				x3=entry5.get()
				y3=entry6.get()
				l[2] = x3
				l[5] = y3


			elif noofcoor == '4':
				l=[x1, x2, x3, x4, y1, y2, y3, y4]
				x1=entry1.get()
				y1=entry2.get()
				l[0] = x1
				l[4] = y1
				x2=entry3.get()
				y2=entry4.get()
				l[1] = x2
				l[5] = y2
				x3=entry5.get()
				y3=entry6.get()
				l[2] = x3
				l[6] = y3
				x4=entry7.get()
				y4=entry8.get()
				l[3] = x4
				l[7] = y4

			elif noofcoor == '5':
				l=[x1, x2, x3, x4, x5, y1, y2, y3, y4, y5]
				x1=entry1.get()
				y1=entry2.get()
				l[0] = x1
				l[5] = y1
				x2=entry3.get()
				y2=entry4.get()
				l[1] = x2
				l[6] = y2
				x3=entry5.get()
				y3=entry6.get()
				l[2] = x3
				l[7] = y3
				x4=entry7.get()
				y4=entry8.get()
				l[3] = x4
				l[8] = y4
				x5=entry9.get()
				y5=entry10.get()
				l[4] = x5
				l[9] = y5


			customframe.tkraise()
			checkfloat(l)
			customdrawgraph(xlist, ylist)




		def finalcustom():	#displays the entry for coordinates acoording to the user's choice of number of coordinates
			global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10
			global noofcoor
			noofcoor = funclista.get()

			if noofcoor == '1':
				labelerase = ttk.Label(customframe, text=""" """)
				labelerase.place(relx=0, rely=0.14, relwidth=1, relheight=0.35)

				label2 = ttk.Label(customframe, text="Enter the (x,y) coordinates :-", font=('Courier, 13'))
				label2.place(relx=0.1, rely=0.18, anchor='w')


				label3 = ttk.Label(customframe, text="x1 : ", font=('Courier, 12'))
				label3.place(relx=0.15, rely=0.25, anchor='w')
				entry1 = ttk.Entry(customframe)
				entry1.place(relx=0.25,rely=0.25, anchor='w', relwidth=0.15)
				label4 = ttk.Label(customframe, text="y1 : ", font=('Courier, 12'))
				label4.place(relx=0.55, rely=0.25, anchor='w')
				entry2 = ttk.Entry(customframe)
				entry2.place(relx=0.65,rely=0.25, anchor='w', relwidth=0.15)

				def del1():	#if go back is pressed, this function erases old coordinates entry boxes 
					labelerase.place_forget()
					label2.place_forget()
					label3.place_forget()
					label4.place_forget()
					entry1.place_forget()
					entry2.place_forget()
					try:
						label15.place_forget()
					except:
						label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
						label16.place(relx=0.5, rely=0.5)
					buttonunknown.place_forget()

				buttonunknown = ttk.Button(customframe, text="Go Back", style="ab.TButton", command=del1)
				buttonunknown.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.06)

			elif noofcoor == '2':
				labelerase = ttk.Label(customframe, text=""" """)
				labelerase.place(relx=0, rely=0.14, relwidth=1, relheight=0.35)

				label2 = ttk.Label(customframe, text="Enter the (x,y) coordinates :-", font=('Courier, 13'))
				label2.place(relx=0.1, rely=0.18, anchor='w')


				label3 = ttk.Label(customframe, text="x1 : ", font=('Courier, 12'))
				label3.place(relx=0.15, rely=0.25, anchor='w')
				entry1 = ttk.Entry(customframe)
				entry1.place(relx=0.25,rely=0.25, anchor='w', relwidth=0.15)
				label4 = ttk.Label(customframe, text="y1 : ", font=('Courier, 12'))
				label4.place(relx=0.55, rely=0.25, anchor='w')
				entry2 = ttk.Entry(customframe)
				entry2.place(relx=0.65,rely=0.25, anchor='w', relwidth=0.15)


				label5 = ttk.Label(customframe, text="x2 : ", font=('Courier, 12'))
				label5.place(relx=0.15, rely=0.30, anchor='w')
				entry3 = ttk.Entry(customframe)
				entry3.place(relx=0.25,rely=0.30, anchor='w', relwidth=0.15)
				label6 = ttk.Label(customframe, text="y2 : ", font=('Courier, 12'))
				label6.place(relx=0.55, rely=0.30, anchor='w')
				entry4 = ttk.Entry(customframe)
				entry4.place(relx=0.65,rely=0.30, anchor='w', relwidth=0.15)

				def del2():
					labelerase.place_forget()
					label2.place_forget()
					label3.place_forget()
					label4.place_forget()
					entry1.place_forget()
					entry2.place_forget()
					entry3.place_forget()
					entry4.place_forget()
					label5.place_forget()
					label6.place_forget()
					try:
						label15.place_forget()
					except:
						label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
						label16.place(relx=0.5, rely=0.5)
					buttonunknown2.place_forget()


				buttonunknown2 = ttk.Button(customframe, text="Go Back", style="ab.TButton", command=del2)
				buttonunknown2.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.06)

			elif noofcoor == '3':
				labelerase = ttk.Label(customframe, text=""" """)
				labelerase.place(relx=0, rely=0.14, relwidth=1, relheight=0.35)

				label2 = ttk.Label(customframe, text="Enter the (x,y) coordinates :-", font=('Courier, 13'))
				label2.place(relx=0.1, rely=0.18, anchor='w')


				label3 = ttk.Label(customframe, text="x1 : ", font=('Courier, 12'))
				label3.place(relx=0.15, rely=0.25, anchor='w')
				entry1 = ttk.Entry(customframe)
				entry1.place(relx=0.25,rely=0.25, anchor='w', relwidth=0.15)
				label4 = ttk.Label(customframe, text="y1 : ", font=('Courier, 12'))
				label4.place(relx=0.55, rely=0.25, anchor='w')
				entry2 = ttk.Entry(customframe)
				entry2.place(relx=0.65,rely=0.25, anchor='w', relwidth=0.15)


				label5 = ttk.Label(customframe, text="x2 : ", font=('Courier, 12'))
				label5.place(relx=0.15, rely=0.30, anchor='w')
				entry3 = ttk.Entry(customframe)
				entry3.place(relx=0.25,rely=0.30, anchor='w', relwidth=0.15)
				label6 = ttk.Label(customframe, text="y2 : ", font=('Courier, 12'))
				label6.place(relx=0.55, rely=0.30, anchor='w')
				entry4 = ttk.Entry(customframe)
				entry4.place(relx=0.65,rely=0.30, anchor='w', relwidth=0.15)


				label7 = ttk.Label(customframe, text="x3 : ", font=('Courier, 12'))
				label7.place(relx=0.15, rely=0.35, anchor='w')
				entry5 = ttk.Entry(customframe)
				entry5.place(relx=0.25,rely=0.35, anchor='w', relwidth=0.15)
				label8 = ttk.Label(customframe, text="y3 : ", font=('Courier, 12'))
				label8.place(relx=0.55, rely=0.35, anchor='w')
				entry6 = ttk.Entry(customframe)
				entry6.place(relx=0.65,rely=0.35, anchor='w', relwidth=0.15)

				def del3():
					labelerase.place_forget()
					label2.place_forget()
					label3.place_forget()
					label4.place_forget()
					entry1.place_forget()
					entry2.place_forget()
					entry3.place_forget()
					entry4.place_forget()
					label5.place_forget()
					label6.place_forget()
					entry5.place_forget()
					entry6.place_forget()
					label7.place_forget()
					label8.place_forget()
					try:
						label15.place_forget()
					except:
						label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
						label16.place(relx=0.5, rely=0.5)
					buttonunknown3.place_forget()

				buttonunknown3 = ttk.Button(customframe, text="Go Back", style="ab.TButton", command=del3)
				buttonunknown3.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.06)

			elif noofcoor == '4':
				labelerase = ttk.Label(customframe, text=""" """)
				labelerase.place(relx=0, rely=0.14, relwidth=1, relheight=0.35)

				label2 = ttk.Label(customframe, text="Enter the (x,y) coordinates :-", font=('Courier, 13'))
				label2.place(relx=0.1, rely=0.18, anchor='w')


				label3 = ttk.Label(customframe, text="x1 : ", font=('Courier, 12'))
				label3.place(relx=0.15, rely=0.25, anchor='w')
				entry1 = ttk.Entry(customframe)
				entry1.place(relx=0.25,rely=0.25, anchor='w', relwidth=0.15)
				label4 = ttk.Label(customframe, text="y1 : ", font=('Courier, 12'))
				label4.place(relx=0.55, rely=0.25, anchor='w')
				entry2 = ttk.Entry(customframe)
				entry2.place(relx=0.65,rely=0.25, anchor='w', relwidth=0.15)


				label5 = ttk.Label(customframe, text="x2 : ", font=('Courier, 12'))
				label5.place(relx=0.15, rely=0.30, anchor='w')
				entry3 = ttk.Entry(customframe)
				entry3.place(relx=0.25,rely=0.30, anchor='w', relwidth=0.15)
				label6 = ttk.Label(customframe, text="y2 : ", font=('Courier, 12'))
				label6.place(relx=0.55, rely=0.30, anchor='w')
				entry4 = ttk.Entry(customframe)
				entry4.place(relx=0.65,rely=0.30, anchor='w', relwidth=0.15)


				label7 = ttk.Label(customframe, text="x3 : ", font=('Courier, 12'))
				label7.place(relx=0.15, rely=0.35, anchor='w')
				entry5 = ttk.Entry(customframe)
				entry5.place(relx=0.25,rely=0.35, anchor='w', relwidth=0.15)
				label8 = ttk.Label(customframe, text="y3 : ", font=('Courier, 12'))
				label8.place(relx=0.55, rely=0.35, anchor='w')
				entry6 = ttk.Entry(customframe)
				entry6.place(relx=0.65,rely=0.35, anchor='w', relwidth=0.15)


				label9 = ttk.Label(customframe, text="x4 : ", font=('Courier, 12'))
				label9.place(relx=0.15, rely=0.40, anchor='w')
				entry7 = ttk.Entry(customframe)
				entry7.place(relx=0.25,rely=0.40, anchor='w', relwidth=0.15)
				label10 = ttk.Label(customframe, text="y4 : ", font=('Courier, 12'))
				label10.place(relx=0.55, rely=0.40, anchor='w')
				entry8 = ttk.Entry(customframe)
				entry8.place(relx=0.65,rely=0.40, anchor='w', relwidth=0.15)

				def del4():
					labelerase.place_forget()
					label2.place_forget()
					label3.place_forget()
					label4.place_forget()
					entry1.place_forget()
					entry2.place_forget()
					entry3.place_forget()
					entry4.place_forget()
					label5.place_forget()
					label6.place_forget()
					entry5.place_forget()
					entry6.place_forget()
					label7.place_forget()
					label8.place_forget()
					label9.place_forget()
					label10.place_forget()
					entry7.place_forget()
					entry8.place_forget()
					try:
						label15.place_forget()
					except:
						label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
						label16.place(relx=0.5, rely=0.5)
					buttonunknown4.place_forget()

				buttonunknown4 = ttk.Button(customframe, text="Go Back", style="ab.TButton", command=del4)
				buttonunknown4.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.06)

			elif noofcoor == '5':
				labelerase = ttk.Label(customframe, text=""" """)
				labelerase.place(relx=0, rely=0.14, relwidth=1, relheight=0.35)

				label2 = ttk.Label(customframe, text="Enter the (x,y) coordinates :-", font=('Courier, 13'))
				label2.place(relx=0.1, rely=0.18, anchor='w')


				label3 = ttk.Label(customframe, text="x1 : ", font=('Courier, 12'))
				label3.place(relx=0.15, rely=0.25, anchor='w')
				entry1 = ttk.Entry(customframe)
				entry1.place(relx=0.25,rely=0.25, anchor='w', relwidth=0.15)
				label4 = ttk.Label(customframe, text="y1 : ", font=('Courier, 12'))
				label4.place(relx=0.55, rely=0.25, anchor='w')
				entry2 = ttk.Entry(customframe)
				entry2.place(relx=0.65,rely=0.25, anchor='w', relwidth=0.15)


				label5 = ttk.Label(customframe, text="x2 : ", font=('Courier, 12'))
				label5.place(relx=0.15, rely=0.30, anchor='w')
				entry3 = ttk.Entry(customframe)
				entry3.place(relx=0.25,rely=0.30, anchor='w', relwidth=0.15)
				label6 = ttk.Label(customframe, text="y2 : ", font=('Courier, 12'))
				label6.place(relx=0.55, rely=0.30, anchor='w')
				entry4 = ttk.Entry(customframe)
				entry4.place(relx=0.65,rely=0.30, anchor='w', relwidth=0.15)


				label7 = ttk.Label(customframe, text="x3 : ", font=('Courier, 12'))
				label7.place(relx=0.15, rely=0.35, anchor='w')
				entry5 = ttk.Entry(customframe)
				entry5.place(relx=0.25,rely=0.35, anchor='w', relwidth=0.15)
				label8 = ttk.Label(customframe, text="y3 : ", font=('Courier, 12'))
				label8.place(relx=0.55, rely=0.35, anchor='w')
				entry6 = ttk.Entry(customframe)
				entry6.place(relx=0.65,rely=0.35, anchor='w', relwidth=0.15)


				label9 = ttk.Label(customframe, text="x4 : ", font=('Courier, 12'))
				label9.place(relx=0.15, rely=0.40, anchor='w')
				entry7 = ttk.Entry(customframe)
				entry7.place(relx=0.25,rely=0.40, anchor='w', relwidth=0.15)
				label10 = ttk.Label(customframe, text="y4 : ", font=('Courier, 12'))
				label10.place(relx=0.55, rely=0.40, anchor='w')
				entry8 = ttk.Entry(customframe)
				entry8.place(relx=0.65,rely=0.40, anchor='w', relwidth=0.15)


				label11 = ttk.Label(customframe, text="x5 : ", font=('Courier, 12'))
				label11.place(relx=0.15, rely=0.45, anchor='w')
				entry9 = ttk.Entry(customframe)
				entry9.place(relx=0.25,rely=0.45, anchor='w', relwidth=0.15)
				label12 = ttk.Label(customframe, text="y5 : ", font=('Courier, 12'))
				label12.place(relx=0.55, rely=0.45, anchor='w')
				entry10 = ttk.Entry(customframe)
				entry10.place(relx=0.65,rely=0.45, anchor='w', relwidth=0.15)

				def del5():
					labelerase.place_forget()
					label2.place_forget()
					label3.place_forget()
					label4.place_forget()
					entry1.place_forget()
					entry2.place_forget()
					entry3.place_forget()
					entry4.place_forget()
					label5.place_forget()
					label6.place_forget()
					entry5.place_forget()
					entry6.place_forget()
					label7.place_forget()
					label8.place_forget()
					label9.place_forget()
					label10.place_forget()
					entry7.place_forget()
					entry8.place_forget()
					entry9.place_forget()
					entry10.place_forget()
					label11.place_forget()
					label12.place_forget()
					try:
						label15.place_forget()
					except:
						label16 = ttk.Label(customframe, text="                       ", font=('Courier, 13'))
						label16.place(relx=0.5, rely=0.5)
					buttonunknown5.place_forget()

				buttonunknown5 = ttk.Button(customframe, text="Go Back", style="ab.TButton", command=del5)
				buttonunknown5.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.06)

			else:
				customframe.tkraise()


		def customplothelp():	#Help in custom plot window
			messagebox.showinfo("Helper", """Choose the number of coordinates(x, y) to plot from the drop-down list box. Then click on 'OK'. Enter your (x,y) coordinates and click on 'Plot' to view the graph.
\nYou can save the graph by selecting (File-->Save As...) in .png format.\nTo jump back to the Main Menu, click on 'Go Back'.\n""")

			

		#Custom Frame:-
		customframe = ttk.Frame(root)
		customframe.place(relx=0.65, relwidth=0.35, relheight=1)


		button8 = ttk.Button(customframe, text="Main Menu", command=lambda: mainframe.tkraise())
		button8.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.1)


		labelerase = ttk.Label(customframe, text=""" """)
		labelerase.place(relx=0, rely=0.15, relwidth=1, relheight=0.55)

		labela1 = ttk.Label(customframe, text="""Choose the number of (x,y) coordinates
you wish to plot :-""", font=('Courier, 13'))
		labela1.place(relx=0.1, rely=0.25, anchor='w')


		choicesa = ["1", "2", "3", "4", "5"]
		variablea = StringVar()
		variablea.set("5")
		funclista = ttk.Combobox(customframe, textvariable=variablea, values=choicesa, style='TCombobox')
		funclista.place(relx=0.1, rely=0.32, relheight=0.05, relwidth=0.8)
		funclista.bind("<<ComboboxSelected>>")


		buttona = ttk.Button(customframe, text="Ok", command=finalcustom, style='ab.TButton')
		buttona.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.06)


		button9 = ttk.Button(customframe, text="Axes Labels", command=getxy)
		button9.place(relx=0.1, rely=0.58, relheight=0.07, relwidth=0.8)

		button10 = ttk.Button(customframe, text="Help Me", command=customplothelp)
		button10.place(relx=0.1, rely=0.69, relwidth=0.8, relheight=0.07)

		button11 = ttk.Button(customframe, text="Plot", command=customgraph)
		button11.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.17)



		def commonfunchelp():	#help in common functions window
			messagebox.showinfo("Helper", """Choose a function from the drop-down list box. Then, click on 'Plot' to view its graph.
You can save the graph by selecting (File-->Save As...) in .png format. Note: You need not enter '.png'.
If the function you selected sounds unfamiliar, click on 'Google this function' to view more about the function in your Computer's default Web Browser.
Note: This function requires an internet connection.\nTo jump back to the Main Menu, click on 'Go Back'\n""")


		#CommonMathFunctions Display:-
		commonframe = ttk.Frame(root)
		commonframe.place(relx=0.65, relwidth=0.35, relheight=1)


		button4 = ttk.Button(commonframe, text="Main Menu", command=lambda: mainframe.tkraise())
		button4.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.1)

		labelFrame = ttk.LabelFrame(commonframe, text="Common Mathematical Functions", style='TLabelframe')
		labelFrame.place(relx=0, rely=0.2, relwidth=1, relheight=0.4)

		label1 = ttk.Label(commonframe, text="Choose a Function :-", font=('Courier, 12'))
		label1.place(relx=0.01, rely=0.3, anchor='w')

		def googlesearch():	#To search the current function selected
			searchterm = funclist.get()
			url = f"https://www.google.co.in/search?q={searchterm}"
			wb.open_new_tab(url)



		def plotgraph():
			functionchoose = funclist.get()
			functioncoosefunc(functionchoose)
			ylimfunction(ylimit)
			drawgraph(fig)


		choices = ["Linear Function", "Square Function", "Cubic Function", "Square Root Function", "Reciprocal Function",
		"Absolute Function", "Sine Function", "Cosine Function", "Tangent Function", "Cosecant Function", "Secant Function",
		"Cotangent Function", "Logarithmic Function", "Exponential Function"]

		variable = StringVar()
		variable.set("Linear Function")

		funclist = ttk.Combobox(labelFrame, textvariable=variable, values=choices, style='TCombobox')
		funclist.place(relx=0.1, rely=0.35, relheight=0.15, relwidth=0.8)

		funclist.bind("<<ComboboxSelected>>")

		button5 = ttk.Button(commonframe, text="Google this function", command=googlesearch)
		button5.place(relx=0.1, rely=0.46, relwidth=0.8, relheight=0.08)

		button6 = ttk.Button(commonframe, text="Help Me", command=commonfunchelp)
		button6.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.07)

		button7 = ttk.Button(commonframe, text="Plot", command=plotgraph)
		button7.place(relx=0.1, rely=0.76, relwidth=0.8, relheight=0.17)



		def mainhelp(): # help in main window
			messagebox.showinfo("Helper", """Common Math Functions:-\n      Here, you can view the graph of most commonly used mathematical functions.\n
Custom Plot:-\n      Here, you can plot a graph with your custom coordinates(x, y). Note: You can plot atmost Five(5) coordinates.\n""")



		#Main Frame:-
		mainframe = ttk.Frame(root, style='TFrame')
		mainframe.place(relx=0.65, relwidth=0.35, relheight=1)

		button1 = ttk.Button(mainframe, text="Common Math Functions", style='TButton', command=lambda: commonframe.tkraise())
		button1.place(relx=0.1, rely=0.10, relwidth=0.8, relheight=0.2)

		button2 = ttk.Button(mainframe, text="Custom Plot", command=lambda: customframe.tkraise())
		button2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

		button3 = ttk.Button(mainframe, text="Help Me", command=mainhelp)
		button3.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)


		def savefunc():	#Saves the graph in .png format
			savewindow = ThemedTk(theme="scid themes")
			savewindow. title("Save As...")
			label0 = ttk.Label(savewindow, text="Enter File Name :  ", style='TLabel')
			label0.pack(side='left')
			entry0 = ttk.Entry(savewindow)
			entry0.pack(side='left')
			def savefunc2():
				savewindow.tkraise()
				filename = entry0.get()
				string = filename + '.png'
				fig.savefig(string)
				savewindow.destroy()
			button0 = ttk.Button(savewindow, text="Save", style='TButton', command=savefunc2)
			button0.pack(side='left')
			savewindow.mainloop()
						


		filemenu.add_command(label="Save As...", command = savefunc)

		root.config(menu=menubar)


		mainframe.tkraise()
		root.mainloop()


guiWindow() #Application opens at the start


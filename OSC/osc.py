import subprocess
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import myModule
import time
import random
import math
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
from oscilloscope import Osc

count=0
def runccode(filename):
	osc = Osc(window_sec=10, intensity=1)
	arr=[]
	#a_file = open("my_file.txt", "r")
	a_file = open(filename, "r")
	for line in a_file:
		stripped_line = line.rstrip()
		k=float(stripped_line)	
		arr.append(int(k))
	print(arr[2])
	@osc.signal
	def increasing_signal(state):
		while True:
			global count
			if(count==len(arr)-1):
				print("entered quit")
				exit()
			state.draw(arr[count])
			myModule.fib(1)
			count=count+1
	osc.start()



top=tk.Tk()
top.title("TIFR")
top.geometry("1500x1500")

fontStyle = tkFont.Font(size=32)



imagee= Image.open("tifrlogo.png")
imagee = imagee.resize((250, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(imagee)
panel = tk.Label(top, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")
panel.place(x=1200,y=10)





imagee1= Image.open("somaiya.png")
imagee1 = imagee1.resize((250, 200), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(imagee1)
panel1 = tk.Label(top, image = img1)
panel1.pack(side = "bottom", fill = "both", expand = "no")
panel1.place(x=10,y=10)


devlop=tk.Label(top,text="DATA ACQUISITION SYSTEM",font=fontStyle)
devlop.place(x=500,y=50)

label1=tk.Label(top,text="Enter File Name")
label1.place(x=210,y=270)
entry1=tk.Entry(top,bd=5)
entry1.place(x=400,y=270)

run=tk.Button(top,text="Run OSC",command=lambda: runccode(entry1.get()))
run.place(x=210,y=450)

top.mainloop()

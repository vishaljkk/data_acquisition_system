
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
counter=0
k=-1
t=0
counter1=0
t1=0
k1=-1
counter2=0
t2=0
k2=-1
#filenameosc=""
# def osc_graph():
# 	tar=[]
# 	global filenameosc
# 	print(filenameosc)
# 	from oscilloscope import Osc
# 	def setdata():
# 		pullData = open(filenameosc,"r").read()
# 		dataArray=pullData.rsplit("\n")
# 		for eachline in dataArray:
# 			if(len(eachline)>1):
# 				tar.append(float(eachline))
# 		return dataArray

# 	osc = Osc(window_sec=10, intensity=1)
# 	@osc.signal
# 	def increasing_signal(state):
# 		for i in range(0,len(tar)):
# 			k = float(tar[i])
# 			state.draw(k)
# 			myModule.fib(1)
# 	tar=setdata()
# 	print(tar)
# 	osc.start()

# def ns1():
# 	subprocess.call("gcc nanosecond.c -o nanosecond -lm",shell=True)
# def ns(t):
# 	subprocess.call("./nanosecond "+str(t),shell=True)

def runccode(m,s,l,u):
	try :
		mean = int(m)
	except :
		v.set("Incorrect Mean Entered, Enter Int")
		return
	try :
		std = int(s)
	except :
		v.set("Incorrect Standard Deviation, Enter Int")
		return
	
	try :
		x1 = int(l)
	except :
		v.set("Incorrect Lower X Limit Entered, Enter Int")
		return

	try :
		x2 = int(u)
	except :
		v.set("Incorrect Upper X Limit Entered, Enter Int")
		return
	# subprocess.call("gcc guassian.c -o guassian -lm",shell=True)
	# subprocess.call("./guassian "+mean+" "+std+" "+x1+" "+x2,shell=True)
	myModule.dp(mean,std,x1,x2)
	v.set("Compiled")

def showguassian():
	listting1=[]
	listting2=[]
	filename="guassian.txt"
	f = open(filename,"r+") 
	for index, line in enumerate(f.readlines()):
	  if index % 2 == 0:
	      listting2.append(float(line.rstrip("\n\r")))
	  elif index % 2 == 1:
	      listting1.append(float(line.rstrip("\n\r")))

	listting2 = np.array(listting2)
	listting1 = np.array(listting1)
	listting2_smooth = np.linspace(listting2.min(), listting2.max(), 300)
	spl = make_interp_spline(listting2,listting1,k=3)
	listting1_smooth = spl(listting2_smooth)
	plt.plot(listting2_smooth, listting1_smooth, label='lineplots', color='b')
	# filenameosc="guassian_osc.txt"
	# fosc = open(filenameosc,"w+") 
	# for i in range(0,len(listting1_smooth)):
	# 	fosc.write(str(listting1_smooth[i]) + "\n")
	# v2.set(filenameosc)
	plt.xlabel('Values')
	plt.ylabel('Frequency')
	plt.title('My Guassian graph')
	plt.legend()
	plt.show()
	
def cguassian():
	listting1=[]
	listting2=[]
	f = open("guassian.txt","r") 
	for index, line in enumerate(f.readlines()):
	  if index % 2 == 0:
	      listting2.append(float(line.rstrip("\n\r")))
	  elif index % 2 == 1:
	      listting1.append(float(line.rstrip("\n\r"))*1000000)
	f = open('my_file.txt', 'w+')
	print(listting1)
	print("..........")
	print(listting2)

	for i in range(0,len(listting1)):
	  for j in range(-1,int(listting1[i])):
	    k=str(float(listting2[i]))
	    k=k+"\n"
	    f.write(k)
	f.close()
	print("completed")

def plotrehisto():
	f = open('my_file.txt', 'r+')
	lines=f.readlines()
	f.close()
	ylist=[]
	counter=0
	temp=lines[0]
	print(temp)
	xlist=[]
	xlist.append(float(temp.rstrip("\n\r")))
	for i in range(0,len(lines)):
	  if(lines[i]==temp):
	    counter=counter+1
	  else:
	    ylist.append(counter)
	    temp=lines[i]
	    counter=0
	    xlist.append(float(temp.rstrip("\n\r")))
	counter=counter+1
	ylist.append(counter)
	print(xlist,ylist)
	xlist = np.array(xlist)
	ylist = np.array(ylist)
	xlist_smooth = np.linspace(xlist.min(), xlist.max(), 300)
	spl = make_interp_spline(xlist,ylist,k=3)
	ylist_smooth = spl(xlist_smooth)		
	plt.plot(xlist_smooth, ylist_smooth, label='lineplots', color='b')
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
	plt.title('My scatter plot!')
	plt.legend()
	plt.show()
			
def risetimefalltime(r1,f1,interv11):
    try :
    	r = int(r1)
    except :
    	v1.set("Incorrect Risetime, Enter Int")
    	return
    try :
    	f = int(f1)
    except :
    	v1.set("Incorrect Falltime, Enter Int")
    	return
    try :
    	interv = int(interv11)
    except :
    	v1.set("Incorrect Interval, Enter Int")
    	return


    fig = plt.figure()
    global k
    global t
    global counter
    #global filenameosc
    ax1 = fig.add_subplot(1,1,1)
    tar=[]
    v1.set("Ok")
    # filenameosc="my_file.txt"
    # v2.set(filenameosc)
    def setdata():
        pullData = open("my_file.txt","r").read()
        dataArray=pullData.rsplit("\n")
        #print(".........")
        #print(dataArray)
        for eachline in dataArray:
          if(len(eachline)>1):
            tar.append(float(eachline))
        return dataArray
    tar=setdata()
    #print("....!!!!")
    #print(tar)
    risetime=int(r)
    falltime=int(f)
    xar=[]
    yar=[]
    def animate(i):
      global k
      global t
      global counter
      if k==-1:
        xar.append(int(t))
        yar.append(float(0))
        ax1.clear()
        ax1.plot(xar,yar)
        k=1
      elif k==1:
        t=t+risetime
        #print(t)
        #ns(t)
        xar.append(int(t))
        yar.append(float(tar[counter]))
        counter=counter+1
        ax1.clear()
        ax1.plot(xar,yar)
        k=2
      elif k==2:
        t=t+falltime
        #print(t)
        #ns(t)  
        xar.append(int(t))
        yar.append(float(0))
        ax1.clear()
        ax1.plot(xar,yar)
        k=1
    ani = animation.FuncAnimation(fig, animate, interval=int(interv))
    plt.show()
    counter=0
    k=-1
    t=0
    print(yar)




def pad(p1,r1,ff1,interv1):
	try :
		p = int(p1)
	except :
		v1.set("Incorrect Padding Specified, Enter Int")
		return
	try :
		r = int(r1)
	except :
		v1.set("Incorrect Risetime, Enter Int")
		return
	try :
		ff = int(ff1)
	except :
		v1.set("Incorrect Falltime, Enter Int")
		return
	try :
		interv = int(interv1)
	except :
		v1.set("Incorrect Interval, Enter Int")
		return


	pullData = open("my_file.txt","r").read()
	dataArray=pullData.rsplit("\n")
	f = open('my_file_pad.txt',"w+")
	for eachline in dataArray:
		f.write(eachline)
		f.write("\n")
		for i in range(0,int(p)):
			f.write("0\n")
	f.close()
	v1.set("Ok")
	#pullData.close()

	def risetimefalltimepad(r,ff,interv):
	    fig2 = plt.figure()
	    global k2
	    global t2
	    global counter2
	    ax1 = fig2.add_subplot(1,1,1)
	    tar=[]
	    def setdata():
	        pullData = open("another_file_pad.txt","r").read()
	        dataArray=pullData.rsplit("\n")
	        #print(".........")
	        #print(dataArray)
	        for eachline in dataArray:
	          if(len(eachline)>1):
	            tar.append(int(eachline))
	        return dataArray
	    tar=setdata()
	    #print("....!!!!")
	    #print(r)
	    risetime=int(r)
	    falltime=int(ff)
	    xar=[]
	    yar=[]
	    def animate(i):
	      global k2
	      global t2
	      global counter2
	      if k2==-1:
	        xar.append(t2)
	        yar.append(int(0))
	        ax1.clear()
	        ax1.plot(xar,yar)
	        k2=1
	      elif k2==1:
	        t2=t2+risetime
	        #print(t)
	        # ns(t2)
	        xar.append(t2)
	        yar.append(int(tar[counter2]))
	        counter2=counter2+1
	        ax1.clear()
	        ax1.plot(xar,yar)
	        k2=2
	      elif k2==2:
	        t2=t2+falltime
	        #print(t)
	        # ns(t2)  
	        xar.append(t2)
	        yar.append(int(0))
	        ax1.clear()
	        ax1.plot(xar,yar)
	        k2=1
	        print(yar)
	    ani = animation.FuncAnimation(fig2, animate, interval=int(interv))
	    plt.show()
	    counter2=0
	    k2=-1
	    t2=0
	risetimefalltimepad(r,ff,interv)


def radomisepad(r11,ff11,interv111):
	try :
		r1 = int(r11)
	except :
		v1.set("Incorrect Risetime, Enter Int")
		return
	try :
		ff1 = int(ff11)
	except :
		v1.set("Incorrect Falltime, Enter Int")
		return
	try :
		interv1 = int(interv111)
	except :
		v1.set("Incorrect Interval, Enter Int")
		return



	with open('my_file_pad.txt','r') as source:
		data = [ (random.random(), line) for line in source ]
	data.sort()
	with open('another_file_pad2.txt','w') as target:
		for _, line in data:
			target.write( line )
	'''def plotexpo(k):
	x.append(k)
	l=1-(math.pow(2.73,-(k)))
	y.append(l*tt)
	def plotexpo2(k):
		x.append(k+10)
		l=math.pow(2.73,-(k))
		y.append(l*tt)	
	for i in range(0,10):
		plotexpo(i)
	for i in range(0,10):
		plotexpo2(i)'''
	#without guassian
	v1.set("Ok")
	
	def risetimefalltimerandom(r1,ff1,interv1):
	    fig1 = plt.figure()
	    global k1
	    global t1
	    global counter1
	    ax11 = fig1.add_subplot(1,1,1)
	    tar1=[]
	    def setdata1():
	        pullData1 = open("another_file_pad2.txt","r").read()
	        dataArray1=pullData1.rsplit("\n")
	        #print(".........")
	        #print(dataArray)
	        for eachline1 in dataArray1:
	          if(len(eachline1)>1):
	            tar1.append(float(eachline1))
	        return dataArray1
	        #print("In setdata")
	    tar1=setdata1()
	    #print("....!!!!")
	    #print(r)
	    risetime1=int(r1)
	    falltime1=int(ff1)
	    xar1=[]
	    yar1=[]
	    counter1=0
	    t1=0
	    k1=-1
	    def animate1(i1):
	      global k1
	      global t1
	      global counter1
	      print(k1)
	      m=1
	      incr=2000
	      while(m<2):
	      	m=m+1
	      	#print(counter1)
	      	if k1==-1:
	      		#print("Ayush")
	      		xar1.append(t1)
	      		yar1.append(0)
	      		k1=1
	      		ax11.clear()
	      		ax11.plot(xar1,yar1)
	      		#counter = counter+1
	      	elif k1==1:
	        	if tar1[counter1]!=0:
	        		#print("HIII")
	        		def plotexpo(k1):
	        			xar1.append(k1+incr)
	        			l1=1-(math.pow(2.73,-(k1)))
	        			u1=float(tar1[counter1])
	        			yar1.append(float(l1*u1))
	        		def plotexpo2(k1):
	        			xar1.append(k1+incr)
	        			l1=math.pow(2.73,-(k1))
	        			u1=float(tar1[counter1])
	        			yar1.append(float(l1*u1))	
	        		for i1 in range(0+xar1[-1],incr+xar1[-1]):
	        			plotexpo(i1)
	        		for i1 in range(0+xar1[-1],incr+xar1[-1]):
	        			plotexpo2(i1)
	        		counter1=counter1+1
	        		k1=2
	        		ax11.clear()
	        		ax11.plot(xar1,yar1)
	        	else:
	        		t1=t1+risetime1
	        		xar1.append(t1)
	        		yar1.append(tar1[counter1])
	        		counter1=counter1+1
	        		k1=2
	        		ax11.clear()
	        		ax11.plot(xar1,yar1)
	        		#print("BYYYYe")
	      	elif k1==2:
	        	if tar1[counter1]!=0:
	        		#print("AAYYUU")
	        		def plotexpo(k1):
	        			xar1.append(k1+incr)
	        			l1=1-(math.pow(2.73,-(k1)))
	        			u1=float(tar1[counter1])
	        			yar1.append(float(l1*u1))
	        		def plotexpo2(k1):
	        			xar1.append(k1+incr)
	        			l1=math.pow(2.73,-(k1))
	        			u1=float(tar1[counter1])
	        			yar1.append(float(l1*u1))	
	        		for i1 in range(0+xar1[-1],incr+xar1[-1]):
	        			plotexpo(i1)
	        		for i1 in range(0+xar1[-1],incr+xar1[-1]):
	        			plotexpo2(i1)
	        		counter1=counter1+1
	        		k1=1
	        		ax11.clear()
	        		ax11.plot(xar1,yar1)
	        	else:
	        		t1=t1+falltime1
	        		xar1.append(t1)
	        		yar1.append(0)
	        		k1=1
	        		ax11.clear()
	        		ax11.plot(xar1,yar1)
	        		#print("HSSSI")
	      print(len(yar1))
	    ani = animation.FuncAnimation(fig1, animate1, interval=int(interv1))
	    plt.show()
	    counter1=0
	    k1=-1
	    t1=0
	    print("xar yar is")
	    #print(xar1,yar1)
	    with open('xaxis.txt','w') as target:
	    	for i in xar1:
	    		target.write(str(i))
	    		target.write("\n")
	    #print("xar yar is")
	    #print(xar1,yar1)
	    with open('yaxis.txt','w') as target:
	    	for i in yar1:
	    		target.write(str(i))
	    		target.write("\n")
	risetimefalltimerandom(r1,ff1,interv1)
	
	#WITHOUT GUASSIAN

top=tk.Tk()
top.title("TIFR")
top.geometry("1500x1500")

fontStyle = tkFont.Font(size=32)

# canvas = Canvas(top, width = 300, height = 300)      
# canvas.pack()      
# img = PhotoImage(file="tifrlogo.png")      
# canvas.create_image(20,20, anchor=NW, image=img) 

#tifr logo

imagee= Image.open("/Users/ayush/Desktop/NEW TIFR/GUI/tifrlogo.png")
imagee = imagee.resize((250, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(imagee)
panel = tk.Label(top, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")
panel.place(x=1200,y=10)


# somaiya logo


imagee1= Image.open("/Users/ayush/Desktop/NEW TIFR/GUI/somaiya.png")
imagee1 = imagee1.resize((250, 200), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(imagee1)
panel1 = tk.Label(top, image = img1)
panel1.pack(side = "bottom", fill = "both", expand = "no")
panel1.place(x=10,y=10)

# tittlee=tk.Label(top,text="DIGITAL PULSE EMULATOR")

devlop=tk.Label(top,text="DEVELOPMENT OF DIGITAL PULSE EMULATOR",font=fontStyle)
devlop.place(x=410,y=50)

label1=tk.Label(top,text="Enter Mean")
label1.place(x=210,y=270)
label2=tk.Label(top,text="Enter STD")
label2.place(x=210,y=300)
entry1=tk.Entry(top,bd=5)
entry1.place(x=400,y=270)
entry2=tk.Entry(top,bd=5)
entry2.place(x=400,y=300)
label3=tk.Label(top,text="Enter Lower X")
label3.place(x=750,y=270)
label4=tk.Label(top,text="Enter Upper X")
label4.place(x=750,y=300)
entry3=tk.Entry(top,bd=5)
entry3.place(x=850,y=270)
entry4=tk.Entry(top,bd=5)
entry4.place(x=850,y=300)
label5=tk.Label(top,text="Enter Risetime")
label5.place(x=210,y=370)
label6=tk.Label(top,text="Enter Falltime")
label6.place(x=210,y=400)
entry5=tk.Entry(top,bd=5)
entry5.place(x=400,y=370)
entry6=tk.Entry(top,bd=5)
entry6.place(x=400,y=400)
label7=tk.Label(top,text="Enter Interval")
label7.place(x=750,y=370)
entry7=tk.Entry(top,bd=5)
entry7.place(x=850,y=370)
label8=tk.Label(top,text="Enter Padding")
label8.place(x=750,y=400)
entry8=tk.Entry(top,bd=5)
entry8.place(x=850,y=400)
run=tk.Button(top,text="Compile C",command=lambda: runccode(entry1.get(),entry2.get(),entry3.get(),entry4.get()))
run.place(x=210,y=450)
v=tk.StringVar()
label3=tk.Label(top,textvariable=v)
v.set("Yet Not Compiled")
label3.place(x=210,y=480)
guassiandisplay=tk.Button(top,text="Show Graph",command=lambda: showguassian())
guassiandisplay.place(x=360,y=450)
checkguassian=tk.Button(top,text="Check Graph",command=lambda: cguassian())
checkguassian.place(x=490,y=450)
plotcheck=tk.Button(top,text="Recheck Graph",command=lambda: plotrehisto())
plotcheck.place(x=600,y=450)
rtft=tk.Button(top,text="Plot risetime",command=lambda: risetimefalltime(entry5.get(),entry6.get(),entry7.get()))
rtft.place(x=750,y=450)
# rtft1=tk.Button(top,text="Compile NS",command=lambda: ns1())
# rtft1.place(x=850,y=450)
rtft2=tk.Button(top,text="Confirm Padding",command=lambda: pad(entry8.get(),entry5.get(),entry6.get(),entry7.get()))
rtft2.place(x=880,y=450)
rtft3=tk.Button(top,text="Randmise File",command=lambda: radomisepad(entry5.get(),entry6.get(),entry7.get()))
rtft3.place(x=1030,y=450)
label12345=tk.Label(top,text="Status: ")
label12345.place(x=700,y=550)
v1=tk.StringVar()
validlabel=tk.Label(top,textvariable=v1)
v1.set("Ok")
validlabel.place(x=750,y=550)
top.mainloop()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import math

counter1=0
t1=0
k1=-1

def radomisepad(r11,ff11,interv111):
	try :
		r1 = int(r11)
	except :
		print("Incorrect Risetime, Enter Int")
		return
	try :
		ff1 = int(ff11)
	except :
		print("Incorrect Falltime, Enter Int")
		return
	try :
		interv1 = int(interv111)
	except :
		print("Incorrect Interval, Enter Int")
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
	print("Ok")
	
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


def main():
	radomisepad(4,3,1)

if __name__ == '__main__':
    main()
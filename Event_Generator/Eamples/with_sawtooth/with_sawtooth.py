import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

counter2=0
t2=0
k2=-1


def pad(p1,r1,ff1,interv1):
	try :
		p = int(p1)
	except :
		print("Incorrect Padding Specified, Enter Int")
		return
	try :
		r = int(r1)
	except :
		print("Incorrect Risetime, Enter Int")
		return
	try :
		ff = int(ff1)
	except :
		print("Incorrect Falltime, Enter Int")
		return
	try :
		interv = int(interv1)
	except :
		print("Incorrect Interval, Enter Int")
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
	print("Ok")
	#pullData.close()

	def risetimefalltimepad(r,ff,interv):
	    fig2 = plt.figure()
	    global k2
	    global t2
	    global counter2
	    ax1 = fig2.add_subplot(1,1,1)
	    tar=[]
	    def setdata():
	        pullData = open("another_file_pad2.txt","r").read()
	        dataArray=pullData.rsplit("\n")
	        #print(".........")
	        #print(dataArray)
	        for eachline in dataArray:
	          if(len(eachline)>1):
	            tar.append(float(eachline))
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
	        yar.append(float(0.0))
	        ax1.clear()
	        ax1.plot(xar,yar)
	        k2=1
	      elif k2==1:
	        t2=t2+risetime
	        #print(t)
	        # ns(t2)
	        xar.append(t2)
	        yar.append(float(tar[counter2]))
	        counter2=counter2+1
	        ax1.clear()
	        ax1.plot(xar,yar)
	        k2=2
	      elif k2==2:
	        t2=t2+falltime
	        #print(t)
	        # ns(t2)  
	        xar.append(t2)
	        yar.append(float(0.0))
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


def main():
	pad(1,4,3,1)

if __name__ == '__main__':
    main()

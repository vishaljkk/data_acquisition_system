import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

counter=0
k=-1
t=0

def risetimefalltime(r1,f1,interv11):
    try :
    	r = int(r1)
    except :
    	print("Incorrect Risetime, Enter Int")
    	return
    try :
    	f = int(f1)
    except :
    	print("Incorrect Falltime, Enter Int")
    	return
    try :
    	interv = int(interv11)
    except :
    	print("Incorrect Interval, Enter Int")
    	return


    fig = plt.figure()
    global k
    global t
    global counter
    ax1 = fig.add_subplot(1,1,1)
    tar=[]
    print("Ok")
    def setdata():
        pullData = open("my_file.txt","r").read()
        dataArray=pullData.rsplit("\n")
        for eachline in dataArray:
          if(len(eachline)>1):
            tar.append(float(eachline))
        return dataArray
    tar=setdata()
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
        xar.append(int(t))
        yar.append(float(tar[counter]))
        counter=counter+1
        ax1.clear()
        ax1.plot(xar,yar)
        k=2
      elif k==2:
        t=t+falltime  
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


def main():
    risetimefalltime(4,3,1)

if __name__ == '__main__':
    main()
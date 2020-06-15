import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

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


def main():
	cguassian()
	plotrehisto()

if __name__ == '__main__':
    main()

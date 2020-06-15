import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

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

def main():
	showguassian()

if __name__ == '__main__':
    main()


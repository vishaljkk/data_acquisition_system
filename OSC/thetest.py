'''import random
#from time import sleep
import myModule

from oscilloscope import Osc


# adjust window_sec and intensity to improve visibility
osc = Osc(window_sec=10, intensity=1)
pullData = open("my_file.txt","r").read()

@osc.signal
def increasing_signal(state):
	print(pullData[0])
	dataArray = pullData.rspilt("/n")
	for eachline in dataArray:
		if(len(eachline)>1):
			state.draw(float(eachline))
			myModule.fib(1)

osc.start()
'''
import myModule
from oscilloscope import Osc

count=0
osc = Osc(window_sec=10, intensity=1)
arr=[]
a_file = open("my_file.txt", "r")
#a_file = open("yaxis.txt", "r")
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


'''
@osc.signal
def increasing_signal(state):
	
	for line in a_file:
		stripped_line = line.rstrip()	
		print(int(float(stripped_line)))
		state.draw(stripped_line)
		myModule.fib(1)
	a_file.close()

osc.start()
'''

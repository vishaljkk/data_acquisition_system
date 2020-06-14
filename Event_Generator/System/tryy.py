import subprocess
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def runccode(t):
	subprocess.call("gcc nanosecond.c -o nanosecond -lm",shell=True)
	subprocess.call("./nanosecond "+str(t),shell=True)
runccode(10)
# data_acquisition_system

# Table of Contents:
 * Overview
 * How to run
 * Output

# Overview:
We have generated Gaussian curve as shown in figure below. We first find out events based on different input parameters provided like mean and standard deviation which generate a Gaussian curve. An event generator generates events based on the input from the Guassian file. Now a reverse process is applied to recalculate the Gaussian graph given the event file of the event. We also notice that it still retransforms to a gaussian distribution as in the initial plot.The reverse graph concept is mentioned in the folder "recheck_guassian"
    
#  How to run:

open the terminal and go to the directory

    $ cd generator/Event_Generator/Eamples
    
Now run the script 

    $python3 show_guassian.py
#  Output: 

   ![Gaussian](https://github.com/vishaljkk/data_acquisition_system/blob/master/Images/Gaussian.png)

 

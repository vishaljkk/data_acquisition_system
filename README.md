# data_acquisition_system

# Table of Contents:
    Overview
    Installation
    Implementation

# Overview:
    Large scale data acquisition systems are used
    in big data experiments currently being carried out in
    International institutes like CERN. Testing of these systems is
    a challenging task wherein each analog input channel chain
    has to be tested for the integrity of the digitized input data
    along with ensuring the robustness/correctness of the signal
    processing algorithms. A digital emulator is an important
    philosophy which can be utilized in the testing of such
    systems. In a digital emulator, pulses are generated
    depending upon the characteristics of the sensor detectors
    and the process information. This project would involve the
    development of routines required for the generation of
    digitized pulses given the information pertaining to the
    process that needs to be probed and analyzed. Thus it is
    proposed to generate pulses with the help of algorithms
    based on probability and amplitude spectrum. These pulses
    could, in turn, be used for testing data acquisition systems
    and associated signal processing techniques. The entire
    project would involve the development of associated
    routines/algorithms for the system backend using languages
    Python and C while the User interface is built using Python
    libraries.

# Installation:

System instaaltion on Ubuntu 
    
    1. a. Install GCC
            The following linux command will install gcc compiler on on Ubuntu 18.04 Bionic Beaver. Open up terminal and enter:
            $ sudo apt install gcc
                
                OR

       Install build-essential
            Another way to install gcc compiler is to install it as part of build-essential package. build-essential package will also install additional libraries as well as g++ compiler. In most cases or if unsure this is exactly what you need:
            $ sudo apt install build-essential
            Check GCC version

       b. Confirm your installation by checking for GCC version:
            In terminal run
            $ gcc --version

            Output:
            gcc (Ubuntu 7.2.0-18ubuntu2) 7.2.0
            Copyright (C) 2017 Free Software Foundation, Inc.
            This is free software; see the source for copying conditions.  There is NO
            warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

       c. Lets test the instatlltion:
            In order to test lets create a C program that prints Hello World
        
                Compile a simple C "Hello World" code:

                #include <stdio.h>
                int main()
                {
                printf("Hello, World!");
                return 0;
                }

                Save the above code within hello.c file, compile and execute it:
                $ gcc -o hello hello.c 
                $ ./hello 
                
                Output
                Hello, World!


    2. Python Installtion:
        $ sudo apt-get update
        $ sudo apt-get install python3.6

        Create a file named myscript.py and add:
        # myscript.py
        print("python is good to go")

        Open the terminal and run to test that everything is set up correct
        $ python3 myscript.py

    3. Installing pip for Python 3
        a.Start by updating the package list using the following command:
            $ sudo apt update

        b.Use the following command to install pip for Python 3:
            $ sudo apt install python3-pip
        
        c.Once the installation is complete, verify the installation by checking the pip version:
            $ pip3 --version
            
            OUTPUT:
            The version number may vary, but it will look something like this:
            pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)

    4. Installing python packages 
        Install Matplotlib with pip
            Matplotlib can also be installed using the Python package manager, pip. To install Matplotlib with pip, open a terminal window and type:
                $ pip install matplotlib
            
            Verify the installation
                To verify that Matplotlib is installed, try to invoke Matplotlib's version at the Python REPL. Use the commands below that include calling the .__version__ an attribute common to most Python packages.
                
                Open terminal and run 
                $ python3
                
                then execute the following commands
                >>> import matplotlib
                >>> matplotlib.__version__
                '3.1.1'

        Install Oscilloscope
            An oscilloscope for python
                pip install oscilloscope

            Test the libarary by running the following script:
                
                import random
                #from time import sleep
                import myModule

                from oscilloscope import Osc


                # djust window_sec and intensity to improve visibility
                osc = Osc(window_sec=10, intensity=1)


                @osc.signal
                def increasing_signal(state):
                        pullData = open("my_file.txt","r").read()
                    dataArray = pullData.rspilt("/n")
                    for eachline in dataArray:
                        if(len(eachline)>1):
                            state.draw(float(eachline))
                            myModule.fib(1)

                osc.start()
#  Implementation

    Open the terminal and go to the generator directory by typing 
        $ cd generator
    then run the script event.py file:
        $ python3 event.py  
    Output:
        ![GUI](GUI.PNG?raw=true "Display")
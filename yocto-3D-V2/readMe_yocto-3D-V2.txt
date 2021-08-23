nstructions for the Yocto-3D-V2 scripts. 

Information generated from Yocto-3D-V2 User's guide at https://www.yoctopuce.com/projects/yocto3D-V2/Y3DMK002.usermanual-EN.pdf

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
accel.py|
---------
	->This file takes the accelerometer reading from the Yocto-3D-V2 and plots the data as a function of time with PyROOT

	->No user input is required with this file, other than 
		1. Specifying the csv file that contains the accelerometer reading (line 16)
		2. Creating a title with the correct date of measurement (line 32)
		3. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
magnet.py|
----------
	->This file takes the magnetometer reading from the Yocto-3D-V2 and plots the data as a function of time with PyROOT

	->No user input is required with this file, other than 
		1. Specifying the csv file that contains the magnetometer reading (line 16)
		2. Creating a title with the correct date of measurement (line 32)
		3. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
gyro.py|
--------
	->This file takes the gyroscope reading from the Yocto-3D-V2 and plots the data as a function of time with PyROOT

	->No user input is required with this file, other than 
		1. Specifying the csv file that contains the gyroscope reading (line 16)
		2. Creating a title with the correct date of measurement (line 32)
		3. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
compass.py|
-----------
	->This file takes the compass reading from the Yocto-3D-V2 and plots the data as a function of time with PyROOT

	->No user input is required with this file, other than 
		1. Specifying the csv file that contains the compass reading (line 16)
		2. Creating a title with the correct date of measurement (line 32)
		3. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
qt.py|
------
	->This file takes the quaternion reading from the Yocto-3D-V2 and plots the data as a function of time with PyROOT

	->No user input is required with this file, other than 
		1. CHOOSING THE CORRECT quaternion: the user needs to decide which quaternion they would like to take measurements from. Once decided, qt variable names and labels should be changed in the script.
		1. Specifying the csv file that contains the quaternion reading (line 16)
		2. MAKING SURE that the index aligns with the correct quaternion (line 21)
		3. Creating a title with the correct date of measurement (line 32)
		4. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
tilt.py|
------
	->This file takes the tilt reading from the Yocto-3D-V2 and plots the data as a function of time with PyRoot
	->No user input is required with this file, other than 
		1. CHOOSING THE CORRECT tilt: the user needs to decide which tilt they would like to take measurements from. Once decided, tilt variable names and labels should be changed in the script.
		1. Specifying the csv file that contains the tilt reading (line 16)
		2. MAKING SURE that the index aligns with the correct tilt (line 21)
		3. Creating a title with the correct date of measurement (line 32)
		4. Naming the file of the plot (line 35)
----------------------------------------------------------------------------------------------------------------------
fft.py|
-------
	->This file transforms a Yocto-3D-V2 reading as a function of time into a function of frequency using the Fast Fourier Transform algorithm.

	->No user input is required with this file, other than 
		1. Specifying the csv file that contains the compass reading (line 19)
		2. Choosing the correct index of the measurement from the Yocto-3D-V2 (line 24)
		3. Creating a title with the correct date of measurement (line 36)
		4. Setting the limits of the x and y axis (lines 37-38)
		5. Naming the file of the plot (line 40)


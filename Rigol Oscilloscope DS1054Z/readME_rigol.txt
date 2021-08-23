Instructions for the remote Rigol Oscilloscope DS1054Z scripts.

Information generated from Rigol Oscilloscope DS1054Z Programming Guide at http://www.fisica.unipg.it/~michele.pauluzzi/Laboratorio%20II%20varie/Rigol%20Oscilloscope%20DS1054Z%20Programming%20Guide.pdf

------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
control.py|
-----------
	->This file includes general commands that control the oscilloscope.
	
	->To start the oscilloscope, call the run() function.
		run()
		->In SCPI, this is:
			:RUN

	->To enable the waveform auto setting function, call the auto() function.
		auto()
		->In SCPI, this is:
			:AUToscale
		->This command is equivalent to pressing the AUTO key at the front panel.
		->Meant to automatically adjust the oscilloscope parameters according to the input signal.

	->To clear all of the waveforms on the screen, call the clear() function.
		clear()
		->In SCPI, this is:
			:CLEar

	->To stop the oscilloscope, call, you guessed it, the stop() function.
		stop()
		->In SCPI, this is:
			:STOP
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
waveformdata.py|
----------------
	->This file is meant to save the waveform data and produce it into a csv file.
	
	->Let us look at an example of how the creator of this file generated a waveform.

		setChannel("CHAN1")
		setRange("1", "1000")
		getWaveform()
		getTime(1000)
	
	->As you can see, the first line calls the setChannel() function with the argument "CHAN1". This sets the channel of which the waveform will be read.
		setChannel({D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|CHAN1|CHAN2|CHAN3|CHAN4|MATH})

		->In SCPI, this is:
			:WAV:SOUR {D0|D1|D2|D3|D4|D5|D6|D7|D8|D9|D10|D11|D12|D13|D14|D15|CHAN1|CHAN2|CHAN3|CHAN4|MATH}
		->D0-D15 represents the digital channels
		->Default parameter is CHAN1

	->In the second line, the setRange() function is called with the arguments "1" and "100", which are the points where the oscilloscope starts and stops reading the waveform data, respectively.
		setRange(<start>, <stop>))
		->In SCPI, this is:
			:WAV:STAR <start>
			:WAV:STOP <stop>
		->Default parameter for start is 1
		->Default parameter for stop is 1200

	->In the third and fourth lines, the getWaveform() and getTime(1000) functions are called. The getWaveform() function is called to attain the waveform data, which is the voltage of the function, from the oscilloscope. The data format is ASC and is converted into a csv file named 'data1.csv'. The getTime() function creates a time axis that corresponds to the voltage. The argument called within this function is the range of the tracing done, which can be easily calculated by the user by substracting the start value from the stop value and adding one (see setRange() function). This is also saved as csv file named 'data2.csv'. *Both of these files are overwritten each time the program is run*
		getTime(<waverange>)

	->After these lines, the program takes over and combines those two files into one csv file so that a data analysis program can easily graph the waveform. The user is required to input a filename. *Do not include the type of file in the filename; the file is automatically a csv file*

	->Order matters. It is important that the functions are called in the order as shown in the example.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------
cursor.py|
----------
	->This file includes all of the cursor commands used to measure the x-axis and y-axis of the waveform on the screen.
	->cursor.py includes 4 classes, all of which are a representation of the cursor modes that the user can select
		->Which means that this file is object-oriented and the user will have to create an object when selecting the cursor mode they would like to use.

------------
Manual Mode|
------------
	->To select manual mode, you create a manual() object.
		obj = manual()
		->In SCPI, this is:
			:CURS:MODE MAN

	->To select the cursor type in this mode, you call the type() function. 
		obj.type({X|Y})
		->In SCPI, this is:
			:CURS:MAN:TYPE {X|Y}
		->The X type cursors are vertical lines; can be used to measure parameters such as time
		->The Y type cursors are horizontal lines; can be used to measure parameters such as voltage
		->Default parameter is X

	->To set the channel source of this mode, call the source() function
		obj.source({CHAN1|CHAN2|CHAN3|CHAN4|MATH|LA})
		->IN SCPI, this is:
			:CURS:MAN:SOUR {CHAN1|CHAN2|CHAN3|CHAN4|MATH|LA}
		->Note: cursor type cannot be selected to Y when LA is enabled
		->Default parameter is CHAN1
		
	->To select the horizontal unit, call the tunit() function
		obj.tunit({S|HZ|DEG|PERC})
		->In SCPI, this is:
			:CURS:MAN:TUN {S|HZ|DEG|PERC}
		->For S,  AX, BX, BX-AX when expressed in a measurement have the unit S; 1/|dX| is in Hz
		->For Hz,  AX, BX, BX-AX when expressed in a measurement have the unit Hz; 1/|dX| is in S
		->For DEG,  AX, BX, BX-AX are in degrees
		->For PER,  AX, BX, BX-AX are in percentage
		->Default parameter is S

	->To select the vertical unit, call the vunit() function
		obj.vunit({PER|SOUR})
		->In SCPI, this is:
			:CURS:MAN:VUN {PER|SOUR}
		->For PER,  AY, BY, BY-AY are expressed in percentage
		->FOR SOUR,  the units of AY, BY, and BY-are expressed in the unit of the current source
		->Default parameter is SOUR

	->To set the horizontal position of cursor A, call the ax() function
		obj.ax({x})
		->In SCPI, this is:
			:CURS:MAN:AX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 100
	
	->To set the horizontal position of cursor B, call the bx() function
		obj.bx({x})
		->In SCPI, this is:
			:CURS:MAN:BX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 500
	
	->To set the vertical position of cursor A, call the ay() function
		obj.ay({y})
		->In SCPI, this is:
			:CURS:MAN:AY <y>
		->y is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 100
	
	->To set the vertical position of cursor B, call the by() function
		obj.by({y})
		->In SCPI, this is:
			:CURS:MAN:BY <y>
		->y is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 300

	->To query the x value of cursor A, call the getax() function
		obj.getax()
		->In SCPI, this is:
			:CURS:MAN:AXValue?

	->To query the x value of cursor B, call the getbx() function
		obj.getbx()
		->In SCPI, this is:
			:CURS:MAN:BXValue?

	->To query the y value of cursor A, call the getay() function
		obj.getay()
		->In SCPI, this is:
			:CURS:MAN:AYValue?
	
	->To query the y value of cursor B, call the getby() function
		obj.getby()
		->In SCPI, this is:
			:CURS:MAN:BYValue?

	->To query the difference between the X values of cursor A and cursor B (BX-AX), call the getxdelta() function
		obj.getxdelta()
		->In SCPI, this is:
			:CURS:MAN:XDELta?

	->To query the reciprocal of the absolute value of the difference between X values of cursor A and cursor B (1/|dX|), call the get ixdelta() function
		obj.getixdelta()
		->In SCPI, this is:
			:CURS:MAN:IXDELta?

	->To query the difference between the Y values of cursor A and cursor B (BY-AY), call the getydelta() function
		obj.getydelta()
		->In SCPI, this is:
			:CURS:MAN:YDELta?

-----------
Track Mode|
-----------
	->To select track mode, you create a track() object.
		obj = track()
		->In SCPI, this is:
			:CURS:MODE TRAC
			
	->To set the channel source of cursor A, call the source1() function
		obj.source1({OFF|CHAN1|CHAN2|CHAN3|CHAN4|MATH})
		->In SCPI, this is:
			:CURS:TRAC:SOUR1 {OFF|CHAN1|CHAN2|CHAN3|CHAN4|MATH}
		->Default parameter is CHAN1

	->To set the channel source of cursor B, call the source2() function
		obj.source2({OFF|CHAN1|CHAN2|CHAN3|CHAN4|MATH})
		->In SCPI, this is:
			:CURS:TRAC:SOUR2 {OFF|CHAN1|CHAN2|CHAN3|CHAN4|MATH}
		->Default parameter is CHAN1

	->To set the horizontal position of cursor A, call the ax() function
		obj.ax({x})
		->In SCPI, this is:
			:CURS:TRAC:AX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 100
	
	->To set the horizontal position of cursor B, call the bx() function
		obj.bx({x})
		->In SCPI, this is:
			:CURS:TRAC:BX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen
		->Default parameter is 500

	->To query the horizontal position of cursor A, call the getax() function
		obj.getax()
		->In SCPI, this is:
			:CURS:TRAC:AX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	
	->To query the horizontal position of cursor B, call the getbx() function
		obj.getbx()
		->In SCPI, this is:
			:CURS:TRAC:BX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the vertical position of cursor A, call the getay() function
		obj.getay()
		->In SCPI, this is:
			:CURS:TRAC:AY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	
	->To query the vertical position of cursor B, call the getby() function
		obj.getby()
		->In SCPI, this is:
			:CURS:TRAC:BY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen


	->To query the x value of cursor A, call the getaxv() function
		obj.getaxv()
		->In SCPI, this is:
			:CURS:TRAC:AXValue?

	->To query the x value of cursor B, call the getbxv() function
		obj.getbxv()
		->In SCPI, this is:
			:CURS:TRAC:BXValue?

	->To query the y value of cursor A, call the getayv() function
		obj.getayv()
		->In SCPI, this is:
			:CURS:TRAC:AYValue?
	
	->To query the y value of cursor B, call the getbyv() function
		obj.getbyv()
		->In SCPI, this is:
			:CURS:TRAC:BYValue?


	->To query the difference between the X values of cursor A and cursor B (BX-AX), call the getxdelta() function
		obj.getxdelta()
		->In SCPI, this is:
			:CURS:TRAC:XDELta?

	->To query the reciprocal of the absolute value of the difference between X values of cursor A and cursor B (1/|dX|), call the get ixdelta() function
		obj.getixdelta()
		->In SCPI, this is:
			:CURS:TRAC:IXDELta?

	->To query the difference between the Y values of cursor A and cursor B (BY-AY), call the getydelta() function
		obj.getydelta()
		->In SCPI, this is:
			:CURS:TRAC:YDELta?


----------
Auto Mode|
----------
	->To select auto mode, you create an auto() object.
		obj = auto()
		->In SCPI, this is:
			:CURS:MODE AUTO

	->To select the parameters to be measured by the auto cursor from the five parameters enabled last, call the item() function
		obj.item({OFF|ITEM1|ITEM2|ITEM3|ITEM4|ITEM5})
		->In SCPI, this is:
			:CURS:AUTO:ITEM {OFF|ITEM1|ITEM2|ITEM3|ITEM4|ITEM5}
		->The parameters are enabled by the :MEASure:ITEM command (found in measure.py)
		->Default parameter is OFF

	->To query the horizontal position of cursor A, call the getax() function
		obj.getax())
		->In SCPI, this is:
			:CURS:AUTO:AX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the horizontal position of cursor B, call the getbx() function
		obj.getbx())
		->In SCPI, this is:
			:CURS:AUTO:BX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the vertical position of cursor A, call the getay() function
		obj.getay())
		->In SCPI, this is:
			:CURS:AUTO:AY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the vertical position of cursor B, call the getby() function
		obj.getby())
		->In SCPI, this is:
			:CURS:AUTO:BY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the x value of cursor A, call the getaxv() function
		obj.getaxv()
		->In SCPI, this is:
			:CURS:AUTO:AXValue?

	->To query the x value of cursor B, call the getbxv() function
		obj.getbxv()
		->In SCPI, this is:
			:CURS:AUTO:BXValue?

	->To query the y value of cursor A, call the getayv() function
		obj.getayv()
		->In SCPI, this is:
			:CURS:AUTO:AYValue?
	
	->To query the y value of cursor B, call the getbyv() function
		obj.getbyv()
		->In SCPI, this is:
			:CURS:AUTO:BYValue?


--------
XY Mode|
--------
	->To select XY mode, you create a XY() object.
		obj = xy()
		->In SCPI, this is:
			:CURS:MODE XY
		->NOTE: in XY mode, the xy display area is different than that of the other modes
		->(0, 0) is located at the top left corner of the screen
		->(400, 400) is located at the bottom right corner of the screen
		
	->To set the horizontal position of cursor A, call the ax() function
		obj.ax({x})
		->In SCPI, this is:
			:CURS:XY:AX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(400, 400) is located at the bottom right corner of the screen
		->Default parameter is 100
	
	->To set the horizontal position of cursor B, call the bx() function
		obj.bx({x})
		->In SCPI, this is:
			:CURS:XY:BX <x>
		->x is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(400, 400) is located at the bottom right corner of the screen
		->Default parameter is 300
	
	->To set the vertical position of cursor A, call the ay() function
		obj.ay({y})
		->In SCPI, this is:
			:CURS:XY:AY <y>
		->y is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(400, 400) is located at the bottom right corner of the screen
		->Default parameter is 100
	
	->To set the vertical position of cursor B, call the by() function
		obj.by({y})
		->In SCPI, this is:
			:CURS:XY:BY <y>
		->y is a representation of the horizontal pixel coordinate of the screen
		->(0, 0) is located at the top left corner of the screen
		->(400, 400) is located at the bottom right corner of the screen
		->Default parameter is 300

	->To query the horizontal position of cursor A, call the getax() function
		obj.getax())
		->In SCPI, this is:
			:CURS:XY:AX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen


	->To query the horizontal position of cursor B, call the getbx() function
		obj.getbx())
		->In SCPI, this is:
			:CURS:XY:BX?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the vertical position of cursor A, call the getay() function
		obj.getay())
		->In SCPI, this is:
			:CURS:XY:AY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the vertical position of cursor B, call the getby() function
		obj.getby())
		->In SCPI, this is:
			:CURS:XY:BY?
		->(0, 0) is located at the top left corner of the screen
		->(600, 400) is located at the bottom right corner of the screen

	->To query the x value of cursor A, call the getaxv() function
		obj.getaxv()
		->In SCPI, this is:
			:CURS:XY:AXValue?

	->To query the x value of cursor B, call the getbxv() function
		obj.getbxv()
		->In SCPI, this is:
			:CURS:XY:BXValue?

	->To query the y value of cursor A, call the getayv() function
		obj.getayv()
		->In SCPI, this is:
			:CURS:XY:AYValue?

	->To query the y value of cursor B, call the getbyv() function
		obj.getbyv()
		->In SCPI, this is:
			:CURS:XY:BYValue?







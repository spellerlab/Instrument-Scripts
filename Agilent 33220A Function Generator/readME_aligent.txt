Instructions for the remote Aligent 33220A Function Generator scripts

Information generated from Agilent 33220A User's Guide at http://ecelabs.njit.edu/student_resources/33220_user_guide.pdf
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
apply.py|
---------
	->This file uses the APPLy command, which programs the basic parameters of the function generator (frequency, amplitude) in one command.
	->If the user were to call the function without any arguments ("apply()"), all of the parameters would be set to their default values.
	->However the user can configure some or all of the function parameters
	->Let's say that we wanted to output a 10 Vpp square wave at 8 kHz and a -2.5 volt offset
		->In SCPI Language, this would be written as:
			APPL:SQU 10 VPP, 8 KHZ, -2.5 V
		->For this script, the user would need to write:
			apply("SQU", "10 VPP", "8 KHZ", "-2.5 V")
	->For another example, let's say that we wanted to output a sin wave, but we did not care about the other parameters
		->In SCPI Language, this would be written as:
			APPL:SIN    -or-    APPL:SIN DEF, DEF, DEF
		->For this script, the user would need to write:
			apply("SIN")
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
burstmode.py|
-------------
	->This file generates a burst
	->It should be noted that you need to configure the generator (see apply.py) before you generate a burst
	->You can generate a burst using two modes: triggered and gated
		->For organizational reasons, this script includes two classes that correspond with the modes
---------------
Triggered Mode|	
---------------	
	->To select triggered mode you would create a trig() object:
		obj = trig()   
		->In SCPI, this is:
			BURS:MODE TRIG
	->Now, you can output a waveform with a specific number of cycles every time a trigger is received from a trigger source


	->Burst Count
		->To set the number of cycles per burst, call the count() function from the trig() class
			obj.count({<# cycles>|INFinity|MINimum|MAXimum})
			->In SCPI, this is:
				BURS:NCYC {<# cycles>|INFinity|MINimum|MAXimum}

	->Trigger Source
		->To set the source of the burst call the source() function
			obj.source({IMMediate|EXTernal|BUS})
			->In SCPI, this is:
				TRIG:SOUR {IMMediate|EXTernal|BUS}
		->When the Immediate (internal) source is selected, the frequency at which the burst is generated is determined by the burst period (this is the default value)
		->When the External source is selected, the function generator will accept a hardware trigger applied to the rear-panel Trig In connector. (burst period is ignored)
		->When the Bus (software) source is selected, the function generator outputs one burst each time a bus trigger command is received. (burst period is ignored)

	->Burst Period
		->To set the interval at which internally-triggered bursts are generated, call the period() function
			obj.period({<seconds>|MINimum|MAXimum})
			->In SCPI, this is:
				BURS:INT:PER {<seconds>|MINimum|MAXimum}

	->Set Angle of Phase
		->To set the angle of the starting phase (default is degrees) call the phase() function
			obj.angle({DEGree|RADian})
			->In SCPI, this is:
				UNIT:ANGL {DEGree|RADian}

	->Burst Phase
		->To set the starting  phase for the burst in degrees or radians as specified in the angle command, call the function phase()
			obj.phase({<angle>|MINimum|MAXimum})
			->In SCPI, this is:
				BURS:PHAS {<angle>|MINimum|MAXimum}
	->Trigger Slope
		->To select whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector for an externally-triggered burst, call the slope() function
			obj.slope({POSitive|NEGative})
			->In SCPI, this is:
				TRIG:SLOP {POSitive|NEGative}
	->Trigger Output Slope
		->In order to select a rising or falling edge for the “trigger out” signal, call the outputSlope() function
			obj.outputSlope({POSitive|NEGative})
			->In SCPI, this is:
				OUTP:TRIG:SLOP {POSitive|NEGative}
	->Trigger Output
		->To disable or enable the “trigger out” signal (used with burst and sweep only), call the output() function
			obj.output({OFF|ON})
			->In SCPI, this is:
				OUTP:TRIG {OFF|ON}
		->When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the burst.

	->Burst State
		->To set the state of the burst, use the state() function
			obj.state({OFF|ON})
			->In SCPI, this is:
				BURS:STAT {OFF|ON}

	->Let's say we want to generate a triggered internal burst with a burst count of 1000 cycles per burst, the period to be 10 seconds, and the starting phase angle to be 30 degrees. We would write:
		obj = trig()
		obj.count("1000")
		obj.source("IMM")
		obj.period("10")
		obj.phase("30")
		obj.state("ON")
		

-----------
Gated Mode|
-----------	
	->To select gated mode you would create a gat() object:
		obj = gat()
		->In SCPI, this is:
			BURS: MODE GAT
	->Now, you can output a continuous waveform based on whether the gate signal is true or false 	


	->Set Angle of Phase
		->To set the angle of the starting phase (default is degrees) call the phase() function
			obj.angle({DEGree|RADian})
			->In SCPI, this is:
				UNIT:ANGL {DEGree|RADian}

	->Burst Phase
		->To set the starting  phase for the burst in degrees or radians as specified in the angle command, call the phase() function
			obj.phase({<angle>|MINimum|MAXimum})
			->In SCPI, this is:
				BURS:PHAS {<angle>|MINimum|MAXimum}

	->Burst State
		->To set the state of the burst, use the state() function
			obj.state({OFF|ON})
			->In SCPI, this is:
				BURS:STAT {OFF|ON}

	->Polarity
		->To select whether the function generator uses true-high (NORM) or true-low (INV) logic levels on the rear-panel Trig In connector for an externally-gated burst, use the pol() function (normal is default)
			obj.pol({NORMal|INVerted})
			->In SCPI, this is:
				BURS:GATE:POL {NORMal|INVerted}
	->Trigger Output Slope
		->To select a rising or falling edge for the “trigger out” signal, call the outputSlope() function
			obj.outputSlope({POSitive|NEGative})
			->In SCPI, this is:
				OUTP:TRIG:SLOP {POSitive|NEGative}
	->Trigger Output
		->To disable or enable the “trigger out” signal (used with burst and sweep only), call the output() function
			obj.output({OFF|ON})
			->In SCPI, this is:
				OUTP:TRIG {OFF|ON}
		->When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the burst.

	->Let's say we want to generate an external gated burst with a starting phase of 30 degrees that uses true low logic levels. We would write:
		obj = gat()
		obj.pol("INV")
		obj.phase("30")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






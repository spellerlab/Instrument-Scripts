# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:17:34 2022

@author: SpellerLab
"""

import pyvisa 
from GenericPyVisaCommands import *
import sys


## DMM USB Name: 'USB0::0x05E6::0x6500::04485760::INSTR




#def SetVoltageRange(inst, voltRange):

def SetVoltageRange(inst, rangeval):
    # units of voltage range are volts
    # options: 0.1, 1, 10, 100, 1000, or "auto"
    
    if (rangeval == 0.1) or (rangeval == 1) or (rangeval == 10) or (rangeval == 100) or (rangeval == 1000):
        inst.write(':SENS:VOLT:RANGE '+str(rangeval))      
    elif rangeval == "auto":
        inst.write('SENS:VOLT:INP AUTO')
    else:
          print("INVALID RANGE VALUE PROVIDED, RANGE NOT SET PROPERLY")
          sys.exit()
    
def MeasureDCVoltage(inst, debug=False):
    if debug is True:
        print(inst.query(':READ?'))    
    return inst.query(':READ?')

def ReturnsVoltageRange(inst):
    return(inst.query(':SENS:VOLT:RANGE?'))

def FourWireMeasurement(inst, offset):
    #### SCPI COMMAND ERROR SOMEWHERE 
    # units of ressitance range are ohms
    # options: 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000
    

    inst.write(':SENS:FUNC "FRES"') # sets to four wire measurment
    inst.write(':SENS:FRES:NPLC 1')
    inst.write(':SENS:FRES:RANG AUTO ON')
    inst.write(':SENS:FRES:AZER ON')
    print("4-WIRE RESISTANCE RANGE MEASURMENT SET TO "+str(inst.query(':SENS:FRES:RANG?'))+" OHMS")
    #if offset is True:
    #    inst.write(':SENS:FRES:OCOM ON')
    #    print("OFFSET COMPENSATION IS ENABLED")
    #else:
    #    inst.write(':SENS:FRES:OCOM OFF')
    #    print("OFFSET COMPENSATION IS DISABLED")
        
    print("MEASURED RESISTANCE VALUE IS "+str(inst.query(':READ?')))



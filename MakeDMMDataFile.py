# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:08:55 2022

@author: SpellerLab
"""
import pyvisa 
from GenericPyVisaCommands import *
from DMMFunctions import *
import datetime
import time 

#############################################################

### variables to edit 

# name of output datafile 
datafilename = "testDataFileMaker.csv"

# voltage range (suggestion: "auto")
voltagerange = "auto"

# How often you want to record a measurment: units are seconds (i.e. I will record data every x seconds)
samplingrate = 3

# desired size of datafile, synonamous with number of lines in a text file 
buffersize = 10
#############################################################



# set DMM To take Data 
rm = MakeResourceManager()

DMM = LoadInstrument(rm, 'USB0::0x05E6::0x6500::04485760::INSTR') 

ResetInstrument(DMM)
# set range for DMM measurment ~ 100 mV range
SetVoltageRange(DMM, voltagerange)  

datafile = open(datafilename, "w+")    

datafile.write("Month-Day-Year,Hour,Minute,Second,VoltageMeasurment,VoltageRange\n")                  

# define bufffer counter to set sample size for data file                       
buffercounter = 0  

while buffercounter < buffersize:
    
    FourWireMeasurement(DMM, True)
    # waits desired time to take a measuremnt 
    time.sleep(samplingrate)  
    
    # SCPI returns strings with end of lines attatched. Will mess up text file format if not converted to floats first 
    voltvalstr = MeasureDCVoltage(DMM)
    voltrangestr = ReturnsVoltageRange(DMM)
    
    #voltage = float(voltvalstr)
    #voltagerange = float(voltrangestr)
    
    # get sample's time info 
    timeinfo = datetime.datetime.now()
    year = timeinfo.strftime("%Y")
    month = timeinfo.strftime("%m")
    day = timeinfo.strftime("%d")
    hour = timeinfo.strftime("%H")
    minute = timeinfo.strftime("%M")
    second = timeinfo.strftime("%S")

    
    #datafile.write(month+"-"+day+"-"+year+","+hour+","+minute+","+second+","+str(voltage)+","+str(voltagerange)+"\n")
    
    buffercounter+=1
    
datafile.close()
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:10:36 2021

@author: Andrew Kille - SpellerLab
@email: killeandrew@gmail.com

Title: Rigol Oscilloscope DS1054Z Waveform Tracing
This script is intended to capture the data of the waveform produced on the Rigol Osilloscope DS1054Z. This includes setting parameters of the oscilloscope, accumulating the data, and converting the measurements into a csv file.For a greater explanation of this script, see the readME file associated with the Rigol Oscilloscope scripts.
"""

import pyvisa
import pandas as pd
import numpy

rm = pyvisa.ResourceManager()
oscil = rm.open_resource('#USB')  #Insert USB serial number here

print(oscil.query("*IDN?"))
print(oscil.query(":TIM:SCAL?"))


#Stops the oscillscope so that we can trace the stationary function
oscil.write(":STOP")   


#Defines the channel that we intend to gather our measurements from
def setChannel(chan):
    oscil.write(":WAV:SOUR " + chan)
    print(oscil.query(":WAV:SOUR?"))


#Defines the range of the function in which we accumulate the data
def setRange(start, stop):
    oscil.write(":WAV:STAR " + start)
    print(oscil.query(":WAV:STAR?"))
    oscil.write(":WAV:STOP " + stop)
    print(oscil.query(":WAV:STOP?"))
    

def getWaveform():
    oscil.write(":WAV:FORM ASC")   #Data is first accumulated in a .txt file
    rawdata = oscil.query(":WAV:DATA?")
    data = rawdata.split(',')
    #The format of the ASC file that is returned includes a useless string of characters before the very first measurement. The next three lines gets rid of that string
    s = data[0]  
    temp = s
    data[0] = temp[11:]
    Ndata = [float(x) for x in data] #Converts strings into floats
    numpy.savetxt('data1.csv', Ndata, delimiter = ', ') #Saved as .csv file that is overwritten every time this function is called
    
    

#The SCPI command ':WAV:DATA?' only returns the voltage values of the waveform, which means that we have to generate our own time axis with this function
def getTime(waverange):
    xincr = float(oscil.query("WAV:XINC?")) #Tells us how much to increment by

    time = []
    i = 0
    while i < waverange:  
        time.append(i*xincr) #We line up the time values with the voltage
        i+=1

    numpy.savetxt('data2.csv', time, delimiter=', ')  #Saved as .csv file


#customizes the script
setChannel("CHAN1")
setRange("1", "1000")
getWaveform()
getTime(1000)



#combines the two .csv files
data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')

output = pd.concat([data2, data1], axis= 1)
output.drop(1, axis=1, inplace=True)
filename = input('Enter filename of waveform data: ')   #User names the combined file
output.to_csv((filename) + '.csv')




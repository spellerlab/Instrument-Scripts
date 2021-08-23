# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:48:42 2021

@author: Andrew Kille - SpellerLab
@email: killeandrew@gmail.com

Title: Yocto-3D-V2 Fast Fourier Transform
This script is intended to transform the time domain of a desired measurement from the Yocto-3D-V2 into a frequency domain using the Fast Fourier Transform algorithm. For a more detailed description, see the Yocto-3D-V2 readME file. 
"""

import ROOT
from ROOT import TGraph, TCanvas, TF1, TLine, TAxis, TSpectrum
import numpy as np
from numpy import fft
import csv

x = []  #time
y = []

#places data from given CSV file into lists. *Must remember to change the CSV file name in next line
with open('3Dv2_data_8_5_2021.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter = ';')
    next(csvReader)
    for row in csvReader:
        x.append(row[0])  #Never change this -- this will always remain as time
        y.append(row[2])  #Change this index to access different columns in the Yocto CSV file
        
#turns list into numpy array
x = np.array(x, dtype=float)

#shifts the unix time to zero
x = x-x[0]
    
y = np.array(y, dtype=float)

#transforms time domain into frequency domain using numpy fft library
xf = fft.fftfreq(len(x), d=1.0)
yf = fft.fft(y)

#graphs data
c = TCanvas()
g = TGraph(len(x), xf, np.abs(yf))
g.SetTitle('Fast Fourier Transform of Accelerometer reading - 7/25/2021; Frequency; Amplitude') #update plot title, x-axis, y-axis
#Customize the data ranges (postive values only)
g.GetXaxis().SetRangeUser(0.001, 0.55) #Sets range to right after zero for x-axis; max amplitude at zero
g.GetYaxis().SetRangeUser(0, 1)

g.Draw()

c.SaveAs('fft_accel_8_5_2021.root') #update filename of plot

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:51:57 2021

@author: Andrew Kille - SpellerLab
@email: killeandrew@gmail.com

Title: Yocto-3D-V2 Qt Plot
This script is intended to plot the qt data from a given Yocto CSV file. For a more detailed description, see the Yocto-3D-V2 readME file.

**Remember to update your desired qt throughout this file; there are multiple types of qts!!**
"""

import ROOT
from ROOT import TGraph, TCanvas, TF1
import numpy as np
import csv

time = []
qt1 = []  #update the desired qt

#places data from given CSV file into lists. *Must remember to change the CSV file name in next line
with open('3Dv2_data_8_11_2021.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter = ';')
    next(csvReader)
    for row in csvReader:
        time.append(row[0])
        qt1.append(row[8])
        
#turns list into numpy array
time = np.array(time, dtype=float)

#shifts the unix time to zero
time1 = time-time[0]
    
qt1 = np.array(qt1, dtype=float)

#graphs data
c = TCanvas()
g = TGraph(len(time1), time1, qt1)
g.SetTitle('Qt1 reading - 8/11/2021; Time [s]; Qt1 [deg]') #update plot title, x-axis, y-axis

g.Draw()
c.SaveAs('Qt1_8_11_2021.png') #update filename of plot

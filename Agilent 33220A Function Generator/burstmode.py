# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 09:24:49 2021

@author: Andrew Kille - Speller Lab
@email: killeandrew@gmail.com
Title: Agilent 33220A Function Generator Burst Mode
This file allows the Agilent 33220A Function Generator to create some type of burst (trigger or gate signal).  For a more detailed description, see the Aligent Function Generator readMe file.
"""

import pyvisa

rm = pyvisa.ResourceManager()
#print(rm.list_resources())

funcgen = rm.open_resource('#USB') Insert USB serial number

print("Instrument loaded is:")
print(funcgen.query("*IDN?"))

#must load parameters before you output a burst (see apply.py)


class trig():
    #constructor
    def __init__(self):   
        self.mode = "TRIG"
        funcgen.write("BURS:MODE " + self.mode)
        print(funcgen.query("BURS:MODE?"))

    def count(self, burstCount):    
        funcgen.write("BURS:NCYC " + burstCount)
        print(funcgen.query("BURS:NCYC?"))
       
    def period(self, burstPeriod):
        funcgen.write("BURS:INT:PER " + burstPeriod)
        print(funcgen.query("BURS:INT:PER?"))

    def setUnit(self, angle):    
        funcgen.write("UNIT:ANG " + angle)
        print(funcgen.query("UNIT:ANG?"))
    
    def phase(self, burstPhase):   
        funcgen.write("BURS:STAT " + burstPhase)
        print(funcgen.query("BURS:PHAS?"))
        
    def source(self, trigSource):
        funcgen.write("TRIG:SOUR: " + trigSource)
        print(funcgen.query("TRIG:SOUR?"))
        
    def slope(self, trigSlope):
        funcgen.write("TRIG:SLOP " + trigSlope)
        print(funcgen.query("TRIG:SLOP?"))

    #state is ON or OFF
    def state(self, burstState):  
        funcgen.write("BURS:STAT " + burstState)
        print(funcgen.query("BURS:STAT?")

    def outputSlope(self, trigOutputSlope):
        fungen.write("OUTP:TRIG:SLOP " + trigOutputSlope)
        print(funcgen.query("OUTP:TRIG:SLOP?")
    
    def output(self, trigOutput):
        funcgen.write("OUTP:TRIG " + trigOutput)
        print(funcgen.query("OUTP:TRIG?")
        


class gat():
    #constructor
    def __init__(self):
        self.mode = "GAT"
        funcgen.write("BURS:MODE " + self.mode)
        print(funcgen.query("BURS:MODE?"))
            
    def phase(self, burstPhase):
        funcgen.write("BURS:STAT " + burstPhase)
        print(funcgen.query("BURS:PHAS?"))

    def state(self, burstState):  #state is ON or OFF
        funcgen.write("BURS:STAT " + burstState)
        print(funcgen.query("BURS:STAT?")
        
    def pol(self, polarity):
        funcgen.write("BURS:GAT:POL " + polarity)
        print(funcgen.write("BURS:GAT:POL?"))

    def outputSlope(self, trigOutputSlope):
        fungen.write("OUTP:TRIG:SLOP " + trigOutputSlope)
        print(funcgen.query("OUTP:TRIG:SLOP?")


    def output(self, trigOutput):
        funcgen.write("OUTP:TRIG " + trigOutput)
        print(funcgen.query("OUTP:TRIG?")


    
obj = trig()
obj.count("1000")
obj.period("10")
obj.phase("30")
obj.state("ON")

#The next line resets the function generator
#funcgen.write("*RST")


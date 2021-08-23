# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:58:06 2021

@author: Andrew Kille - SpellerLab
@email: killeandrew@gmail.com

Title: Agilent 33220A Function Generator Waveform
This script is intended to customize and generate a waveform on the Aligent 33220A Function Generator. For a more detailed description, see the Aligent Function Generator readMe file.
"""

import pyvisa

rm = pyvisa.ResourceManager()
#print(rm.list_resources())

funcgen = rm.open_resource('#USB')  #Insert USB serial number here

print("Instrument loaded is:")
print(funcgen.query("*IDN?"))

#this function generates the waveform; the user can choose the customize each setting (function, frequency, amplitude, offset) or leave it as the default value
def apply(func="DEF", freq="DEF", amp="DEF", offset="DEF"):
    funcgen.write("APPL:" + self.func + ", " + self.freq + ", " + self.amp + ", " + self.offset)
    print(funcgen.query("APPL?"))

#example command
apply("SQU", "10 kHz")

#the next line resets the function generator
#funcgen.write("*RST")

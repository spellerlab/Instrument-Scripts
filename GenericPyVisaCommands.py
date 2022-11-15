# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:21:54 2022

@author: SpellerLab
"""

import pyvisa

def MakeResourceManager():
    rm = pyvisa.ResourceManager()
    return rm 


def PrintAvailableInstruments(ResourceManager):
        print(ResourceManager.list_resources())
        
def LoadInstrument(ResourceManager, inst):
    # syntax: LoadInstrument(<resource manager object>, 'instrument name found from PrintAvailableIstruments')
        
    instrument = ResourceManager.open_resource(inst)
    print(str(instrument.query('*IDN?'))+" IS LOADED INTO RESOURCE MANAGER")
    return instrument     

def ResetInstrument(instrument):
    
    instrument.write('*RST')
    print("RESET "+str(instrument.query('*IDN?')))

#rm = MakeResourceManager()
#dmm = LoadInstrument(rm, 'USB0::0x05E6::0x6500::04485760::INSTR')


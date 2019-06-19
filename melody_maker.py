#!/usr/bin/env python

import random
from melopy import melopy
from melopy import Melopy

def main(): 
    timeSig = str(raw_input("Enter desired time signature (x/x): "))

    while timeSig.find("/") == -1:
        timeSig = str(raw_input("Time signature must contain a '/'. Please reenter: "))

    timeCount = timeSig.split("/")
    total = int(timeCount[0]) ##top of time signature; amount of beats to generate
    beat = int(timeCount[1])  ##bottom of time signature; what constitutes a single beat       
    inputKey = raw_input("Enter desired key (X Major/X Minor): ")
    note = inputKey[0:2].strip() ##Note can be 1-2 chars.. G, G# etc..

    m = Melopy('generated_clip')

    keys = None

    ## checking if input key is minor/major and calling corresponding Melopy method
    if inputKey.upper().find("MINOR") != -1:
        keys = melopy.generateScale("melodic_minor", note)
    elif inputKey.upper().find("MAJOR") != -1:
        keys = melopy.generateScale("major", note)

    ##calling recursive method with 'curr' parameter as 0, and the list of note time values we will be using
    generated(total, 0, ["semiquaver", "quaver", "quarter", "half"], keys, m, beat)

    m.render()

##recursively generates and adds random notes until current time count = total time count. if we overshoot, reset and re-call
def generated(total, curr, timeVals, keys, m, beat):
    print(total, curr, beat)
    timeValue = timeVals[random.randint(0,len(timeVals)-1)] ##picking random value from time signature list
    noteValue = keys[random.randint(0, len(keys)-1)] ##picking random note from input key
    curr += int(addNote(timeValue, noteValue, m, beat))
    if curr < total:
        generated(total, curr, timeVals, keys, m, beat)
    elif curr > total:
        curr = 0
        m = Melopy("generated_clip")
        generated(total, curr, timeVals, keys, m, beat)
    
    
##adding noteValue with timeValue to melopy object and returning generated beat value to calling method
def addNote(timeValue, noteValue, m, beat): 
    print(timeValue, noteValue, beat)

    ##TODO: map here instead
    ##mapping generated timeValues to corresponding Melopy methods and multiplying timeValue by the beat to get the relative beat value
    if timeValue == "semiquaver":
        m.add_sixteenth_note(noteValue)
        return float((1.0/16)) * beat
    if timeValue == "quaver":
        m.add_eighth_note(noteValue)
        return float((1.0/8)) * beat
    if timeValue == "quarter":
        m.add_quarter_note(noteValue)
        return float((1.0/4)) * beat
    if timeValue == "half":
        m.add_half_note(noteValue)
        return float((1.0/2)) * beat
    return -1;
    
if __name__== "__main__": main()
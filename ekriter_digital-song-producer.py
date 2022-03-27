#Evey Kriter/CSCI0101/11.1.2019/Lab 7

import middsound
import math

def append_tone(snd, freq, duration):
    '''adds (duration) of a pure tone at frequency (freq) to sound (snd)'''
    num_samples = int(snd.framerate * duration)
    
    for i in range(num_samples):
        sample = int(math.sin(2 * math.pi * freq * (i/snd.framerate))* middsound.MAXVALUE)
        snd.append(sample)

def make_song(notes):
    '''a function that outputs songs'''
    snd = middsound.new()
    while len(notes) > 0: #parsing the notes string
        if notes[0] == " ":
            append_tone(snd, 0 , 0.1)
            notes = notes[1:]
        else:
            append_tone(snd, middsound.get_frequency(notes[0:2]), 0.25)
            notes = notes[2:]
    return snd

x = middsound.new()
x = make_song("c5 c5 c5 g4 a4 a4 g4      e5 e5 d5 d5 c5   g4 c5 c5 c5 g4 a4 a4 g4      e5 e5 d5 d5 c5")
x.play()
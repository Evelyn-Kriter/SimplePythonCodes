#Evey Kriter/CSCI0101/11.7.2019/Homework 7

import middsound
import math

def is_sorted(seq):
    '''takes in a sequence and returns True if the sequence is in order and False if its not'''
    for i in range(len(seq[:-1])):
        if seq[i] > seq[i + 1]:
            return False
    return True

#print(is_sorted('rgwjd'))

def power(seq, exponent):
    """
    takes in a list of numbers and returns a new list where each value of the original list has been raised to the exponent
    """
    return [i ** exponent for i in seq]

#print(power([1,2,3,4,5] , 3))

def amplify(sound):
    '''returns a new sound that has doubled the amplitude of the original sound'''
    new_snd = middsound.new(framerate=sound.framerate)
    for sample in sound:
        sample = sample * 2 #amplify the sound by 2
        sample = min(sample , middsound.MAXVALUE) #These next two lines return sample if it doesn't go over/under
        sample = max(sample , middsound.MINVALUE)
        new_snd.append(sample)
    return new_snd

#snd = middsound.open('hamster.wav')
#newsound = amplify(snd)
#newsound.play()
'''
def echo(sound, delay_sec, strength):
    new_sound = middsound.new(framerate=sound.framerate) #make a new variable that we can change around
    delay = delay_sec * sound.framerate #how many frames are inside those couple seconds of delay
    for i in range(0, len(sound)+(delay*3)):
        new_sound.append(0)
    for i in range(0, math.ceil((len(sound)+(delay*3))/delay)): #for each of the generation
        if (len(sound)+(delay*4))>=len(new_sound):
            for sample in range(((len(sound)-len(sound)+(delay*3)))%len(new_sound)-1):
                new_sample = sound[sample] * (strength ** i)
                new_sound[sample + (delay * i)] = int(new_sound[sample + (delay * i)] + new_sample)
        else:
            for sample in range(len(sound)):
                new_sample = sound[sample] * (strength ** i)
                new_sound[sample + (delay * i)] = int(new_sound[sample + (delay * i)] + new_sample)
    return new_sound
        
snd = middsound.open('hamster.wav')
newsound = echo(snd, 1, 0.5)
newsound.play()
'''
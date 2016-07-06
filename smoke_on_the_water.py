__author__ = 'Sergei P. Wallace'

import sys
from music import Music


def main():

    # check for correct number of arguments
    if len(sys.argv) != 2:
        return print("This program requires one command line argument. Please give the the name of the input file.")
    m = Music(sys.argv[1])

    m.set_beat(.5)  # one beat is 0.5 seconds

    m.header()  # output the audio header

    #generate the audio data for
    #Smoke On the Water (64bit)
    #performed by Deep Purple
    #64bit optimized by
    #Sean and Peyton
    for i in range(3):
        m.play("E", i+1, 1)  # play E in octave i+1 for one beat
        m.play("G", i+1, 1)  # play G in octave i+1 for one beat
        m.play("A", i+2, 1.5)  # play A in octave i+2 for one and a half beat

        m.play("E", i+1, 1)  # play E in octave i+1 for one beat
        m.play("G", i+1, 1)  # play G in octave i+1 for one beat
        m.play("A#", i+2, .5)  # play A# in octave i+2 for a half beat
        m.play("A", i+2, 2)  # play A in octave i+1 for two beats

        m.play("E", i+1, 1)  # play E in octave i+1 for one beat
        m.play("G", i+1, 1)  # play G in octave i+1 for one beat
        m.play("A", i+2, 1.5)  # play A in octave i+2 for one and a half beat
        m.play("G", i+1, 1)  # play G in octave i+1 for one beat
        m.play("E", i+1, 2.5)  # play E in octave i+1 for two and a half beats

main()
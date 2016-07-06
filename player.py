__author__ = 'Sergei Wallace'

import sys
from music import Music



def main():
    # check for correct number of arguments
    if len(sys.argv) < 2:
        return print("This program requires one command line argument. Please give the the name of the input file.")

    m = Music(sys.argv[1])
    m.set_beat(0.25)  # one beat is 0.5 seconds

    m.header()  # output the audio header

    # generate the audio data
    m.play("C", 3, 1)  # play C in octave 3 for one beat

    m.play("D", 3, 2)  # play D in octave 3 for two beats


main()

__author__ = 'Sergei P. Wallace'

import math, sys
from collections import Counter


class Music():

    def __init__(self, file):
        self.beat = 0.25  # default beat - 0.25 seconds
        self.frequency = 261.62556530  # default frequency - middle C
        self.octave = 3  # default octave - 3
        with open(file) as f:
            self.array = f.read().splitlines()  # read dat file into array
            self.array = list(map(int, self.array))
        f.close()
        self.notes = {"A": -3, "A#": -2, "B": -1, "C": 0, "C#": 1, "D": 2, "D#": 3}
        notes1 = {"E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8}
        self.notes.update(notes1)

    def set_beat(self, beat):
        self.beat = beat

    def header(self):
        sys.stdout.write("RRAUDIO\n%%\n")

    def play(self, note, octave, beats):
        self.frequency = 261.62556530 * math.sqrt(2)**((1/12)*((octave - self.octave)*12+self.notes[note]))
        sample_rate = len(self.array)
        cycle = sample_rate/self.frequency
        sample_total = sample_rate*beats*self.beat
        repetitions = int(sample_total/self.frequency)
        '''
        print("sample rate =", sample_rate)
        print("note: ", note, ", octave: ", octave, ", frequency: ", self.frequency, sep="")
        print("cycles =", int(cycle))
        print("number of beats:", beats)
        print("beat duration = ", self.beat)
        print("total samples = ", sample_total)
        print("repetitions = ", repetitions)
        '''
        for i in range(repetitions):
            for j in range(int(cycle)):
                sys.stdout.write(str(self.array[j])+"\n")
            #print("\n-beat-\n")
        #print()


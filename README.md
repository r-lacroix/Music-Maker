# Music-Maker
Terminal script to generate a melody as a wav file given a time signature and key from the user. Using jdan's Melopy library (https://github.com/jdan/Melopy) to convert to wav file and to generate scales.

Built to help musicians write melodies/riffs, especially in odd time signatures

The script takes in a time signature and uses the numerator as the amount of beats to generate, and the denominator as what constitutes one beat. It will pick a random note from the key the user entered (this scale is generated from the Melopy library), and a completely random time value for the note and repeat this process recursively until it hits the number of beats specified in the numerator of the time signature. The result will be a .wav file containing 1 randomly generated measure within the specified criteria

This code uses a completely random approach. If it overshoots the time signature it completely resets its progress. This is not a big performance concern for now, but for a #TODO, on each iteration I'd like to calculate the remaining beats to finish the measure and then limit the time values of the generated notes to values smaller than the remainder

Currently the smallest note it will generate is a sixteenth note and the largest it will generate is a half note. This is intentional. The possibility of a whole note will use up too much precious space, and anything smaller than a a sixteenth note might crowd it too much.





# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:24:32 2013

@author: NotMark
"""

from math import sqrt, ceil, floor
import string, itertools

def xyloMaker (t = .12, matl = 'Aluminum', scale = [24, 25, 26]):
  
    # Dictionary of materials. Stores the modulus and density as the value
    # of each material key. [modulus, density]
    
    v_sound = 343.7 #m/s
    
    materialList = {'aluminum': [69e9, 2700], 
                    'steel': [30, 12],
                    'oak': [10, 2],
                    'maple': [12, 2.5]
                    }
    
    try:
        
        E, p = materialList[matl.lower()]
    
    except(KeyError):
        
        print 'Material \'' + matl + '\' undefined. Please select from ' + \
                ', '.join(materialList.keys())
        print 'Exiting ...'
        
        return
        
    t_m = t * .0254
        
    c = 1.028 * t_m * sqrt(E / p)
    
    L = [sqrt(c / f) for f in scale]
    
    L_in = [i/.0254 for i in L]    
    
    tube_L_in = [v_sound / (4.0 * f * .0254)  for f in scale]
    
    return [ ("%.3f" % a, "%.3f" % b, "%.3f" % c) for a, b, c 
                in zip(L_in, tube_L_in, scale) ]
        
    
def makeScale(rootNote = 'B2', key = 'major', length = 8):
    
    f0 = 440    #A 440 Hz
    noteMap = ['C', 'Cs', 'D', 'Eb', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'Bb', 'B']
    majorIntervals = [2, 2, 3, 2, 3]
    minorIntervals = [3, 2, 2, 3, 2]
    
    if key == 'major':
        multiplier = ceil(length / float(len(majorIntervals)))
        scaleIntervals = majorIntervals * int(multiplier)

    elif key == 'minor':
        multiplier = ceil(length / float(len(minorIntervals)))
        scaleIntervals = minorIntervals * int(multiplier)
       
    scaleIntervals = scaleIntervals[:length-1]
   
    note = rootNote.rstrip('0123456789').capitalize()
    octave = int(rootNote.lstrip(string.ascii_letters))
    
    noteDiff = noteMap.index(note) - noteMap.index('A')
    octaveDiff = octave - 4
    
    interval = noteDiff + 12 * octaveDiff    
    
    noteFreq = f0 * 2.0 ** (interval/12.0)
    
    
    fuckingfuckyou = []    

    for i in range(len(scaleIntervals)):
        if i == 0:
            fuckingfuckyou.append(scaleIntervals[i])
        else:
            fuckingfuckyou.append(scaleIntervals[i] + fuckingfuckyou[i-1])
        
    print fuckingfuckyou
    
    finalshit = [f0 * 2.0 ** ((i+interval)/12.0) for i in fuckingfuckyou]
    finalshit.insert(0, noteFreq)    
    print finalshit
    
    print note + str(octave) + ': ' + str(noteFreq)
    
    return finalshit
    
def noteSearch(freq):
    
    freq = float(freq)

    pianoScale = [
    
        [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87],
        [32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74],
        [65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5],
        [130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.7, 220.0, 233.1, 246.9],
        [261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9],
        [523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8],
        [1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976],
        [2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951],
        [4186, 4435, 4699, 4978, 5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902]
    
        ]
        
    flatscale = list(itertools.chain.from_iterable(pianoScale))
    
    closestFreq = min(flatscale, key = lambda x: abs(x - freq))
    freqIndex = flatscale.index(closestFreq)
    
    freqOctave = floor(freqIndex / 12)
    freqNote = freqIndex % 12
    
    noteMap = ['C', 'Cs', 'D', 'Eb', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'Bb', 'B']
    
    return str(noteMap[freqNote]) + str(int(freqOctave))


xylophone = xyloMaker(.12, 'aluminum', makeScale('Fs2', 'major', 5))

f = open('xylo.html', 'w')

f.write('<html>\n<head>')
f.write('<style type=\'text/css\'>')
f.write('h2 {line-height: 50%; margin-top: 30px; background: #EEE; width: 275px}')
f.write('h3 {line-height: 25%} body {font-family: arial; margin: 0 0 0 50px; background: #222}')
f.write('.realBody {background: #FFFFFF; width: 300px; padding: 15px}')
f.write('</style>\n<body><div class="realBody">')
f.write('<img src=\'http://icons.iconarchive.com/icons/visualpharm/ios7v2/256/Music-Set-Xylophone-icon.png\'>')
f.write('<h1>Xylophone Notes</h1>')

for noteNum, lengths in enumerate(xylophone):

    f.write('<h2>Note ' + str(noteNum+1) + ': ' + noteSearch(lengths[2]) + '</h2>')
    f.write('<h3>Bar Length: ' + lengths[0] + ' in.</h3>')
    f.write('<h3>Tube Length: ' + lengths[1] + ' in.</h3>')
    f.write('<h3>Frequency: ' + lengths[2] + ' Hz.</h3>')    
    
f.close()



#pianoScale = {
#    'C':  [16.35, 32.70, 65.41, 130.8, 261.6, 523.3, 1047, 2093, 4186],
#    'Cs': [17.32, 34.65, 69.30, 138.6, 277.2, 554.4, 1109, 2217, 4435],
#    'D':  [18.35, 36.71, 73.42, 146.8, 293.7, 587.3, 1175, 2349, 4699],
#    'Eb': [19.45, 38.89, 77.78, 155.6, 311.1, 622.3, 1245, 2489, 4978],
#    'E':  [20.60, 41.20, 82.41, 164.8, 329.6, 659.3, 1319, 2637, 5274],
#    'F':  [21.83, 43.65, 87.31, 174.6, 349.2, 698.5, 1397, 2794, 5588],
#    'Fs': [23.12, 46.25, 92.50, 185.0, 370.0, 740.0, 1480, 2960, 5920],
#    'G':  [24.50, 49.00, 98.00, 196.0, 392.0, 784.0, 1568, 3136, 6272],
#    'Gs': [25.96, 51.91, 103.8, 207.7, 415.3, 830.6, 1661, 3322, 6645],
#    'A':  [27.50, 55.00, 110.0, 220.0, 440.0, 880.0, 1760, 3520, 7040],
#    'Bb': [29.14, 58.27, 116.5, 233.1, 466.2, 932.3, 1865, 3729, 7459],
#    'B':  [30.87, 61.74, 123.5, 246.9, 493.9, 987.8, 1976, 3951, 7902]
#    }
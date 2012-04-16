import random
from subprocess import call

class scoreMaker:
    """Used to creare lilypond files"""
    cantusNotes = []
    cantusValues = []
    counterNotes = []
    
    fileOutName = 'lilyFile_'+ str(random.getrandbits(32)) + '.ly'
    1,2
    
    

    def __init__(self):
        name = 'foo'

    def noteToName(note):
        note = note
        notes = ('c','cis','d','dis','e','f','fis','g','gis','a','ais','b')
        octaves = (',,,,',',,,',',,',',','','\'','\'\'')
        if (note >= 0) and( note <= 119):
            return (notes[note%12] + octaves[int(note/12)] + '1')

    
    def appendCantus(self, note):
        
        newNote = scoreMaker.noteToName(note)
        scoreMaker.cantusNotes.append('\t\t' + newNote + "\n")
        scoreMaker.cantusValues.append(note)

    def appendCounter(self, note):
        newNote = scoreMaker.noteToName(note)
        scoreMaker.counterNotes.append('\t\t' + newNote + "\n")
        

    def write():
        fileOut = open(scoreMaker.fileOutName, "w+")
        fileOut.write('\\score {\n')
        fileOut.write('\t\\new Staff << \n')
        fileOut.write('\t\\new Voice {\n')
        fileOut.write('\t\\set midiInstrument = #\"clarinet"\n')
        fileOut.write('\t\\time 4/4\n')
        fileOut.write('\t\\voiceOne\n')
        fileOut.write('\t\t\\clef treble {\n')
        for x in scoreMaker.counterNotes:
            fileOut.write(str(str(x)))
        fileOut.write('\t\t}\n')
        fileOut.write('\t}\n')
        fileOut.write('\t\t\\new Staff\n')
        fileOut.write('\t\\new Voice {\n')
        fileOut.write('\t\\set midiInstrument = #\"clarinet"\n')
        if sum(scoreMaker.cantusValues) > 60:
            fileOut.write('\t\t\\clef bass {\n')
        else:
            fileOut.write('\t\t\\clef bass {\n')
        fileOut.write('\t\\voiceTwo\n')
        for x in scoreMaker.cantusNotes:
            fileOut.write(str(str(x)))
        fileOut.write('\t\t}\n')
        fileOut.write('\t}\n')
        fileOut.write('>>\n')
        fileOut.write('\\layout {}\n')
        fileOut.write('\\midi {\n')
        fileOut.write('\\context {\n')
        fileOut.write('\\Staff \n')
        fileOut.write('\\remove \"Staff_performer\" \n')
        fileOut.write('\t}\n')
        fileOut.write('\\context {\n')
        fileOut.write('\\Voice \n')
        fileOut.write('\\consists \"Staff_performer\" \n')
        fileOut.write('\t}\n')
        fileOut.write('\\context {\n')
        fileOut.write('\\Score \n')
        fileOut.write('tempoWholesPerMinute = #(ly:make-moment 72 2)\n')
        fileOut.write('\t}\n')
        fileOut.write('\t}\n')
        fileOut.write('\t}\n')
        print('file was written- ' + scoreMaker.fileOutName)
        fileOut.close()
        z = call(["/Applications/LilyPond.app/Contents/Resources/bin/lilypond", scoreMaker.fileOutName])
        print(z)
        


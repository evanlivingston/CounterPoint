import random

class scoreMaker:
    """Used to creare lilypond files"""
    cantusNotes = []
    counterNotes = []
    fileOutName = 'lilyFile_'+ str(random.getrandbits(32)) + '.ly'
    
    
    

    def __init__(self):
        name = 'foo'

    def noteToName(note):
        note = note
        notes = ('c','cis','d','dis','e','f','fis','g','gis','a','ais','b')
        octaves = (',,,',',,',',','','\'','\'\'','\'\'\'')
        if (note >= 0) and( note <= 119):
            return (notes[note%12] + octaves[int(note/12)] + '1')

    
    def appendCantus(self, note):
        
        newNote = scoreMaker.noteToName(note)
        scoreMaker.cantusNotes.append('\t\t' + newNote + "\n")

    def appendCounter(self, note):
        newNote = scoreMaker.noteToName(note)
        scoreMaker.counterNotes.append('\t\t' + newNote + "\n")
        

    def write(self):
        fileOut = open(scoreMaker.fileOutName, "w+")
        fileOut.write('\\version \"2.15.36\"\n')
        fileOut.write('\\score {\n')
        fileOut.write('\t<< \n')
        fileOut.write('\t\t\\new Staff {\n')
        fileOut.write('\t\t\\clef treble\n')
        fileOut.write('\t\t{\n')
        for x in scoreMaker.counterNotes:
            fileOut.write(str(str(x)))
        fileOut.write('\t\t}\n')
        fileOut.write('\t}\n')
        fileOut.write('\t\t\\new Staff {\n')
        fileOut.write('\t\t\\clef tenor\n')
        fileOut.write('\t\t{\n')
        for x in scoreMaker.cantusNotes:
            fileOut.write(str(str(x)))
        fileOut.write('\t\t}\n')
        fileOut.write('\t}\n')
        fileOut.write('>>\n')
        fileOut.write('}\n')
        print('file was written')
        fileOut.close()
        
        


init python:
    pos1 = 660
    pos2 = 860
    pos3 = 1060
    pos4 = 1260
    beat = 0.72289156626 # 83 bpm, valid for the first song
    offset = 1.666666666667

    def addNote(timing, position):
        sprites.append(RhythmD(Text("O"), 20, (timing*beat)-offset, position))

    def chart1():
        addNote(9.35, pos1)
        addNote(9.85, pos3)
        addNote(10.35, pos3)
        addNote(14.35, pos4)
        addNote(14.85, pos3)
        addNote(15.35, pos2)
        addNote(15.85, pos3)
        addNote(16.35, pos2)
        addNote(16.85, pos1)
        addNote(17.35, pos2)
        addNote(18.35, pos3)
        addNote(18.85, pos3)
        addNote(20.85, pos1)
        addNote(21.35, pos2)
        addNote(22.85, pos1)
        addNote(23.35, pos2)
        addNote(23.85, pos3)
        addNote(24.35, pos3)
        addNote(24.85, pos4)
        addNote(25.35, pos2)
        addNote(26.35, pos3)
        addNote(26.85, pos3)
        addNote(28.85, pos2)
        addNote(29.35, pos4)
        addNote(30.35, pos1)
        addNote(31.35, pos3)
        addNote(32.85, pos4)
        addNote(33.35, pos3)
        addNote(34.35, pos1)
        addNote(34.85, pos1)
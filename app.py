testpoem = '''The Moving Finger writes; and, having writ, Moves on: 
nor all thy Piety nor Wit. Shall lure it back to cancel half a Line, 
Nor all thy Tears wash out a Word of it.'''


lines = testpoem.split("\n")
lines.reverse()

for poem in lines:
    print(poem)
#problem 1
#Pattern Matching
#Finds all of the occurences of a pattern in a string

Genome = ''
Pattern = ''

lenGenome = len(Genome)
lenPattern = len(Pattern)

output = ''
currentPat =''
x = 0

for i in range (0, (lenGenome - lenPattern +1)):
    currentPat = Genome[i]
    x = i + 1
    for y in range (0,lenPattern-1):
        currentPat = currentPat + Genome[x]
        if str(currentPat) == Pattern:
            index = i
            output = output + str(index) + ' '
        x = x + 1
        y = y + 1
    currentPat = ''
    i = i + 1

print output

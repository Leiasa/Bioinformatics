#problem2
#finds the most frequent words in a string

text = ''
k = 14 #words length of k

# helper method Pattern Counter 
def patterncount(Text, Pattern):
    lenText = len(Text)
    lenPattern = len(Pattern)
    count = 0
    currentPat =''
    x = 0
    for i in range (0, (lenText - lenPattern +1)):
        currentPat = Text[i]
        x = i + 1
        for y in range (0,lenPattern-1):
            currentPat = currentPat + Text[x]
            if str(currentPat) == Pattern:
                count = count + 1
            x = x + 1
            y = y + 1
        currentPat = ''
        i = i + 1
    return count

freqpatt = []
newarray = []
countarray = []
maxcount = 0
output = ''

for i in range (0, len(text)):
    countarray.append(0)

for i in range(0, len(text) - k):
    pattern = text[i: i + k]
    countarray[i] = patterncount(text, pattern)
for i in countarray:
    if i > maxcount:
        maxcount = i
for i in range (0, len(text) - k):
    if countarray[i] == maxcount:
        freqpatt.append(text[i: i + k])
        
outputarray = list(set(freqpatt))
    

                
for word in outputarray:
    output = output + str(word) + ' '

print output

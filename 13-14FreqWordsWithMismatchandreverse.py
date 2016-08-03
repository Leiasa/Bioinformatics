#correct/ working one




#### helper methods #####

# Computes the hamming distance between two strings
def hammdist(pattern, pattern2):
    pattern_len = len(pattern)
    pattern2_len = len(pattern2)
    counter = 0
    for i in range(0,pattern_len):   
        current1 = pattern[i]
        current2 = pattern2[i]
        if current1 != current2:
            counter = counter + 1
    return counter

# start approximate counter
def approxpatcount(text, pattern, d):
    count = 0
    for i in range (0, len(text) - len(pattern) + 1 ):
        pattern2 = text[ i : i + len(pattern)]
        if hammdist(pattern, pattern2) <= d:
            count = count + 1
    return count

# generates the d-neighborhood of a k-mer pattern recursive way
def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = []
    firstsymbol = pattern[0]
    suffix = pattern[1:]
    suffixNeighbors = neighbors(suffix, d)
    for text in suffixNeighbors:
        if hammdist(suffix, text) < d:
            for x in 'ACGT':
                toadd = x + text
                neighborhood.append(toadd)
        else:
            toadd = firstsymbol + text
            neighborhood.append(toadd)
    return neighborhood

def patterntonumber(pattern):
    if pattern == '':
        return 0
    lenpattern = len(pattern)
    lastsymbol = pattern[lenpattern - 1]
    pattern = pattern[:-1]
    prefix = pattern
    return ((int(4) * patterntonumber(prefix)) + symboltonumber(lastsymbol))

#helper method symbol to number
def symboltonumber(symbol):
    if symbol == "A":
        return 0
    
    elif symbol == "C":
        return 1
        
    elif symbol == "G":
        return 2
        
    elif symbol == "T":
        return 3

def numbertopattern(index, k):
    prefixindex = (index / 4)
    r = (index % 4)
    symbol = numbertosymbol(r)
    if k == 0:
        return '' # base case to break recursion 
    prefixpattern = numbertopattern(prefixindex, k-1)
    return prefixpattern + symbol
    
#helper method
def numbertosymbol(index):
    if index == 0:
        return "A"
    
    elif index == 1:
        return "C"
        
    elif index == 2:
        return "G"
        
    elif index == 3 :
        return "T"

# Complementing a strand of DNA
def compleDNA(dna):
    cDNA= ""
    numb_Nucle = len(dna)
    #make complement DNA
    for i in range( 0, numb_Nucle):
        current = dna[i]
        if current == "A":
            cDNA += "T"
        elif current == "C":
            cDNA += "G"
        elif current == "G":
            cDNA += "C"
        elif current == "T":
            cDNA += "A"        
    leng_cDNA = len(cDNA)
    current2 = leng_cDNA - 1
    ccDNA = ""
    #Print complement DNA in reverse
    for x in range ( 0, leng_cDNA):  
        ccDNA += str(cDNA[current2])
        current2 = current2 - 1
    return ccDNA 
    
    
##### start function #####
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
text2 = compleDNA(text)

k = 4
d = 1

freqpattern = []
close = []
maxcount = 0

def function(text):
    freqarray = []
    for i in range (0, (4**k)):
        close.append(0)
        freqarray.append(0)
    
    for i in range (0, len(text)- k + 1):
        neighborhood = neighbors(text[i: i+ k], d)
        for pattern in neighborhood:
            index = patterntonumber(pattern)
            close[index] = 1
        
    for i in range (0, (4**k - 1)):
        if close[i] == 1:  
            pattern = numbertopattern(i,k)
            freqarray[i] = approxpatcount(text, pattern, d)
    return freqarray


freqarray1 = function(text)
freqarray2 = function(text2)
freqarray3 = [x + y for x,y in zip(freqarray1, freqarray2)]

for i in freqarray3:
    if i > maxcount:
        maxcount = i

for i in range (0, (4**k - 1)):
    if freqarray3[i] == maxcount:
        pattern = numbertopattern(i,k)
        freqpattern.append(pattern)

output = ''
for freq in freqpattern:
        output = output + str(freq) + ' '

f = open('output5.txt', 'w')
f.write(output) 
print output


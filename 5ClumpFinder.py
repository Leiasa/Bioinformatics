#problem 5
# the better clump finder pseudo code from the book
#Finds all patterns forming clumps in a string
#input: string genome, integers k,L,t
#output: all distinct k-mers forming (L,t)-clumps in genome



genome = ''
k = 10  #length of patterns
L = 585  #fixed length in genome
t = 20 #how many clumps
lengenome = len(genome)



###### START HELPER METHODS #######

# helper method pattern to number 
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
#helper method freq array 
def computingfreq(Text, k):
    array = []
    for i in range (0, (4**k)):
        array.append(0)
    for i in range (0, (len(Text) - k +1)):
        pattern = Text[ i : i + k]
        j = patterntonumber(pattern)
        array[j] = array[j] + 1                                   
    return array 

#helper method number to pattern
def numbertopattern(index, k):
    prefixindex = (index / 4)
    r = (index % 4)
    symbol = numbertosymbol(r)
    if k == 0:
        return '' # base case to break recursion 
    prefixpattern = numbertopattern(prefixindex, k-1)
    return prefixpattern + symbol
    
#helper method number to symbol
def numbertosymbol(index):
    if index == 0:
        return "A"
    
    elif index == 1:
        return "C"
        
    elif index == 2:
        return "G"
        
    elif index == 3 :
        return "T"

###### START FUNCTION #######
def clumpfind(genome, k,t,L):
    freqpatterns = []
    freqarray = []
    clump = []
    output = ''

    for i in range (0, ((4**k) - 1)):
        clump.append(0)
    text = genome[0: 0 + L]
    freqarray = computingfreq(text, k)
    
    for i in range (0, ((4**k) - 1)):
            if freqarray[i] >= t:
                clump[i] = 1 # check for error here
    
    
    for i in range (0, (lengenome - L + 1)):
        firstpattern = genome[i-1: ((i-1)+k)]
      
        index = patterntonumber(firstpattern)
        freqarray[index] = freqarray[index] - 1
        lastpattern = genome[i+L-k: ((i+L-k) + k)]
     
        index = patterntonumber(lastpattern)
        freqarray[index] = freqarray[index] + 1
        if freqarray[index] >= t:
                clump[index] = 1        
            
    for i in range (0, ((4**k) - 1)):
        if clump[i] == 1:
            pattern = numbertopattern(i,k)
            freqpatterns.append(pattern)
            
    for freq in freqpatterns:
        output = output + str(freq) + ' '
    print output           
    
clumpfind( genome, k,t,L)
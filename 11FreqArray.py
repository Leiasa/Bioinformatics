#problem 11
#creates a frequency array of a string

Text = ''
k = 8
array = []

output = ''

#pattern to number methods
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

    
for i in range (0, (4**k)):
    array.append(0)
for i in range (0, (len(Text) - k +1)):
    pattern = Text[ i : i + k]
    j = patterntonumber(pattern)
    array[j] = array[j] + 1
                                   
for freq in array:
    output = output + str(freq) + ' '
print output

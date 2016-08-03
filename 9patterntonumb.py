# pattern to number 


pattern ='AAAGAATGAAAGCGAATTCACAGGTTCT'

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

print patterntonumber(pattern)
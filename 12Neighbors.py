#problem 12
#generates the d-neighborhood of a k-mer pattern recursive way

pattern = 'GAGACTCC'
d = 3
lenpattern = len(pattern)

# helper method that computes the hamming distance between two strings
def hammdist(suffix, text):
    suffix_len = len(suffix)
    text_len = len(text)
    counter = 0
    for i in range(0,suffix_len - 1):    
        current1 = suffix[i]
        current2 = text[i]   
        if current1 != current2:
            counter = counter + 1    
    return counter

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

output = neighbors(pattern, d) 
f = open('neighboroutput.txt', 'w')


for text in output: #to print neighborhood on individual lines
    print >>f, text

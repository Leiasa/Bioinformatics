# Number to Pattern

index = 6906
k = 9

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
    

print numbertopattern(index, k)
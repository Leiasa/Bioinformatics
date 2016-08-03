#problem 3
#finds the reverse complement of dna



DNA = ""

cDNA= ""

numb_Nucle = len(DNA)


#make complement DNA
for i in range( 0, numb_Nucle):
    
    current = DNA[i]

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

#print complement DNA in reverse
for x in range ( 0, leng_cDNA):
   
    ccDNA += str(cDNA[current2])
    current2 = current2 - 1
    
print ccDNA    
    



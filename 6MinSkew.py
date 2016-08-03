#problem 6
#find the position in a genome of the minimum skew 

DNA = ""


numb_Nucleo = len(DNA)
count = 0
countarray = []
minSkew = 0 
output = ''

for i in range(0,numb_Nucleo):
    current = DNA[i]  
    if current == "C":
        count = count - 1
        countarray.append(count) 
    elif  current == "G": 
        count = count + 1
        countarray.append(count)
    elif  current == "T":
        countarray.append(count)
    elif  current == "A":
        countarray.append(count)

for i in range(0, len(countarray)):
    if countarray[i] < minSkew:
        minSkew = countarray[i]
    i = i + 1  
    

for i in range (0, len(countarray)):
    current = countarray[i]
    if countarray[i] == minSkew:
        output = output + str(i + 1) + ' '
    i = i + 1

print output
    
        
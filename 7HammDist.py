#problem 7 
#Computes the hamming distance between two strings

DNA1 = ""

DNA2 = ""

DNA1_len = len(DNA1)
DNA2_len = len(DNA2)

counter = 0

for i in range(0,DNA1_len):
    
    current1 = DNA1[i]
    current2 = DNA2[i]
    
    if current1 != current2:
        counter = counter + 1
    
print counter
#problem 40 
#find the highest-scoring alignemnt of two strings
#add negative -5 for indels

#scorign matrix = pam250
pam250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}

v = 'MEANLY'
w = 'PENALTY'

lengv = len(v)
lengw = len(w)

pen = -5 #penality for indel

s = [[0 for z in range(lengw+1)] for z in range(lengv+1)]
backtrack = [[0 for z in range(lengw)] for z in range(lengv)]

#inializes s to have the first row and column with the pen
def initiazescorematrix(matrix):
    lengn = len(matrix)
    lengm = len(matrix[0])
    temp = []
    for i in range (0, lengm):
        num = pen * i
        temp.append(num)
    matrix[0] = temp
    for j in range(1, lengn):
        num = pen * j
        matrix[j][0] = num
    #print matrix
    return matrix


#helper method that creates of a backtrack
def keepbacktrack(v,w):
    i =0
    j = 0
    
    for i in range(1, lengv+1):
        for j in range(1, lengw+1):
            keyi_1 = v[i-1]
            keyj_1 = w[j-1]
            s[i][j] = max(0,(s[i-1][j] + pen), (s[i][j-1] + pen), (s[i-1][j-1] + pam250[keyj_1][keyi_1]))         
                
            if s[i][j] == s[i-1][j]+ pen:
                backtrack[i-1][j-1] = 1 #down deletion
                
            elif s[i][j] == s[i][j-1]+ pen: 
                backtrack[i-1][j-1] = 2 #right insertions
               
                                
            elif (s[i][j] == (s[i-1][j-1]+ pam250[keyi_1][keyj_1])):  
                backtrack[i-1][j-1] = 3 #diagnoal  match of mismatch
                
            elif s[i][j] == 0: 
                 backtrack[i-1][j-1]  = 0 #the end part of free taxi ride 
                #condition that shows backtrack where to stop
                
    return backtrack

def globalalignment(backtrack, v, w):
    output1 = ''
    output2 = ''
    #print backtrack
    x = 0 
    y = 0
    
    #find the futherest/highest value in backtrack matrix to start from 
    #part of free taxi ride
    maxscore = 0
    for x in range(0,len(v)+1):
           for y in range(0,len(w)+1):
                if maxscore <= s[x][y]:
                    maxscore = s[x][y]
                    savex = x
                    savey = y
    
    
    #print maxbacktrack
    #print savex, savey
    #print backtrack[savex][savey]
    #u = len(backtrack[0]) -1
    #l = len(backtrack)-2
    #print l,u 
    #print backtrack[l][u]
    i = savex 
    j = savey
    
    stopped = False #to keep track of whether a free taxi ride casued the end 
    
    #print s
    #print "back"
    #print
    #print backtrack
    
    
    while i != 0 and j != 0:

        if backtrack[i-1][j-1] == 1: #down deletions
            i = i - 1
            output2 = '-' + output2
            output1 = v[i] + output1 

            
        elif backtrack[i-1][j-1] == 2: #right insertions
            j = j - 1
            output1 = '-' + output1
            output2 = w[j] + output2 
      
            
        elif backtrack[i-1][j-1] == 3: # diagnoal matches/mismatches
            output1 =  v[i-1] + output1
            output2 = w[j-1] + output2         
            i = i - 1
            j = j - 1
            
        elif backtrack[i-1][j-1] == 0: #free taxi
            #i = i - 1
            #j = j - 1
            stopped = True
            break
        
    print i, j 
    print stopped

    #add letters that didnt get added before
    k = 0        
    while (i > 0) and (stopped == False):
        output1 = v[i-1] + output1
        if len(output2) != len(output1):
            for k in range(0, i):
                output2 = '-' + output2
        i = i - 1
        
    y = 0            
    while (j > 0) and (stopped == False):
        output2 = w[j-1] + output2
        if len(output2) != len(output1):
            for k in range(0, j):
                output1 = '-' + output1
        j = j - 1
          
    print output1
    print output2
    #print len(output1), len(output2)
   
    return [output1, output2]

def scoring(output):
    string1 = output[0]
    string2 = output[1]
    score = 0
    i = 0
    for letter in string1:
        letter2 = string2[i]
        if letter == '-':
            score = score + pen
        elif letter2 == '-':
            score = score + pen
        else:
            score = score + pam250[letter][letter2]
        i = i +1
    print i            
    print score
            

#initiazescorematrix(s)
scoring(globalalignment(keepbacktrack(v,w), v, w))


#problem 43
#find the highest-scoring alignemnt of two strings
#add negative -1 for indels
# +1 for match


w = 'ATCGAGG' # v has to be longer string
v = 'TCAG'


lengv = len(v)
lengw = len(w)

pen = -1

s = [[0 for z in range(lengw+1)] for z in range(lengv+1)]
backtrack = [[0 for z in range(lengw)] for z in range(lengv)]



#helper method that creates of a backtrack
def keepbacktrack(v,w):
    i = 0
    j = 0
    
    for i in range(1, lengv+1):
        for j in range(1, lengw+1):
            keyi_1 = v[i-1]
            keyj_1 = w[j-1]
            if v[i-1] == w[j-1]:
                s[i][j] = max((s[i-1][j] + pen), (s[i][j-1] + pen), (s[i-1][j-1] + 1))         
            else:
                s[i][j] = max((s[i-1][j] + pen), (s[i][j-1] + pen), (s[i-1][j-1] - 1)) 
                
            if s[i][j] == s[i-1][j]+ pen:
                backtrack[i-1][j-1] = 1 #s[i-1][j] down
                
            elif s[i][j] == s[i][j-1]+ pen: 
                backtrack[i-1][j-1] = 2 #s[i][j-1] right
               
                                
            elif (s[i][j] == (s[i-1][j-1]+ 1)) or (s[i][j] == (s[i-1][j-1] - 1)):  
                backtrack[i-1][j-1] = 3 #s[i-1][j-1] diagnoal 
                
            #elif s[i][j] == 0: 
                 #backtrack[i-1][j-1]  = 0 #the end part of free taxi ride 
                #condition that shows backtrack where to stop
                
            else:
                 continue
    print s 
    print backtrack
    return backtrack

def fittingalignment(backtrack, v, w):
    output1 = ''
    output2 = ''
   
    j = lengw
    #stopped = False
    maxscore = - float('inf')
    x=lengw
    for x in range(lengw, lengv+1):
            if maxscore < s[x][j]:
                maxscore = s[x][j]
                savex = x
    
    i = savex
    print i,j
    #print i,j
    while j > 0:

        if backtrack[i-1][j-1] == 1: #s[i-1][j] down deletions
            i = i - 1
            output2 = '-' + output2
            output1 = v[i] + output1 #w[j-1]?
     
            
        elif backtrack[i-1][j-1] == 2: #s[i][j-1] right insertions
            j = j - 1
            output1 = '-' + output1
            output2 = w[j] + output2 #w[j-1]?
    
            
        elif backtrack[i-1][j-1] == 3: #s[i-1][j-1] diagnoal matches/mismatches
            output1 =  v[i-1] + output1
            output2 = w[j-1] + output2
            i = i - 1
            j = j - 1
        #elif backtrack[i-1][j-1] == 0: #free taxi
            #i = i - 1
            #j = j - 1
            #stopped = True
            #break
        
    
    
    print output1
    print output2
   
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
        elif letter == letter2:
            score = score + 1
        elif letter != letter2:
            score = score - 1
                              
        i = i +1
    #print i            
    print "score", score
    
    
    
#print s
scoring(fittingalignment(keepbacktrack(v,w), v, w))
#print s

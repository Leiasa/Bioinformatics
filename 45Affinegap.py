import pprint
#problem 40 
#find the highest-scoring alignemnt of two strings
#add negative -5 for indels

blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

string1 = 'DWAIIRATNAIERDHIQNIRSPWCPTSCCEDKDREVVIFGPTMIQIGYSMHTMNRLGMCGGIWFENSCSGFPDLEVR'
string2 = 'DWAIIRATNAICHIRDTYSMEYADNIRSPFGPTYIWNGETMNRLDMCGGQSWCSGFKDWEVR'
if len(string1) > len(string2):
   
    v = string1
    w = string2
else:
    print "string 2 is v so flip"
    v = string2
    w = string1


lengv = len(v)
lengw = len(w)

openpen = 11 #row / d gap opening
extpen = 1 #e pen for elongating a gap

slower = [[0 for z in range(lengw+1)] for z in range(lengv+1)] # neg inf/ eq
smiddle = [[0 for z in range(lengw+1)] for z in range(lengv+1)] # eq/ eq
supper = [[0 for z in range(lengw+1)] for z in range(lengv+1)] # eq/ neg inf

backtracklower = [[0 for z in range(lengw)] for z in range(lengv)]
backtrackmiddle = [[0 for z in range(lengw)] for z in range(lengv)]
backtrackupper = [[0 for z in range(lengw)] for z in range(lengv)]

backtrack = [backtracklower, backtrackmiddle, backtrackupper]

#initial middle matrix to have -11 around edges but the upper and lower are -1
def initiazescorematrix(matrix, pen): #NEED TO DO figure out how to initialize matrix
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

    return matrix



#helper method that creates of a backtrack
def keepbacktrack(v,w):
    i =0
    j = 0
    
    for i in range(1, lengv+1):
        for j in range(1, lengw+1):
            keyi_1 = v[i-1]
            keyj_1 = w[j-1]
            #print keyi_1, keyj_1
            #fill lower
            s[0][i][j] = max((s[0][i-1][j] - extpen), (s[1][i-1][j] - openpen)) 
            #fill middle
          
          
            #fill upper
            s[2][i][j] = max((s[2][i][j-1] - extpen), (s[1][i][j-1] - openpen))
            s[1][i][j] = max((s[0][i][j]), (s[1][i-1][j-1] + blosum62[keyj_1][keyi_1]), (s[2][i][j]))
            #fill backtrack
            #lower conditions
            
            if s[0][i][j] == s[0][i-1][j] - extpen:
                backtrack[0][i-1][j-1] = 1 # down
                
            elif s[0][i][j] == s[1][i-1][j] - openpen:
                backtrack[0][i-1][j-1] = 2 #from middle based on score to midle for backtrack 
            
            #middle conditions
                
            if s[1][i][j] == s[0][i][j]: 
                backtrack[1][i-1][j-1] = 1 #to lower
               
                                
            elif s[1][i][j] == (s[1][i-1][j-1] + blosum62[keyi_1][keyj_1]):  
                backtrack[1][i-1][j-1] = 2 #diagnoal 
                #print keyi_1, keyj_1
                
            elif s[1][i][j] == s[2][i][j]: 
                backtrack[1][i-1][j-1] = 3 #to upper
           
            #upper condtions
                
            if s[2][i][j] == s[2][i][j-1] - extpen:
                backtrack[2][i-1][j-1] = 1 #right
                
            elif s[2][i][j] == s[1][i][j-1] - openpen:
                backtrack[2][i-1][j-1] = 2 #from middle 
              
                
    return backtrack

def globalalignment(backtrack, v, w):
    output1 = ''
    output2 = ''
    i = len(v)
    j = len(w)
    #beststart = s[0][i][j]
    index = 0
    curr = s[index][i-1][j-1]
    if curr < s[1][i-1][j-1]:
        index = 1 
        curr = s[1][i-1][j-1]
    if curr <= s[2][i-1][j-1]:
        index = 2
    #print "here", index
    #need to grab starting point check all bottom right corners
    #pprint.pprint(s)
    #pprint.pprint(backtrack)
    
    #index = 2  
    while i != 0 and j != 0:
        #print i, j
        #print v[i-1], w[j-1]
        #set which matrix you are in        
        #lower conditions          
        if index == 0:
            if backtrack[index][i-1][j-1] == 1:
                index = 0
            elif backtrack[index][i-1][j-1] == 2: # down
                index = 1
            
            output2 = '-' + output2
            output1 = v[i-1] + output1
            i = i - 1
        #middle conditions
        elif index == 1:        
            if backtrack[index][i-1][j-1] == 2: # down
                index = 1
                output2 = w[j-1] + output2
                output1 = v[i-1] + output1
                i = i - 1
                j = j - 1
            elif backtrack[index][i-1][j-1] == 1: #from middle 
                index = 0
            elif backtrack[index][i-1][j-1] == 3: # down
                index = 2
            
        else: #index == 2            
            if backtrack[index][i-1][j-1] == 1: #from middle 
                index = 2
                
            elif backtrack[index][i-1][j-1] == 2: 
                index = 1
           
            output1 = '-' + output1
            output2 = w[j-1] + output2
            j = j - 1

    #print output1
    #print output2       
   
    while (i > 0):
        output1 = v[i-1] + output1
        output2 = '-' + output2
        i -= 1
        #if len(outputv) != len(outputw):
            #for k in range(0, i):
                #outputw = '-' + outputw
                   
    while (j > 0):
        output2 = w[j-1] + output2
        output1 = '-' + output1
        j -= 1
          
    
    print output1
    print output2
   
    return [output1, output2]

def scoring(output): #this works was tested
    string1 = output[0]
    string2 = output[1]
    score = 0
    i = 0
    b = 0
    prevletter = string1[0]
    for letter in string1:
        letter2 = string2[i]
        prevletter2 = string2[b]

        if letter == '-' or letter2 == '-':
            #"here"
            if letter == '-' and prevletter == '-':
                score = score - extpen               
            elif letter == '-' and prevletter != '-':
                score = score - openpen
                
            if letter2 == '-' and prevletter2 == '-':
                score = score - extpen
            elif letter2 == '-' and prevletter2 != '-':
                score = score - openpen
     
        else: # both letters not - good for match or mistmatch
            score = score + blosum62[letter][letter2]

        b = i
        prevletter = letter
        i = i +1
        
                
    print score

            
    
    
# initialize lower matrix the down matrix so that the top row is -inf and the first column is equation k is eqaul to how far down you are in the matrix    
for i in range (0, len(slower[0])):
    slower[0][i] = - float("inf")
for j in range(1, len(slower)):
    num = -11 + -1 * j
    slower[j][0] = num
    
for i in range (1, len(smiddle[0])):
    k = i + 1
    num = -11 + -1 * (k - 1)
    smiddle[0][i] = num
    
for j in range(0, len(smiddle)):
    num = -11 + -1 * j
    smiddle[j][0] = num
    
# initialize lower matrix the down matrix so that the top row is -inf and the first column is equation k is eqaul to how far down you are in the matrix 

for i in range (0, len(supper[0])):
    num = -11 + -1 * i 
    supper[0][i] = num
for j in range(1, len(supper)):
    supper[j][0] = - float("inf")


#smiddle = initiazescorematrix(smiddle, openpen)

s = [slower, smiddle, supper]

scoring(globalalignment(keepbacktrack(v,w), v, w))
#print blosum62['S']['N']

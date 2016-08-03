#shouldnt the score matrix have only 1 and 0 
#how does it decide in this case if there are so many options like if there are multiple in the max

import pprint
#w = 'ATATCCG'
#u = 'TCCGA'
#v = 'ATGTACTG'

v = 'TACCCCCATGGCGGAGCATGAGCGT'
w = 'TCGTAGCCGTGGTTGAGCTTCCGGT'
u = 'TCGACACAGTCTTGCCTTGTCGTCCAA'

lengv = len(v)
lengw = len(w)
lengu = len(u)

pen = 0
s = [[[0 for z in xrange(lengu + 1)] for z in xrange(lengw + 1)] for z in xrange(lengv +1)]
#s1 = [[0 for z in range(lengw+1)] for z in range(lengv+1)]
#s2 = [[0 for z in range(lengw+1)] for z in range(lengu+1)]
#s3 = [[0 for z in range(lengv+1)] for z in range(lengu+1)]
#s = [[s1], [s2], [s3]]
#s.append(s1)
#s.append(s2)
#s.append(s3)
#print s
backtrack = [[[0 for z in xrange(lengu)] for z in xrange(lengw)] for z in xrange(lengv)]
pen = 1


#k,i,j

#helper method that creates of a backtrack
def keepbacktrack(v, w, u):
    i = 0
    j = 0
    k = 0
    
    for i in range(1, lengv+1):
        for j in range(1, lengw+1):
            for k in range(1, lengu+1):
        
                if v[i-1] == w[j-1] and u[k-1] == w[j-1]:
                    
                    s[i][j][k] = (s[i-1][j-1][k-1] + 1) 
                else:
                     s[i][j][k] = max( (s[i-1][j][k]), (s[i][j-1][k]), (s[i][j][k-1]), (s[i-1][j-1][k]), (s[i-1][j][k-1]), (s[i][j-1][k-1]), (s[i-1][j-1][k-1]) )         
                
                if s[i][j][k] == s[i-1][j][k]:
                    backtrack[i-1][j-1][k-1] = 1 
                    
                elif s[i][j][k] == s[i][j-1][k]:
                    backtrack[i-1][j-1][k-1] = 2
                    
                elif s[i][j][k] == s[i][j][k-1]:
                    backtrack[i-1][j-1][k-1] = 3
                    
                elif s[i][j][k] == s[i-1][j-1][k]:
                    backtrack[i-1][j-1][k-1] = 4
                    
                elif s[i][j][k] == s[i-1][j][k-1]:
                    backtrack[i-1][j-1][k-1] = 5
                    
                elif s[i][j][k] == s[i][j-1][k-1]:
                    backtrack[i-1][j-1][k-1] = 6
                    
                elif s[i][j][k] == s[i-1][j-1][k-1] + 1 or s[i][j][k] == s[i-1][j-1][k-1] :
                    backtrack[i-1][j-1][k-1] = 7
                #else:
                    #continue
                
    #print s            
    return backtrack

def multiplealignment(backtrack, v, w, u):
    outputv = ''
    outputw = ''
    outputu = ''
    i = len(v)
    j = len(w)
    k = len(u)
    #pprint.pprint(s)
    #pprint.pprint(backtrack)
    while i > 0 and j > 0 and k > 0:
    #check index maybe weird   output1 = v[i] + output1 w[j-1] but was output1 =  v[i-1] + output1 for both i -1 and j-1
         
        if backtrack[i-1][j-1][k-1] == 1: #s[i-1][j][k]
            outputv = v[i-1] + outputv
            outputw = '-' + outputw
            outputu = '-' + outputu
            i -= 1
                
        elif backtrack[i-1][j-1][k-1] == 2:  #s[i][j-1][k]
            outputw = w[j-1] + outputw
            outputv = '-' + outputv
            outputu = '-' + outputu
            j -= 1
                
        elif backtrack[i-1][j-1][k-1] == 3: # s[i][j][k-1]
            outputu = u[k-1] + outputu
            outputv = '-' + outputv
            outputw = '-' + outputw
            k -= 1
                
        elif  backtrack[i-1][j-1][k-1] == 4: #s[i-1][j-1][k]
            outputv = v[i-1] + outputv
            outputw = w[j-1] + outputw
            outputu = '-' + outputu
            i -= 1
            j -= 1
               
        elif backtrack[i-1][j-1][k-1] == 5: #s[i-1][j][k-1]
            outputv = v[i-1] + outputv
            outputu = u[k-1] + outputu
            outputw = '-' + outputw
            i -= 1
            k -= 1
                
        elif backtrack[i-1][j-1][k-1] == 6: #s[i][j-1][k-1]
            outputw = w[j-1] + outputw
            outputu = u[k-1] + outputu
            outputv = '-' + outputv
            j -= 1
            k -= 1
                
        elif  backtrack[i-1][j-1][k-1] == 7: #s[i-1][j-1][k-1]
            outputv = v[i-1] + outputv
            outputw = w[j-1] + outputw
            outputu = u[k-1] + outputu
            i -= 1
            j -= 1
            k -= 1
     
    #print i, j, k                   
    #print outputv
    #print outputw
    #print outputv
    while (i > 0):
        outputv = v[i-1] + outputv
        outputu = '-' + outputu
        outputw = '-' + outputw
        i -= 1
        #if len(outputv) != len(outputw):
            #for k in range(0, i):
                #outputw = '-' + outputw
                   
    while (j > 0):
        outputw = w[j-1] + outputw
        outputu = '-' + outputu
        outputv = '-' + outputv
        j -= 1
        #if len(outputw) != len(outputu):
            #for k in range(0, j):
                #outputu = '-' + outputu
            
    while (k > 0):
        outputu = u[k-1] + outputu
        outputv = '-' + outputv
        outputw = '-' + outputw
        k -= 1
        #if len(outputu) != len(outputv):
            #for c in range(0, k):
                #outputv = '-' + outputv
          
    
    print outputv
    print outputw
    print outputu
   
    return [outputv, outputw, outputu]

def scoring(output): #tested works for multiple
    string1 = output[0]
    string2 = output[1]
    string3 = output[2]
    #print len(string1), len(string1), len(string1)
    score = 0
    i = -1
    for letter in string1:       
        i = i +1
        letter2 = string2[i]
        letter3 = string3[i]
        if letter != '-':
            if letter == letter2 and letter2 == letter3:
                score = score + 1
        else:
            continue
        
                
    print score
    
    
    

scoring(multiplealignment(keepbacktrack(v, w, u), v, w, u))


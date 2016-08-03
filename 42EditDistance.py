#problem number 42
# compute the edit distnace between two strings

#s = ['P','L','E','A','S','A','N','T','L','Y']
#t = ['M','E','A','N','L','Y']
#s = ['k','i','t','t','e','n']
#t = ['s','i','t','t','i','n','g']

first = ''
second = ''

first = list(first)
second = list(second)

firstleng = len(first)
secondleng = len(second)
subcost = 0

d  = [[0 for x in range(secondleng)] for x in range(firstleng)] #the matrix 

for i in range(1, firstleng):
    d[i][0] = i
    
for j in range(1, secondleng):
    d[0][j] = j
    
for j in range(1, secondleng):
    for i in range(1, firstleng):
        if first[i] == second[j]:
            subcost = 0
        else:
            subcost = 1
        d[i][j] = min((d[i-1][j] + 1), (d[i][j-1] + 1), (d[i-1][j-1] + subcost))

print d[(firstleng-1)][(secondleng-1)]

  
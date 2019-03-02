#BIOINFO MIDTERM Q1
import numpy


'''
Sij = max
max = Si-1, j-1 + M[X[i],Y[j]]
    = Si-1, j+gap
    = Si, j-1+gap

'''

#tacggtat
x = ['t', 'a', 'c', 'g', 'g', 't', 'a', 't']

#ggacgtacg
y = ['g', 'g', 'a', 'c', 'g', 't', 'a', 'c', 'g']

#gap = d

#          a,  c,  t,  g
matrix = [[1, -1, -1, -1], #a
          [-1, 1, -1, -1], #c
          [-1, -1, 1, -1], #t
          [-1, -1, -1, 1]] #g

def MaxScore (i, j, g):
    m2 = 0
    m3 = 0
    max = 0
    print(i-1, j-1)
    m2 = scoreTable[i][j - 1] - g
    m3 = scoreTable[i - 1][j] - g
    #a compared to all
    if (x[j-1] == 'a' and y[i-1] == 'a'):
        max = scoreTable[i - 1][j - 1] + matrix[0][0]
        print("aa")
    elif (x[j-1] == 'a' and y[i-1] == 'c'):
        max = scoreTable[i - 1][j - 1] + matrix[0][1]
        print("ac")
    elif (x[j-1] == 'a' and y[i-1] == 't'):
        max = scoreTable[i - 1][j - 1] + matrix[0][2]
        print("at")
    elif (x[j-1] == 'a' and y[i-1] == 'g'):
        max = scoreTable[i - 1][j - 1] + matrix[0][3]
        print("ag")
    #c paired to all
    elif (x[j-1] == 'c' and y[i-1] == 'a'):
        max = scoreTable[i - 1][j - 1] + matrix[1][0]
        print("ca")
    elif (x[j-1] == 'c' and y[i-1] == 'c'):
        max = scoreTable[i - 1][j - 1] + matrix[1][1]
        print("cc")
    elif (x[j-1] == 'c' and y[i-1] == 't'):
        max = scoreTable[i - 1][j - 1] + matrix[1][2]
        print("ct")
    elif (x[j-1] == 'c' and y[i-1] == 'g'):
        max = scoreTable[i - 1][j - 1] + matrix[1][3]
        print("cg")
    #t compared to all
    elif (x[j-1] == 't' and y[i-1] == 'a'):
        max = scoreTable[i - 1][j - 1] + matrix[2][0]
        print("ta")
    elif (x[j-1] == 't' and y[i-1] == 'c'):
        max = scoreTable[i - 1][j - 1] + matrix[2][1]
        print("tc")
    elif (x[j-1] == 't' and y[i-1] == 't'):
        max = scoreTable[i - 1][j - 1] + matrix[2][2]
        print("tt")
    elif (x[j-1] == 't' and y[i-1] == 'g'):
        print("tg")
        max = scoreTable[i - 1][j - 1] + matrix[2][3]
    #g compared to all
    elif (x[j-1] == 'g' and y[i-1] == 'a'):
        max = scoreTable[i - 1][j - 1] + matrix[3][0]
        print("ga")
    elif (x[j-1] == 'g' and y[i-1] == 'c'):
        max = scoreTable[i - 1][j - 1] + matrix[3][1]
        print("gc")
    elif (x[j-1] == 'g' and y[i-1] == 't'):
        max = scoreTable[i - 1][j - 1] + matrix[3][2]
        print("gt")
    elif (x[j-1] == 'g' and y[i-1] == 'g'):
        max = scoreTable[i - 1][j - 1] + matrix[3][3]
        print("gg")

    if(m2 > m3):
        if(m2 > max):
            max = m2
    elif(m3 > m2):
        if(m3 > max):
            max = m3

    # if (i == 1 and j == 2):
    #     print(m2, m3, max)
    #     print("HERE")
    return max



score = 0

scoreTable = numpy.zeros(shape=(len(y)+1, len(x)+1), dtype=int)
#            r  c
# scoreTable[0][1] = 1

print(scoreTable)
if(len(x)<len(y)):
    g = len(y) - len(x)
elif(len(y)< len(x)):
    g = len(x) - len(y)
elif(len(x) == len(y)):
    g = 0

for i in range(0, len(y)+1):
    for j in range(0, len(x)+1):
        #NOT A BASE CASE
        if(i != 0 and j != 0):
            score = MaxScore(i, j, g)
            scoreTable[i][j] = score
        #BASE CASE
        if(i == 0):
            scoreTable[i][j] = j * -1
        #BASE CASE
        elif(j == 0):
            scoreTable[i][j] = i * -1
        print(scoreTable, "\n")

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
#print("A[1] =", matrix[1][1])



def MaxScore (s, d, g,):
    m1 = 0
    m2 = 0
    m3 = 0
    max = 0

    print(i)
    #a compared to all
    if (x[s] == 'a' and y[s] == 'a'):
        print(s,d)
        print(x[i],y[i])
        m1 = scoreTable[s - 1][d - 1] + matrix[0][0]
    elif (x[s] == 'a' and y[s] == 'c'):
        m1 = scoreTable[s - 1][d - 1] + matrix[0][1]
    elif (x[s] == 'a' and y[s] == 't'):
        m1 = scoreTable[s - 1][d - 1] + matrix[0][2]
    elif (x[s] == 'a' and y[s] == 'g'):
        m1 = scoreTable[s - 1][d - 1] + matrix[0][3]
    #c paired to all
    elif (x[s] == 'c' and y[s] == 'a'):
        m1 = scoreTable[s - 1][d - 1] + matrix[1][0]
    elif (x[s] == 'c' and y[s] == 'c'):
        m1 = scoreTable[s - 1][d - 1] + matrix[1][1]
    elif (x[s] == 'c' and y[s] == 't'):
        m1 = scoreTable[s - 1][d - 1] + matrix[1][2]
    elif (x[s] == 'c' and y[s] == 'g'):
        m1 = scoreTable[s - 1][d - 1] + matrix[1][3]
    #t compared to all
    elif (x[s] == 't' and y[s] == 'a'):
        m1 = scoreTable[s - 1][d - 1] + matrix[2][0]
    elif (x[s] == 't' and y[s] == 'c'):
        m1 = scoreTable[s - 1][d - 1] + matrix[2][1]
    elif (x[s] == 't' and y[s] == 't'):
        m1 = scoreTable[s - 1][d - 1] + matrix[2][2]
    elif (x[s] == 't' and y[s] == 'g'):
        m1 = scoreTable[s - 1][d - 1] + matrix[2][3]
    #g compared to all
    elif (x[s] == 'g' and y[s] == 'a'):
        m1 = scoreTable[s - 1][d - 1] + matrix[3][0]
    elif (x[s] == 'g' and y[s] == 'c'):
        m1 = scoreTable[s - 1][d - 1] + matrix[3][1]
    elif (x[s] == 'g' and y[s] == 't'):
        m1 = scoreTable[s - 1][d - 1] + matrix[3][2]
    elif (x[s] == 'g' and y[s] == 'g'):
        m1 = scoreTable[s - 1][d - 1] + matrix[3][3]

    max = m1
    m2 = scoreTable[s - 1][d] - g
    m3 = scoreTable[s][d - 1] - g
    if(max < m2):
        max = m2
    elif(max < m3):
        max = m3

    # print(m1, m2, m3, max)
    return max



total = 0
score = 0
temp = 0

scoreTable = numpy.zeros(shape=(len(x), len(y)), dtype=int)

if(len(x)<len(y)):
    g = len(y)- len(x)
elif(len(y)< len(x)):
    g = len(x)- len(y)
elif(len(x) == len(y)):
    g = 0

for i in range(len(x)):
    for j in range(len(y)):
        #NOT A BASE CASE
        if(i != 0 and j != 0):
            score = MaxScore(i, j, g)
            scoreTable[i][j] = score
        #BASE CASE
        elif(i == 0):
            scoreTable[i][j] = j * -1
        #BASE CASE
        elif(j == 0):
            scoreTable[i][j] = i * -1
        print(scoreTable, "\n")

# for i in range(len(x)):


    # #a compared to all
    # if (x[i] == 'a' and y[i] == 'a'):
    #     total = total + matrix[0][0]
    #     print("aa")
    #     print(total)
    # elif (x[i] == 'a' and y[i] == 'c'):
    #     total = total + matrix[0][1]
    #     print("ac")
    #     print(total)
    # elif (x[i] == 'a' and y[i] == 't'):
    #     total = total + matrix[0][2]
    #     print("at")
    #     print(total)
    # elif (x[i] == 'a' and y[i] == 'g'):
    #     total = total + matrix[0][3]
    #     print("ag")
    #     print(total)
    # #c paired to all
    # elif (x[i] == 'c' and y[i] == 'a'):
    #     total = total + matrix[1][0]
    #     print("ca")
    #     print(total)
    # elif (x[i] == 'c' and y[i] == 'c'):
    #     total = total + matrix[1][1]
    #     print("cc")
    #     print(total)
    # elif (x[i] == 'c' and y[i] == 't'):
    #     total = total + matrix[1][2]
    #     print("ct")
    #     print(total)
    # elif (x[i] == 'c' and y[i] == 'g'):
    #     total = total + matrix[1][3]
    #     print("cg")
    #     print(total)
    # #t compared to all
    # elif (x[i] == 't' and y[i] == 'a'):
    #     total = total + matrix[2][0]
    #     print("ta")
    #     print(total)
    # elif (x[i] == 't' and y[i] == 'c'):
    #     total = total + matrix[2][1]
    #     print("tc")
    #     print(total)
    # elif (x[i] == 't' and y[i] == 't'):
    #     total = total + matrix[2][2]
    #     print("tt")
    #     print(total)
    # elif (x[i] == 't' and y[i] == 'g'):
    #     total = total + matrix[2][3]
    #     print("tg")
    #     print(total)
    # #g compared to all
    # elif (x[i] == 'g' and y[i] == 'a'):
    #     total = total + matrix[3][0]
    #     print("ga")
    #     print(total)
    # elif (x[i] == 'g' and y[i] == 'c'):
    #     total = total + matrix[3][1]
    #     print("gc")
    #     print(total)
    # elif (x[i] == 'g' and y[i] == 't'):
    #     total = total + matrix[3][2]
    #     print("gt")
    #     print(total)
    # elif (x[i] == 'g' and y[i] == 'g'):
    #     total = total + matrix[3][3]
    #     print("gg")
    #     print(total)


# total = total - g
# print(total)
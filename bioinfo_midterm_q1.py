#BIOINFO MIDTERM Q1
from Bio.Seq import Seq


'''
Sij = max
max = Si-1, j-1 + M[X[i],Y[j]]
    = Si-1, j+gap
    = Si, j-1+gap

'''

#tacggtat
x = ['t', 'a', 'c', 'g', 'g', 't', 'a', 't']

#ggacgtacg
y = ['g', 'a', 'a', 'c', 'g', 't', 'a', 'c', 'g']

#gap = d

#          a,  c,  t,  g
matrix = [[1, -1, -1, -1], #a
          [-1, 1, -1, -1], #c
          [-1, -1, 1, -1], #t
          [-1, -1, -1, 1]] #g
#print("A[1] =", matrix[1][1])

total = 0

for i in range(len(x)):
    if(len(x)<len(y)):
        g = len(y)- len(x)
    elif(len(y)< len(x)):
        g = len(x)- len(y)
    elif(len(x) == len(y)):
        g = 0

    #a compared to all
    if (x[i] == 'a' and y[i] == 'a'):
        total = total + matrix[0][0]
        print("aa")
        print(total)
    elif (x[i] == 'a' and y[i] == 'c'):
        total = total + matrix[0][1]
        print("ac")
        print(total)
    elif (x[i] == 'a' and y[i] == 't'):
        total = total + matrix[0][2]
        print("at")
        print(total)
    elif (x[i] == 'a' and y[i] == 'g'):
        total = total + matrix[0][3]
        print("ag")
        print(total)
    #c paired to all
    elif (x[i] == 'c' and y[i] == 'a'):
        total = total + matrix[1][0]
        print("ca")
        print(total)
    elif (x[i] == 'c' and y[i] == 'c'):
        total = total + matrix[1][1]
        print("cc")
        print(total)
    elif (x[i] == 'c' and y[i] == 't'):
        total = total + matrix[1][2]
        print("ct")
        print(total)
    elif (x[i] == 'c' and y[i] == 'g'):
        total = total + matrix[1][3]
        print("cg")
        print(total)
    #t compared to all
    elif (x[i] == 't' and y[i] == 'a'):
        total = total + matrix[2][0]
        print("ta")
        print(total)
    elif (x[i] == 't' and y[i] == 'c'):
        total = total + matrix[2][1]
        print("tc")
        print(total)
    elif (x[i] == 't' and y[i] == 't'):
        total = total + matrix[2][2]
        print("tt")
        print(total)
    elif (x[i] == 't' and y[i] == 'g'):
        total = total + matrix[2][3]
        print("tg")
        print(total)
    #g compared to all
    elif (x[i] == 'g' and y[i] == 'a'):
        total = total + matrix[3][0]
        print("ga")
        print(total)
    elif (x[i] == 'g' and y[i] == 'c'):
        total = total + matrix[3][1]
        print("gc")
        print(total)
    elif (x[i] == 'g' and y[i] == 't'):
        total = total + matrix[3][2]
        print("gt")
        print(total)
    elif (x[i] == 'g' and y[i] == 'g'):
        total = total + matrix[3][3]
        print("gg")
        print(total)


total = total - g
print(total)
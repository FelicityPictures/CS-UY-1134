def select(arr,k,lim=5):
    median = MoM(arr,lim)

    s = []
    l = []

    for x in arr:
        if x == median:
            pass
        elif x<median:
            s.append(x)
        else:
            l.append(x)

    # print(s)
    # print(l)

    if k==len(s):
        return median
    else:
        if k<len(s):
            # print("l")
            return select(s,k)
        else:
            # print('s')
            return select(l,k-len(s)-1)


import math
def MoM(arr,lim=5):
    numparts = math.ceil(len(arr) / lim)
    total = []
    for partnum in range(numparts):
        total.append( [arr[ (partnum * lim) + i] for i in range(lim) if (partnum * lim) + i < len(arr)] )

    # print(total)
    for i in range(len(total)):
        total[i] = sorted(total[i])

    medians = []
    for part in total:
        medians.append(part[(len(part)- 1) // 2])
        # print(total[i])
        # print(len(total[i])//2)
        # total[i] = select(total[i],len(total[i])//2,lim)

    # print (medians)
    # print("total sorted: " + str(total))
    # medians = [x[len(x)//2] for x in total]
    return getMedian(medians)

def getMedian(A):
    # print(A)
    if len(A) <= 2:
        return A[0]
    else:
        max = min = (0, A[0])
        for count, el in enumerate(A):

            if el < min[1]:
                min = (count, el)
            elif el > max[1]:
                max = (count, el)
        return getMedian( list(el for count, el in enumerate(A) if count != max[0] and count != min[0]))

import random
A=list(range(222))
random.shuffle(A)
# print(select(A,5))s
print([select(A,i) for i in range(220)])

import timeit
def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+str(n), setup="from __main__ import "+f.__name__,number=repeat)/repeat

def timeFunctionString(f,n,repeat=1):
	return f.__name__ + ": " + str("{:4.6f}".format(timeit.timeit(f.__name__+str(n),
                    setup="from __main__ import "+f.__name__,number=repeat)/repeat)) + "   "
def printFunctionTimes(array,r):
    for x in r:
        print("n= " + str(x) + "   ",end='')
        for m in array:
            if array.index(m)==len(array)-1:
                print(timeFunctionString(m,x))
            else:
                print(timeFunctionString(m,x),end='')
import turtle
def plotFunctionTimesSimple():
    for n in range(1,300):
        turtle.goto(n,timeFunction(select,n,100)*500000)

#plotFunctionTimesSimple()

def plotFunctionTimes(functions,colors,xr,maxy,repeat=1):
    turtle.speed(0)
    turtle.setworldcoordinates(0,0,xr[-1],1)
    br = [5,200]
    for f,c in zip(functions,colors):
        turtles = [turtle.Turtle() for f in functions]
    for x,c in zip(turtles,colors):
        x.pencolor(c)
    for n in xr:
        for f,lk,turt in zip(functions,br,turtles):
            A = list(range(n))
            random.shuffle(A)
            turt.goto(n,timeFunction(f,(A, 0,lk),repeat)/maxy)

# plotFunctionTimes([select,select],["red",'black'],range(1,1000,5),.01,repeat=10)

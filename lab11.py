def select(arr,k,lim=5):
    return selecth(arr,k,lim,0,len(arr))

def selecth(arr,k,lim,start,end):
    if end>len(arr):
        end = len(arr)
    median = MoM(arr,lim,start,end)
    x = start+1
    s = start+1
    l = end-1
    while x<end and s<l:
        if arr[x]<median:
            arr[s],arr[x]=arr[x],arr[s]
            s+=1
        if arr[x]>median:
            arr[l],arr[x]=arr[x],arr[l]
            l-=1
            x-=1
        x+=1
    if arr[s]<median:
        arr[start],arr[s]=arr[s],arr[start]
        medpt = s #medpt is index of array where the median is
    else:
        arr[start],arr[s-1]=arr[s-1],arr[start]
        medpt = s-1
    # print(arr[start:end])
    if k==medpt:
        return median
    else:
        print(median)
        print(arr)
        if k<medpt:
            print("s")
            return selecth(arr,k,lim,start,medpt)
        else:
            print('l')
            return selecth(arr,k-medpt-1,lim,medpt+1,end)

            # print(median)
            # print(s)
            # print(l)
            # print("after: " +str(arr))
            # if x == median:
            #     pass
            # elif x<median:
            #     s.append(x)
            # else:
            #     l.append(x)

            # print(s)
            # print(l)

import math

def s(arr,start,end): #does not include end
    if end>len(arr):
        end = len(arr)
    for m in range(end-start-1):
        if arr[start+m]>arr[start+m+1]:
            arr[start+m],arr[start+m+1]=arr[start+m+1],arr[start+m]
            # print(arr)
        # if m>2:
        for x in range(m):
            # print(x)
            if arr[start+m-x]<arr[start+m-x-1]:
                arr[start+m-x],arr[start+m-x-1]=arr[start+m-x-1],arr[start+m-x]
                # print(arr)
    return arr

def MoM(arr,lim,start,end):
    numparts = math.ceil((end-start) / lim)
    # total = []
    for begin in range(numparts):
        s(arr,start+(begin*lim),start+(begin*lim+lim))
    for x in range(numparts):
        arr[start+x],arr[start+(x*lim+(lim//2))]=arr[start+(x*lim+(lim//2))],arr[start+x]
    return getMedian(arr,start,start+numparts)
        # print(s(arr,begin*lim,begin+lim))
    #     total.append( [arr[ (partnum * lim) + i] for i in range(lim) if (partnum * lim) + i < len(arr)] )

    # print(total)
    # for i in range(len(total)):
    #     total[i] = sorted(total[i])

    # medians = []
    # for part in total:
    #     medians.append(part[(len(part)- 1) // 2])
        # print("just " + str(start+x))
        # print(start+(x*lim+(lim//2)))

        # print(total[i])
        # print(len(total[i])//2)
        # total[i] = select(total[i],len(total[i])//2,lim)

    # print (medians)
    # print("total sorted: " + str(total))
    # medians = [x[len(x)//2] for x in total]

def getMedian(arr,start,end): #Does not look at arr[end]
    # print(A)
    if end-start<= 2:
        # arr[0],arr[start]=arr[start],arr[0]
        return arr[start]
    else:
        for x in range(end):
            if arr[start+x]<arr[start]:
                arr[start],arr[start+x]=arr[start+x],arr[start]
            if arr[start+x]>arr[end]:
                arr[end],arr[start+x]=arr[start+x],arr[end]
    return getMedian(arr,start+1,end-1)
        # max = min = (0, arr[0])
        # for count, el in enumerate(A):
            # if el < min[1]:
            #     min = (count, el)
            # elif el > max[1]:
            #     max = (count, el)



import random
f = list(range(20))
random.shuffle(f)
print("original: " + str(f))
# print(s(felicity,2,20))
# print(f)
print([select(f,i) for i in range(len(f))])
# print(s(f,0,100))

# A=list(range(222))
# random.shuffle(A)
# print(select(A,5))
# print([select(A,i) for i in range(220)])

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

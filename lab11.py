import math,random,timeit,turtle

def select(arr,k,lim=5):
    return selecth(arr,k,lim,0,len(arr))

def selecth(arr,k,lim,start,end):
    if end>len(arr):
        end = len(arr)
    median = MoM(arr,lim,start,end) #(value of median,index)

    if end-start>=2:
        if end-start==2:
            if median[0]>arr[start+1]:
                arr[median[1]],arr[start+1]=arr[start+1],arr[median[1]]
                median = (median[0],start+1)
        else:
            x = median[1]+1
            l = end-1
            while x<l:
                if arr[x]>median[0]:
                    arr[l],arr[x]=arr[x],arr[l]
                    l-=1
                    x-=1
                x+=1
            if arr[l]>median[0]:
                try:
                    arr[l-1],arr[median[1]]=arr[median[1]],arr[l-1]
                    median = (median[0],l-1)
                except IndexError:
                    pass
            else:
                if arr[l]<median[0]:
                    arr[l],arr[median[1]]=arr[median[1]],arr[l]
                    median = (median[0],l)

    if k==median[1]:
        return median[0]
    else:
        if k<median[1]:
            return selecth(arr,k,lim,start,median[1])
        else:
            return selecth(arr,k,lim,median[1]+1,end)

def s(arr,start,end): #does not include end
    if end>len(arr):
        end = len(arr)
    """bubble"""
    # if start+1<end:
    #     for x in range(end-start):
    #         curr = 0
    #         while curr<end-x-1:
    #             # print('curr'+ str(curr))
    #             if arr[curr]>arr[curr+1]:
    #                 arr[curr],arr[curr+1]=arr[curr+1],arr[curr]
    #             curr+=1
    """insertion"""
    for m in range(end-start-1):
        if arr[start+m]>arr[start+m+1]:
            arr[start+m],arr[start+m+1]=arr[start+m+1],arr[start+m]
        for x in range(m):
            if arr[start+m-x]<arr[start+m-x-1]:
                arr[start+m-x],arr[start+m-x-1]=arr[start+m-x-1],arr[start+m-x]
    return arr


def MoM(arr,lim,start,end):
    if end-start<2:
        return (arr[start],start)
    numparts = math.ceil((end-start) / lim)
    for x in range(numparts):
        s(arr,start+(x*lim),start+(x*lim)+lim)
    for x in range(numparts):
        if start+(x*lim)+(lim//2)>=end:
            arr[start+x],arr[start+(x*lim)+((end-(start+(x*lim)))//2)]=arr[start+(x*lim)+((end-(start+(x*lim)))//2)],arr[start+x]
        else:
            arr[start+x],arr[start+(x*lim)+(lim//2)]=arr[start+(x*lim)+(lim//2)],arr[start+x]
    return getMedian(arr,start,start+numparts)

def getMedian(arr,start,end): #Does not look at arr[end]
    if end-start-1<=2:
        return (arr[start],start)
    else:
        for x in range(end-start):
            if arr[start+x]<arr[start]:
                arr[start],arr[start+x]=arr[start+x],arr[start]
            if arr[start+x]>arr[end-1]:
                arr[end-1],arr[start+x]=arr[start+x],arr[end-1]
    return getMedian(arr,start+1,end-1)

###################################################################################################

A=list(range(21))
random.shuffle(A)
# print(A)
# s(A,0,len(A))
# print(A)
# print(select(A,20))
# for x in range(100):
#     print([select(A,i) for i in range(21)])
#     random.shuffle(A)

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

plotFunctionTimes([select,select],["red",'black'],range(1,1000,5),.1,repeat=10)

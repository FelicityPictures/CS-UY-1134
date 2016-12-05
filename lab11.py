def select(arr,k,lim=5):
    print('k' + str(k))
    # print(arr)
    # if len(arr)==1:
    #     return arr[0]
    if lim>len(arr):
        return sorted(arr)[len(arr)//2]
    # print('m: ' + str(median))
    # print("median: " + str(median))
    else:
        total = [arr[:lim]]
        u = lim
        d = 2*lim
        # print(total)
        while d<len(arr):
            # print(arr[u:d])
            total.append(arr[u:d])
            u+=lim
            d+=lim
        total.append(arr[u:])
        for i in range(len(total)):
            # total[i] = select(total[i],len(total[i])//2)
            total[i] = sorted(total[i])[len(total[i])//2]
        # print("total sorted: " + str(total))
        # medians = [x[len(x)//2] for x in total]
    # print("Total:"+str(total))
    s = []
    l = []
    #median = select(total,len(total)//2)
    median = sorted(total)[len(total)//2]
    # print("med: " + str(median))
    for x in arr:
        if x == median:
            pass
        elif x<median:
            s.append(x)
        else:
            l.append(x)
    print('s' + str(s))
    # print("k: " + str(k))
    print('l: ' + str(l))

    ###############################
    if k==len(l)+1:
        return median
    else:
        if k<len(l)+1:
            # print("l")
            return select(l,k)
        else:
            # print('s')
            return select(s,k-len(l)-1)

def MoM(arr,lim=5):
    if len(arr)<lim+1 or lim>=len(arr):
        return sorted(arr)[len(arr)//2]
    else:
        total = [arr[:lim]]
        u = lim
        d = 2*lim
        # print(total)
        while d<len(arr):
            # print(arr[u:d])
            total.append(arr[u:d])
            u+=lim
            d+=lim
        total.append(arr[u:])
        # print(total)
        for i in range(len(total)):
            total[i] = select(total[i],len(total[i])//2)
        # print("total sorted: " + str(total))
        # medians = [x[len(x)//2] for x in total]
        return MoM(total)


# print(select([10,1,0,11,3,9,20,12,7,8,17,6,2,14,19,18,21,16,15,13,5,4],15))
# print(sorted([10,1,0,11,3,9,20,12,7,8,17,6,2,14,19,18,21,16,15,13,5,4]))
import random
A=list(range(10))
random.shuffle(A)
# print(select(A,5))
print([select(A,i) for i in range(1,5)])

# import timeit
# def timeFunction(f,n,repeat=1):
# 	return timeit.timeit(f.__name__+str(n), setup="from __main__ import "+f.__name__,number=repeat)/repeat
#
# def timeFunctionString(f,n,repeat=1):
# 	return f.__name__ + ": " + str("{:4.6f}".format(timeit.timeit(f.__name__+str(n),
#                     setup="from __main__ import "+f.__name__,number=repeat)/repeat)) + "   "
# def printFunctionTimes(array,r):
#     for x in r:
#         print("n= " + str(x) + "   ",end='')
#         for m in array:
#             if array.index(m)==len(array)-1:
#                 print(timeFunctionString(m,x))
#             else:
#                 print(timeFunctionString(m,x),end='')
# import turtle
# def plotFunctionTimesSimple():
#     for n in range(1,300):
#         turtle.goto(n,timeFunction(select,n,100)*500000)
#
# #plotFunctionTimesSimple()
#
# def plotFunctionTimes(functions,colors,xr,maxy,repeat=1):
#     turtle.speed(0)
#     turtle.setworldcoordinates(0,0,xr[-1],1)
#     br = [5,200]
#     for f,c in zip(functions,colors):
#         turtles = [turtle.Turtle() for f in functions]
#     for x,c in zip(turtles,colors):
#         x.pencolor(c)
#     for n in xr:
#         for f,lk,turt in zip(functions,br,turtles):
#             A = list(range(n))
#             random.shuffle(A)
#             turt.goto(n,timeFunction(f,(A, 1,lk),repeat)/maxy)

# plotFunctionTimes([select,select],["red",'black'],range(1,1000,5),.1,repeat=10)

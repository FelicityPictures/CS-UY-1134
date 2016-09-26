"""
Task 1:
fib1(x) - finds the xth fibonnaci number
fib2(x,prev1,prev2) - helper function for fib1
"""
def fib1(x):
    if x==0:
        return x
    else:
        return helper(x,1,0)

def helper(x,prev1,prev2):
    if x==1:
        return prev1
    else:
        return helper(x-1,prev1+prev2,prev1)

#print([fib1(i) for i in range(10)])
#print (fib1(13))

"""
Task 2:
"""
def fib2(n):
    a=[0]
    x=2
    if n==0:
        return a[len(a)-1]
    a.append(1)
    if n==1:
        return a[len(a)-1]
    while x<=n:
        a.append(a[len(a)-1]+a[len(a)-2])
        x+=1
    return a[len(a)-1]
#print (fib2(13))

"""
Task 3:
"""
temp1=0
temp2=1
def fib3(n):
    temp1=0
    temp2=1
    if n==0:
        pass
    else:
        while n>0:
            temp3=temp1
            temp1=temp1+temp2
            temp2=temp3
            n-=1
    return temp1
#print(fib3(15))
"""
print([fib1(i) for i in range(10)])
print([fib2(i) for i in range(10)])
print([fib3(i) for i in range(10)])

for f in(fib1,fib2,fib3):
    print([f(i) for i in range(10)])
"""



"""
Task 4:
"""
import timeit
def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')', setup="from __main__ import "+f.__name__,number=repeat)/repeat

def timeFunctionString(f,n,repeat=1):
	return f.__name__ + ": " + str("{:4.6f}".format(timeit.timeit(f.__name__+'('+str(n)+')',
                    setup="from __main__ import "+f.__name__,number=repeat)/repeat)) + "   "
#print(timeFunction(fib1,2))


def printFunctionTimes(array,r):
    for x in r:
        print("n= " + str(x) + "   ",end='')
        for m in array:
            if array.index(m)==len(array)-1:
                print(timeFunctionString(m,x))
            else:
                print(timeFunctionString(m,x),end='')

#print(printFunctionTimes((fib1,fib2,fib3),range(5,40,5)))

"""
Task 5:
"""
import turtle
def plotFunctionTimesSimple():
    for n in range(1,300):
        turtle.goto(n,timeFunction(fib2,n,100)*500000)

#plotFunctionTimesSimple()

def plotFunctionTimes(functions,colors,xrange,maxy,repeat=1):
    turtle.setworldcoordinates(0,0,xrange[-1],maxy)
    turtle.speed(0)
    turtles = [ turtle.Turtle() for f in functions ]
    for t,c in zip(turtles,colors):
        t.pencolor(c)
    for x in xrange:
        for f,turt in zip(functions,turtles):
            turt.goto(x,timeFunction(f,x,100))

plotFunctionTimes((fib2,fib3),("black","red"),range(1,1000,2),.001,repeat=10)

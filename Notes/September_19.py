#September 19
def f(a):
    #works with even length arrays only
    if len(a)==2:
        if a[0]<a[-1] :
            return a[0]
        else:
            return a[-1]
    else:
        if f(a[len(a)//2:]) < f(a[:len(a)//2]):
            return f(a[len(a)//2:])
        else:
            return f(a[:len(a)//2])

#r=[10,1,3]
#print(f(r))

"""
Makes three recursive calls.
Recursion   |   n   |runtime|number of Recursion
0           |   n   |   n   |       1
1           |  n/2  |  n/2  |       3
2           |  n/4  |  n/4  |       9
l           |n/(2^l)|n/(2^l)|      3^l

log_2 N                         log_2 N
Sigma: (3^l)(n/(2^l))     =     n*Sigma: (3/2)^l   =   O(n(3/2)^log_2 N)
l=0                             l=0
"""

#Improved
def fv2(a,low,high):
    #works with even length arrays only
    if high==None:
        high=a[len(a)]
    if (high-low)<=2:
        if a[0]<a[-1] :
            return a[0]
        else:
            return a[-1]
    else:
        mid=(low+high)/2
        if fv2(a,low,mid) < fv2(a,mid,high):
            return fv2(a,low,mid)
        else:
            return fv2(a,mid,high)

"""
Recursion   |   n   |runtime|Number of Recursion
0           |   n   |   1   |       1
1           |  n/2  |   1   |       3
2           |  n/4  |   1   |       9
l           |n/(2^l)|   1   |      3^l
"""

def fv3(a,low,high):
    #works with even length arrays only
    if high==None:
        high=a[len(a)]
    if (high-low)<=2:
        if a[0]<a[-1] :
            return a[0]
        else:
            return a[-1]
    else:
        mid=(low+high)/2
        x = fv3(a,low,mid)
        y = fv3(a,mid,high)
        if x < y:
            return x
        else:
            return y

"""
    Recursion   |   n   |runtime|Number of Recursion
    0           |   n   |   1   |       1
    1           |  n/2  |   1   |       2
    2           |  n/4  |   1   |       4
    l           |n/(2^l)|   1   |      2^l
fv3() is O(N). Much better than f()
"""

#to compute x^y
#Assume y is a non-negative integer
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
"""
Recursion depth is y.

y
Sigma: 1 = y+1
l=0

O(y)
"""


def powerv2(x,y):
    if y==0:
        return 1
    else:
        b=powerv2(x,y/2)
        a=b*b
        if y%2:
            a*=x
        return a

"""
recusion depth of log_2 Y
O(log Y)

Why is it better to NOT have recursion?
Because you won't need to store all those variables and parameters

Python has maximum recursive depth of 1,000 or 10,000
"""

def Fib(x):
    if x==0:
        return 0
    else:
        if x==1:
            return 1
        else:
            return Fib(x-1)+Fib(x-2)
#Runtime: Big omega: (sqrt(2))^x and big O(2^x)

def LU(a):
#Returns true if everything in the list is unique. False if otherwise
    if len(a)==1:
        return True
    else:
        return a[0]!=a[-1] and LU(a[1:]) and LU(a[:1])
"""
Runtime: 2^N, assuming slicing is free
"""

def LUv2(a):
    for x in a:
        for y in a:
            if x==y:
                return False
    return True

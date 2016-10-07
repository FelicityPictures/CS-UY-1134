testTask1=False
testTask2=False
testTask3=False
testTask4=False
testTask5=False


#----------------Some code to check your answers. Ignore

def checkAnswer(yours,correct):
    print("Your answer:")
    print(yours)
    if yours==correct:
        print("Correct!")
    else:
        print("Wrong. The correct answer is:")
        print(correct)

#----------------TASK 1

"""
 Here you are to code a function firstN that takes an iterator I and
 a nonnegative integer n and you should return a list with the
 first n elements of I. You can assume I has at least n elements to
 iterate over

 For example: firstN(iter(range(10000)),10) should give
"""

def firstN(I,n):
    return [next(I) for m in range(n)]

# Here is a generator that generates all the Fibonacci numbers.
# This will be used in the test code
def fib():
    a,b=0,1
    yield a
    yield b
    while (True):
        a,b=b,a+b
        yield b


if testTask1:
    print("Task 1")

    checkAnswer( firstN(fib(),10) , [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

#----------------TASK 2

"""
In this task you are given a 2D array and you should with a funciton
which will return True if any of the elements are duplicated.

For example:
duplicated2D([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
should return false

and

duplicated2D([[0, 1, 2], [3, 4, 5], [6, 7, 0]])
should return true as 0 is duplicated
"""

def duplicated2D(A):
    temp=[]
    while len(A)>0:
        temp=A[0]
        A.pop(0)
        for x in temp:
            for m in range(len(A)):
                for c in range(len(A[0])):
                    if x==A[m][c]:
                        return True
    return False


if testTask2:
    print("\nTask 2")

    A1=[ [i+3*j  for i in range(3)] for j in range(3)]
    A2=[ [ (i+3*j)%8  for i in range(3)] for j in range(3)]
    print("Duplicate in ",A1," ?")
    checkAnswer( duplicated2D(A1), False)
    print("\nDuplicate in ",A2," ?")
    checkAnswer( duplicated2D(A2), True)

#----------------TASK 3

"""
 Here you are to write a function that computes the number of digits in a
 nonnegative integer

 It must be recursive and have no loops

 For example howManyDigits(12345) should return 5
"""

def howManyDigits(x):
    if x//10==0:
        return 1
    else:
        return 1 + howManyDigits((x//10))

if testTask3:
    print("\nTask 3")
    for i,answer in ((5,1),(10,2),(90,2),(123456,6)):
        print()
        print(i," has this many digits:")
        checkAnswer(howManyDigits(i),answer)


#----------------TASK 4

"""
In this task you are to write a function to reverse a deque (collections.deque)
Your funciton must be recursive. It must have no loops, no for or while
"""


import collections

def reverseDeque(D):
    print(D)
    if len(D)<=1:
        return D
    else:
        arr = D.pop()
        reverseDeque(D)
        return D.appendleft(arr)

if testTask4:
    print("\nTask 4")
    D=collections.deque( range(10))
    print("Reversing: ",D)
    reverseDeque(D)
    checkAnswer(D,collections.deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

#----------------TASK 5
"""
Your task here is to code a function that creates a multidimensional array and initializes it.

Your function should look like this:
def makeDDimensionalArray(d,n,f)
(hint: you may need to add other parameters, but give them default values)

n: This is the size in each dimension.
d: This is the number of dimensions
f: This is the function called to initialize the array. It should work as
follows: suppose you have a 3-D array, call it A and you need to initilize
A[i][j][k]. You shoud set it to f( (i,j,k) ).

For example, to create a 2D 5x5 array where A[i][j]=i+j you would call:
checkAnswer(makeDDimensionalArray(2,5,sum)
and this should return:
[[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]

As another example, to create a 4D 2x2x2x2 array, all of ones, you would call:

checkAnswer(makeDDimensionalArray(4,2,always1)
and ti would return
[[[[1, 1], [1, 1]], [[1, 1], [1, 1]]], [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]]
where always1 is the function defined below that always returns 1

Hint 1: Recursion
Hint 2: My answer is one line long. Yours should not be very long.

"""

def makeDDimensionalArray(d,n,f,c=[]):
    #you can also make c a parameter for the function
    return [f(c + [i]) for i in range(n)] if d==1 else [makeDDimensionalArray(d-1,n,f,c+[i]) for i in range(n)]


# for i in range(x):
#     grid.append([Cell((s*i+(s/2),s*m+(s/2)),randomColor(),False) for m in range(y)])

def always1(x):
    return 1

def hi(a):
    return a

def sum(x):
    return x

print(makeDDimensionalArray(2,3,hi))
if testTask5:
    print("\nTask 5")
    checkAnswer(makeDDimensionalArray(2,5,sum),
        [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]])

    checkAnswer(makeDDimensionalArray(4,2,always1),
        [[[[1, 1], [1, 1]], [[1, 1], [1, 1]]], [[[1, 1], [1, 1]], [[1, 1], [1, 1]]]])

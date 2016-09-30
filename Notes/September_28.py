#September 28th, 2016

#You can change arrays but not strings and tuples
S = "hello"
S = S + " there"
print(S)
#Doesn't change S. Just makes it point to something else
S = "The complete works..."
T=[]
for c in S:
    if c.isalpha():
        T.append(c)
A = "".join(T)
print(A)

A = "".join([c for c in S if c.isalpha()])
#you can get rid of the [] to make it more efficient
#.join() takes anything that's iterable
print(A)

def f():
    for i in range(5):
        yield i
def S(A):
    r=0
    for i in A:
        r+=1
        return r
S(f())
S([i for i in f()])

#Strings are immutable!!
"""
A[5] is O(1), constant run time
A.append(5) is O(1), constant
A.pop() is also O(1), constant
A[i:j] is linear time, O(j-i)
A+B is O(len(A)+len(B))
5 in A returns boolean if 5 is in A, so O(n) because it has to loop through it
A.count(5) is also O(n)
A.index(5) is also O(n)
A==B is O(n)
del A[1] takes second element from list andd removes it. O(n-i)
del A would undeclare A as a variable

STACKS
push: inserts item to be first in stack
pop: removes first item in stack
top: returns first item in stack
"""

class Stack:
    def __init__(self):
        self._A = []
    def push(self,x):
        self._A.append(x)
    def pop(self):
        self._A.pop()
    def top(self):
        return self._A[-1]
    def __len__(self):
        return len(self._A)
ex = "([{}()([])])"
#You can use stack to determine if they're closed. Put open in a stack and check to see the top matches it each time a closed comes up
def pmatch(s):
    OPEN = "({["
    CLOSE = ")}]"
    x = Stack()
    for c in s:
        if c in OPEN:
            x.push(c)
        else:
            if c==CLOSE[OPEN.index(x.top())]:
                #can replace CLOSE[OPEN.index(x.top())] with dictionary Close
                x.pop()
            else:
                return False
    return True

Close = {'(':')', '{':'}', '[':']'}

"""
QUEUE

enqueue
dequeue
front
back
"""
class Queue:
    def __init__(self):
        self._A = []
    def enqueue(self,x):
        self._A.push(x)
    def dequeue(self):
        del self._A[0]
    def front(self):
        return A[0]
    def back(self):
        return A[-1]

#python has a built in deque: appendleft(), append(), popleft(), pop()

class doubleEndedQueue:
    def __init__(self):
        self._A = [None]
        self._back=0
        self._front=0

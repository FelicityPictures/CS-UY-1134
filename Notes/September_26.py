#September 26th, 2016
A=[0]*3
#is [0,0,0]

A=[[0]*3]*3
#is [[0,0,0],[0,0,0],[0,0,0]]
#bad because if you do A[1][1] = 2, it means A[0][1] is also 2. This method creates a one dimensional array that points to another one
#dimensional array.

#the better way
A=[0 for i in range(3)]
A=[[0 for i in range(2)]for i in range(3)]

#on a 64-bit machine, when you write 0, it uses 64 bytes
A=[0 for i in range(100)]
import sys
sys.getsizeof(A)#gets size of A, but all the indexes of A are pointers so it gets the size of A and the size of the pointers
print(sys.getsizeof(A)+sum([sys.getsizeof(a) for a in A]))
#when you run, you get 3708

import array
B=array.array('b',A)
#the little b means it will represent the assigned integers in A as one byte
#B[3]='cat' would get an error because you can only store very small numbers
#B would not have arrows/pointers. Instead, the array has the things inside the array
print(sys.getsizeof(B))

for i in A:
    i+=1
#it doesn't change anything in A. If you want to change A, you have to use the index:
for i in range(len(A)):
    A[i]=A[i]+1

A=(n*ctypes.py.Object)()
#array of size n that can be Python objects

class myList:
    def __init__(self):
        self._A = None
        self._L = 1
        self._act = 0
    def append(self,x):
        if self._L == self._act:
            T = self._getArray(self_L*2)
            for i in range(self._L):
                T[i]=A[i]
            T[self._L]=x
            self._L=self._L*2
            self._A=T
        else:
            A[self._act+1]=x
        self._act+=1
        """
size:   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
cost:   2   4   -   8   -   -   -   16  -   -   -   -   -   -   -   32  -   -   -
total cost:
        2   6   6   14  14  14  14  30  30  30  30  30  30  30  30  62  62  62
total # operations:
        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
total cost divided by total # operations is always less than 4
        """
#any class can support indexing if you use:
    def __getitem__(self,i):
        return self._A[i]
#len(myList):
    def __len__(self,i):
        return self._L
    def _getArray(self,n):
        return n*ctypes.py.Object()

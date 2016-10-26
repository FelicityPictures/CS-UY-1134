#October 26, 2016
"""
Priority Queue:
key is the number/priority
v is the data

add(key,v)
In normal array, would be O(1)
In sorted array, would be O(n)
In a heap, O(log n)

remove_min(): Returns key and v
In normal array, would be O(n)
In sorted array, would be O(1)
In a heap, O(log n)

min(): returns key and v
In normal array, would be O(n)
In sorted array, would be O(1)

__len__()
is_empty()
------------------------------------------
A heap is a tree where every node is <= to its children.
All the levels are full until the last level.
A tree that is full and has h levels has (2^h)-1 nodes.

Ex: Inserting 9 into a tree of:
                    7
            10            20
        35      11      21  100
    150   37  12
How to insert:
1) Put into tree
2) if smaller, switch with greater parent and keep switching until it's parent is smaller
Bubble up

Remove minimum:
It's the root. Take the furthest down element and check it against the smaller children.
Keep doing it until it reaches the point where it's smaller than it's children.
Bubble down

To put into a list, just read each level because it's a balanced/full tree
As parent, position in array is i. Left node is position 2i+1. Right node is position 2i+2.
As a node, position in array is i. Parent node is position (i-1)/2.
"""

class PriorityQueue:
    def __init__(self,A=None):
        self._A = []
        #if A is not enpty, run heapify
    def _heapify(self):
        for i in range(len(self._A)-1,-1,-1):
            self._bd(i)                                                 :
    def add(self,k,v):
        self._A.append((k,v))
        self._bu(len(self._A)-1)
    def remove_min(self):
        min = self._A[0]
        self._A[0] = self._A.pop()
        self._bd(0)
        return min
    #helper functions
    def _left(self,p):
        return 2p+1
    def _right(self,p):
        return 2p+2
    def _parent(self,p):
        return (p-1)/2
    def _has_left(self,p):
        return self.left(p)<len(self._A)
    def _has_right(self,p):
        return self.right(p)<len(self._A)
    def _root(self,p):
        return p==0
    def _bu(self,p):
        if not self._root(p) and self._A[p]<self._A[self._parent(p)]:
            self._A[p],self._A[self._parent(p)]=self._A[self._parent(p)],self._A[p]
        self._bu(self._parent(p))
    def _bd(self,p):
        lc = self._left(p)
        rc = self._right(p)
        sm = p
        if self._has_left(lc) and self._A[lc]<self._A[sm]:
            sm = lc
        if self._has_right(rc) and self._A[rc]<self._A[sm]:
            sm = rc
        if sm!=p:
            self._A[p],self._A[sm] = self._A[sm],self._A[p]
            self._bd(sm)
def sort(A):
    PQ = PriorityQueue()
    while not A.is_empty():
        PQ.add(A.pop(),None)
    while not PQ.is_empty():
        A.append(PQ.remove_min()[0])
"""
Heapify:
You can put into a tree and loop through to bubble up/down.
To bubble up the things on the bottom, it takes(n/2)logn
To bubble down the things on the bottom, it takes on average 1 swap



"""

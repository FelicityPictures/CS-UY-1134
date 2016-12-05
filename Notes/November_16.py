#November 16, 2016
#Sample exam #2 review

#Question 1
def odd_iter(self):
    p = self._header._next
    while p and p != self._trailer:
        yield p._element
        p=p._next._next

    """
    OR
    while p:
        yield p.element()
        p=self.after(p)
        if p:
            p=self.after(p)
    """

#Question 2
def swapforward(self,p):
    b=p._node
    a=b._prev
    c=b._next
    d=c._next
    b._next,b._prev,c._next,c._prev = c._next,c._prev,b._next,b._prev
    a._next,d._prev = d._prev,a._next

#Question 3
def _add_left(self,p,e):
    #code
    node._prev._next = node._left
    node._left._prev = node._prev
    node._prev = node._left
    node._left._next = node


#Question 4
def stringTree(s):
    t = LinkedBinaryTree()
    if s!=' ':
        t._add_root(s)
        t._attach(T.root(),stringTree(s[:len(s)//2]),stringTree(s[len(s)//2:]))
    return t

#Question 5
def kthMin(self,k):
    A = []
    for i in range(k);
        A.append(self.remove_min())
    r=A[-1]
    for i in A:
        self.add(*i)
    return r

#Question 6
"""
Do it with heappriorityqueue cuz you can just remove min expiration date = soonest expiring lightbulb
"""
h = Heap()
day = 0
c={}
for i in range(100):
    h.add(randint(100,110),1)
while t in range(1000):
    (t,id)=h.extract_min()
    print('---')
    h.add(randint(100,110),id)
    if t in c:
        c[t]+=1
    else:
        c[t]=1
"""
maxcount=0
for id,count in c.items():
    if count>maxcount:
        maxcount=count
        maxid=id
return id
"""

def differentString(S):
    H = {}
    for s in S:
        H[s]='frog'
    return len(H)

#Queestion 7
order = [4,2,6,1,3,5,7]

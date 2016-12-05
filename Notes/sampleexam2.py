#Question 1
def odd_iter(self):
    curr = self.first()
    while curr is not None:
        yield curr
        if self.after(curr) is None:
            return
        else:
            curr = self.after(self.after(curr))

#Question 2
def swap_forward(self,p):
    s = self.after(p)._node
    p = self._validate(p)
    p._next = s._next
    s._prev = p._prev
    p._prev = s
    s._next = p
    p._next._prev = p
    s._prev._next = s


#Question 3
def _add_left(self,p,e):
    node = self._validate(p)
    if node._left is not None:
        raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e,node,next=node,prev=node._next)
    if node._next:
        node._left._next = node._next
    node._next = node._left
    return self._make_position(node._left)

#Question 4
def stringTree(s):
    t = LinkedBinaryTree()
    t._add_root(s)
    if len(s)==1 or len(s)==0:
        return t
    else:
        l = s[:len(s)//2]
        r = s[len(s)//2:]
        t._attach(t.root(),stringTree(l),stringTree(r))

#Question 5
def kthMin(self,i):
    hold = [self.remove_min() for x in range(i)]
    for m in hold:
        self.add(*m)
    return hold[-1]

#Question 6
class Simulation:
    class Bulb:
        def __init__(self,replace=0):
            self._life = randint(100,110)
            self._replaced = replace
        def die(self):
            if self._life == 0:
                self._replaced += 1
                self._life = randint(100,110)
                return True
            self._life -= 1
            return False
    def __init__(self):
        self._bulbs = [Bulb() for i in range(100)]
    def run(self,days):
        max = (0,0) #first is day. Second is lightbulbs changed
        for i in range(days):
            x = 0
            for f in range(len(self._bulbs)):
                if self._bulbs[f].die():
                    x+=1
                    print("day " + str(i) + ": lightbulb " + str(f) + " got changed.")
            if x>max[1]:
                max = (i,x)
            print("Day " + str(i) + " and " + str(x) + "light bulbs were changed.")
        return max[1]

def uniquestr(arr):
    r = 0
    curr = arr.pop()
    while len(arr)>0:
        m=0
        for x in arr:
            if curr == x:
                m+=1
        if m==0:
            r+=1
    return r #r is number of unique strings
#runtime is O(n^2)

#Question 7: 4,2,6,1,3,5,7











        #

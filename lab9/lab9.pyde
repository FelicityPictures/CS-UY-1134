import random

class PQ:
    class Node:
        def __init__(self,data,flip):
            self._l = None
            self._r = None
            self._data = data
            self._flip = flip
        def children(self):
            if self._l==None and self._r==None:
                return False
            return True
        def left(self):
            if self._flip:
                return self._r
            return self._l
        def right(self):
            if self._flip:
                return self._l
            return self._r
        def data(self):
            return self._data
        def changeLeft(self,node):
            if self._flip:
                self._r=node
            self._l = node
        def changeRight(self,node):
            if self._flip:
                self._l=node
            self._r = node
            
    def __init__(self):
        self._flip = False
        self._root = None
    def flip(self,n):
        if n._l != None:
            self.flip(n._l)
        n._l,n._r=n._r,n._l
    def merge(self,n1,n2):
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        if(n1._data<n2._data):
            n1._l=self.merge(n1._l,n2)
            return n1
        else:
            n2._l=self.merge(n2._l,n1)
            return n2
    def insert(self,v):
        #print(v)
        #t = PQ()
        t=self.Node(v,False)
        self._root=self.merge(self._root,t)
        self.flip(self._root)
        #print('current:')
        #self.print_data(self._root)
        
    def print_data(self,curr):
        # curr = start
        if curr != None:
            print(str(curr.data()) + " children are:" + str((curr._l,curr._r)))
            if curr._l != None:
                self.print_data(curr._l)
            if curr._r != None:
                self.print_data(curr._r)
    def extractMin(self):
        x = self._root
        if x is None:
            return None
        else: 
            if x._l != None and x._r != None:
                if x._l.data()<x._r.data():
                    self._root = x._l
                    self.merge(self._root,x._r)
                else:
                    self._root = x._r
                    self.merge(self._root,x._l)
            else:
                if x._l is None:
                    self._root = x._r
                else:
                    self._root = x._l
            return x.data()

def subtree_size(node):
    if node is None:
        return 0
    else:
        return 1+subtree_size(node._l)+subtree_size(node._r)
def draw_tree(node,level=1,x=20,parx=None,pary=None):
    XSEP=15
    YSEP=30
    fill(0)
    textAlign(CENTER,CENTER)
    textSize(15)
    lsize=subtree_size(node._l)
    myx,myy=x+lsize*XSEP,YSEP*level
    text(str(node._data),myx,myy)
    if node._l is not None:
        draw_tree(node._l,level+1,x,myx,myy)
    if node._r is not None:
        draw_tree(node._r,level+1,x+(lsize+1)*XSEP,myx,myy)
    if parx is not None:
        strokeWeight(10)
        stroke(0,255,0,30)
        line(parx,pary,myx,myy)
def setup():
    size(1000,1000)
def draw():
    A=list(range(20))
    #random.shuffle(A)
    pq=PQ()
    for i in A:
        pq.insert(i)
    # pq.extract_min()
    draw_tree(pq._root,8)
    print([pq.extractMin() for i in range(20)])
    
#returns [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    
    
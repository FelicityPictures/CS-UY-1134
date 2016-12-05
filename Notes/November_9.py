#November 9, 2016

"""
Binary search tree:
Everything in the left subtree is smaller and everything in the right subtree is bigger

Search:
find smallest thing - keep going left
find biggest thing - keep going right
To find the smallest one that is also greater - go to right child. If not, then go up until you find one bigger
When you add something, pretend that you're searching for something and then insert it

positions has: .key(), .value(), .item()

def _subtree_search(self,p,k):
    #returns position of where the thing is OR returns the node where you will fall off
    if p.key() == k:
        return p
    elif k<p.key():
        if self.left(p):
            return self._subtree_search(selfleft(p),k)
        else:
            return p
    else:
        #same for right as left

def after(self,p):
    #given a position, return the next position in the tree
    if self.right(p):
        return self._subtree_first_position(self.right())
    else:
        r=self.parent(p)
        while r.key()<p.key():
            r=self.parent()
        return r

def find_position(self,k):
    return self._subtree_search(self.root(),k)
def __contains__(self,k):
    return self.find_position(k).key()==k
def _subtree_first_position(self,p):
    if self.left(p):
        return _subtree_first_position(self.left(p))
    else:
        return p
def find_min(self):
    return self._subtree_first_position(self.root()).item()

def __init__(self):
    p=self._subtree_first_position(self.root())
    while p:
        yield p.key()
        p=self.after(p)
def __setitem__(self,k,v):
    p=find_position(k)
    if p.key()==k:
        p.data().value=v
    else:
        if k>p.key():
            self._insert_right(p,k,v)
        else:
            self._insert_left(p,k,v)
def __getitem__(self,k):
    p=self.find_position(k)
    if p.key()==k:
        return (p.key(),p.value())
    else:
        ###
def find_range(self,start,stop):
    #start and stop are positions
    while start != stop:
        yield start.item()
        start=self.after(start)

def delete(self,p):
    if self.num_children<2:
        super().delete(p)
    else:
        r=self.before(p)
        p.replace(r.key(),r.value())
        self.delete(r)











"""

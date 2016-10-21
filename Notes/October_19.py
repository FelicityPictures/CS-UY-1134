#October 19, 2016
"""
Tree things:
root()
parents(e)
children(e) - returns iterator of children for leaf e
    for c in T.children(T.root()):
        print c.data()
    to write list for children:
        List(T.children(T.root()))
is_root(e) - returns true if its root
is_leaf(e) - returns true if it has no children
num_children(e) - returns number of children the node has
__len__
is_empty
__iter__
positions()
"""
class Tree:
    def __init__(self):
        self._root = None
        self._size = 0
    def __iter__(self):
        for p in self.positions():
            yield p.data
    def positions(self):
        yield from self._positions(self.root())
        #python 2: for i in F: yield i
    def _position(self,p):
        yield p
        for c in self.children(p):
            yield from self._position(c)

"""
_Node
    _data
    _parent (Node)
    _children (list of Nodes)
"""
    def parent(self,p):
        self._mp(p._node._parent)
    def children(self,p):
        for cn in p._node._children:
            yield self._mp(cn)
    def depth(self,e):
        if self.is_root(e):
            return 1
        else:
            return 1+self.depth(self,parent(p))
    def height(self):
        return max(self.depth(p) for p in self.positions())
    def height(self,p=None):
        if not p:
            p=self.root()
        if self.is_leaf(p):
            return 1
        else:
            return 1+max(self.height(c) for c in self.children(p))
            #Change max to sum and height to length in order to count number of leaves

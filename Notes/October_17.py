#October 17, 2016

class PList:
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail)
    def after(self,p):
        return self._make_position(p._next)
    def __iter__(self):
        p = self.first
        while p:
            yield p.data()
            p = self.after(p)
    def _ins_after(self,node,data):
        pass
        
    class Position:
        def __init__(self,node,plist):
            pass
        def data(self):
            pass
        def __iter__(self):
            pass
        def __eq__(self,other):
            #Checks for equality, so you can do something like L==R
            return self.node is other.node
        def __ne__(self,other):
            #For not equal
            return not self==other

    def add_first(self,data):
        pass
    def add_last(self,data):
        pass
    def add_before(self,p,data):
        pass
    def add_after(self,p,data):
        pass
    def delete(self,p):
        pass
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return Position(node,self)

#November 2, 2016

a = ["Is","this","a","this","a","hello","a"]
def mostFrequent(A):
    m ={}
    for w in A:
        """
        if w in m:
            m[w]=m[w]+1
        else:
            m[w]=1
        """
        m[w] = m.get(w,0)+1
    #return max(m.values())
    #return max(m.items(),key=f)[0]
    #key sets it to function f and puts the results into f
    return max(m.items(),key=lambda x: x[1])[0]
    """
    instead of lambda x: x[1], write operator.itemgetter(1)
    O(n)
    use hash table because you don't care about the order of the stuff.
    """
    def f(x):
        return x[1]

    """
    If you hash(x) and hash(y) and they're equal, they'll return the same number
    How would you hash(x,y)? You hash(x) then hash(y) and if they're equal, they return 0
    """
    def hash(t): #t is a tuple
        value = 345678
        for item in t:
            value = 10000003*value^item
            100000*(10000003*345678^x)^y

class HT:
    def __init__(self):
        self._A = [[] for i in range (10)]
        self._size = 0
    def _bucket(self,key):
        return self._A[hash(key) % len(self._A)]
    def __getitem__(self,k):
        for key,val in self._bucket(k):
            if key==k:
                return val
        raise KeyError("error message")
    def __setitem__(self,k,v):
        b=self._bucket(k)
        for i in range(len(b)):
            if k == b[i][0]:
                b[i] = (b[i][0],v)
                return
        b.append((k,v))
        self._size += 1
        if self._size > 2*len(self._A):
            self._resize(2*len*self._A)
    def _resize(self,ns):
        z = self.items()
        self._A = [[] for i in ns]
        self._size = 0
        for k,v in z:
            self[k] = v
    def __delitem__(self,k):
        b=self._bucket(k)
        for i in range(len(b)):
            if k == b[i][0]:
                b.pop(i)
                #self._size -= 1
                return
        raise KeyError("error message")
    def __contains__(self,k):
        b=self._bucket(k)
        for i in range(len(b)):
            if k == b[i][0]:
                return True
        return False
    def __iter__(self):
        for b in self._A:
            for k,v in b:
                yield k



#

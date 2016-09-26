#September 12, 2016
c = Counter()
print(c)
#prints 0
c.inc()
print(c)
#prints 1

class Counter:
	numcounters=n
	#it’s a class variable. ALL classes share the same variable
	def __init__(self, c=None, increment=1):
#if you leave “self” out, you’re creating a static method
        if (c==None):
            self._c=0
        else:
            self._c=c._c
        Counter.numcounters+=1
        self._increment = increment
	def getnc():
		return counter.numcounters
#Capitalize class names. Lower-case and camelcase for methods. Private variables have underscore
    def inc(self):
    	self._c+=1
    def __str__(self):
    	return str(self._c)
    def __add__(self,x): c=c+15
    	self._c+=x
		return seld._c
    def __radd__(self,x): c=15+c
    	self._c+=x
    def inc(self, increment=0):
    	if(increment==0):
    		increment == self._increment
    	self._counter += increment

d=c
d.inc()
print(c,d)
#returns (2,2)

A=[Counter() for i in range(4)]
#Creates 4 separate counters
c=Counter()
for i in range(4):
	A.append(c)
A[0].inc()
A[4].inc()
print(A)
#Yields [1,0,0,0,1,1,1,1] because A[4-7] is pointing to the same counter, c, but A[0-3] are pointing to separate counters


A=[]
A.append(Counter())
for i in range(4):
	A.append(copy.copy(A[0]))
#A=[0,0,0,0,0]
A+=copy.copy(A)
A[1].inc()
print(A)
#A=[0,1,0,0,0,0,1,0,0,0] because the second half of the array points to the first half
#copy.copy(x) is recursive. Uses arrows to point to copied object instead of just repeating it

A=[Counter() for i in range(10)]
print(counter.getnc())
#returns 10

class FancyCounter(Counter):
	def __init__(self,step):
		super().__init__()
		self._step=step
	def inc(self):
		self._c+=self._step
	class _huh:
	#class inside a class


#raise StopIteration
#stops attempts to run
try:
#[--code--]
catch:
#	[--runs this code if the code in try doesn’t work--]

for i in range(10):
	B=[1,2,3,4]
A=[i+1 for i in iter(B)]
#Iterator can be put in B’s position^
#Iterable:
I=iter([1,2])
	print(next(I)) #1
	print(next(I)) #2
	print(next(I)) #will crash. StopIteration

for i in CoI(FancyCounter(4),20)
print i
# yields 0,4,8,12,16

class CoI:
	def __init__(self, c, l):
		self._c=c
		self._l=l
	def __iter__(self):
		return self
	def __next__(self):
		self._c.inc()
		if self_c.value<self._l:
			return self._c.value
		else:
			raise StopIteration
I=iter(x)
while(True):
	print(next(I))
except StopIteration
	print(‘failed’)

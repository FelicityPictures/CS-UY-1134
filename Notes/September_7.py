#September 7th, 2016
A = [0,1,2,3,4]
print(A[-1])
#yields 4
print(A[1:10:2])
#gives every other element starting with the first element and ending with the last

def huh():
	yield “hi”
	yield “hello”
	for i in range(3):
		yield i
for x in huh:
	print x
#You would use huh() instead of using an array storing “hi”, “hello”, and 0, 1, 2 because it is better for memory

def f(x):
	return (x*x, x*x*x)
print (f(2)[0]) returns 2*2

T=(3,4,5)
sum = f(T[0],T[1],T[2]) same as f(*T)

"""
Equation for fibonacci:
(1/sqrt5)(((1+sqrt5)/2)n-((1-sqrt5)/2)n )

If you have n things in a balanced tree, its height is log(n)
"""

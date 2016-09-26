#September 14, 2016
"""
Given N is big enough, a runtime of constant x log(N) is better than a linear runtime of constant x N

Asymptotic notation
3n^2 + 7n + 1 = theta(n^2)
Theta means: it's true if you get rid of 7n, 1, and all leading constants
It's useful because if you write code for linear search, the runtime would be not be EXACTLY the formula.
The setup time can vary from machine to machine but runtime is the same for all machines.
O means theta
linear search: O(N)
binary search: O(log N)

Runtime: Worse case scenario

What does it mean for a function to be O(N)?
If you can draw two lines from the origin such that if you go far enough out, the function always stays between the two lines

Anything can be theta of itself but common convention is to simplify it

There are five symbols: little omega, omega, theta, big O, and little o

            |       >      |   >=  |   =   |   <=  |    <
            | little omega | omega | theta | big O | little o
n=_(n^2)    |      N       |   N   |   N   |   Y   |    Y
n^2=_(n^2)  |      N       |   Y   |   Y   |   Y   |    N
n^3=_(n^2)  |      Y       |   Y   |   N   |   N   |    N

For big O, write the smallest function that makes sense. For omega, write the biggest function.
Omega(N) means there isn't a function that can go faster, but there is a function that can be slower

The fastest function is constant=theta(1)

Runtimes ordered:
^  slow
|       theta(2^N)
|       theta(N^3)
|       theta(N^2)
|       theta(NlogN)
|       theta(N)
|       theta(root N)
|       theta(logN)
|       theta(1)
v  fast

"""
#runtime: O(N^3)
def duplicateInThree(a,b,c):
    for a in a:
        for b in b:
            if a==b:
                for c in c:
                    if a==b==c:
                        return True
    return False

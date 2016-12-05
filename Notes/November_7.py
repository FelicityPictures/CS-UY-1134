#November 7, 2016

"""
x = random variable
x=1,2,3,4,5,or 6
1/6 possibility
E[x+y] = E[x]+E[y]
E[x]=1*1/6 + 2*1/6 + 3*1/6 + 4*1/6 + 5*1/6 + 6*1/6 = 3.5

find_min()
find_max()
find_lt(k) - less than
find_gt(k) - greater than
find_le(k) - less equal
find_ge(k) - great equal
find_range(a,b) - finds everything equal to and greater than a but less than b
__iter__ - returns everything in sorted order

Skip list:
Possibility that an item is at level i or higher: 1/2^i
Possibility given n items at least is at level i or higher: <= n/2^i
Possibility that some item is at level 3log_2(n) or higher: <= n/2^(3log_2(n))= n/2^(n^3)
Total space usage: 2n because of all the shrinking from halving

You won't walk right that much cuz of how the list is split
Maybe at most, 2 steps right

Set:
good if you don't need the data

ex:
set s
s.add("John")
s.discard("John")
"John" in s

set s - set of all students
set a  - set of all students with a A in the class

== != - if the sets are equal or not
<= < - ex: a<=s returns true - for asking if a is a subset of s
>= > - ex: s>=a returns true - for asking if s is a superset of a

isjoint - asks if they have anything in common
A | B - A union B
A & B - A intersection B
A^B - who is in exactly one of the sets

"""

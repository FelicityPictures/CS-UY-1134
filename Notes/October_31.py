#October 31, 2016

"""
remove(self,p)
p = insert(self,k,v)
update()
Good programming practice is a class to deal with things in a heap that
keeps track of key, value, and position.


-----------------------
Insert, delete, search
Array   O(1), O(1), O(n)
Linked List     O(1), O(1), ?
Sorted Array    O(n), O(n), O(log n)
Balanced Binary tree    O(log n), O(log n), O(log n)
Hash table  O(1), O(1), O(1)
Hash tables keep things with no respect to order. Can't tell you what is before and after something

dict, map, associative array:
D = {}
D = {"John":"A","Joe":"F"}
print(D["John"]) would print out "A"
D["John"]="F"
print(D["John"]) would print out "F"
D["Jill"]="B"
del D["John"] would remove "John" from the associative array
iter(D) would iterate over the keys. It would come out in any order.
D.keys() - returns all the keys (John, Joe, and Jill)
D.values() - returns all the values (A,B,F)
D.items() - returns the pairs (Jill and B, Joe and F, etc.)
D.get("John") would return None if John is not there or if John maps to None
D.get("John", 57) would return 57 if John is not there, but not 57 if John maps to None
D.pop() would remove an unknown thing from the dict and return it or None if its empty

Keys must be immutable
ex: node class:
D[n] = 53
N.data = 22

Immutable in python: tuple, int, float, boolean, frozenset
Not immutable in python: List, self defined classes, dict, set

hash function
data-->integer
if a==b:
    then hash(a)==hash(b)
"""
class Color:
    def ___hash___(self):
        return hash((r,g,b))
"""
"John"
hash("John") = 1 2 3 7 2 4
hash("John")%10 = 4
A["John"] = "A"
Puts "John":"A" into the bucket 4
a list that keeps track of the buckets
Hash table is a list of lists of tuple pairs.
N pieces of data
B buckets
N/B is the load factor: the amount of data per buckets
choose B to be about N to 2N
"""

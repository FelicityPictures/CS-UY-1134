#December 5th, 2016

"""
Data structure: TRIE
for storing sets of strings

(aaa,aba,afab,abba,cat,cave,collesus)
Stored on a tree without limits as to how many branches



"""
class Node:
    def __init__(self):
        self._children = {}
        self._end = False #OR you can have a node to a character that you know won't be used. ex: $ in self._children

T = "This is a piece of text" #(size n)
S = "piece" #(size m)
def substring(T,S):
    for i in range(len(T)-len(S)+1):
        if S==T(::I+len(S)):
            return True
    return False
#O(n*m)

"""
Dynamic programming:
        probability
a           .01
b           .5
c           .1
d           .2
e           .01
f           .18

"""

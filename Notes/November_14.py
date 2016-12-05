#November 14, 2016

"""
AVL Trees:
    If you look at any two children, their height will differ by at most 1

s(h) = smallest # of nodes in an AVL tree of height h
s(1) = 1
s(2) = 2
s(3) = 4
s(4) = 7
s(h) = s(h-1) + s(h-2) + 1
Very similar to the fib numbers (fib - 1)
fib(1) = 2
fib(2) = 3
fib(3) = 5
fib(4) = 8

AVL Tree-
insertion: when you add, go up and change the upper nodes' height variable
rotation: Look at last three things and make a small binary tree with it
delete: When there is a violation, pick the path from the other side and rotate


Red-Black Trees:
    Every node is red or black. Root is black. No two reds in a row
    No two reds as parent-child
    Same # of blacks on every root-to-leaf parent-child
insertion: when you insert something, make it red initially and then check.
        If it violates, rotate.

height of AVL trees: 1.44logN
height of RB rtees: 2logN


"""

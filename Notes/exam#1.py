import math
def dist(x,y):
    return math.sqrt( (x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]) )
def closestPair(arr):
    P=[arr[0],arr[1]]
    dis = dist(*P)
    while len(arr)>1:
        curr=arr.pop()
        for i in arr:
            if dist(curr,i)<dis:
                P=[curr,i]
                dis=dist(*P)
    return P

A = [(0,0),(10,10),(20,20),(11,9)]
print(closestPair(A))

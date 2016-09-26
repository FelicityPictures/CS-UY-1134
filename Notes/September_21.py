def rev(A):
#bad code
    if len(A):
        return rev(A[1:])+[A[0]]
    else:
        return A
A = [0,1,2,3,4]
B = rev(A)
# print(B)
#should print [4,3,2,1,0]

def sum(A):
    if len(A):
        return A[0]+sum(A[1:])
    else:
        return 0
#Also written: return A[0]+sum(A[1:]) if len(A) else 0
#One line of code #swag
AA=[5,7,4,3,2]
#print(sum(AA))

def recsum(A):
    B=[recsum(x) if isinstance(x,list) else x for x in A]
    return sum(B)

def correctFlatten(A):
    if len(A):
        return f(A[0]) + f(A[1:]) if isinstance(A[0], list) else [A[0]] + f(A[1:])
    else:
        return A

def f(A):
    if isinstance(A,list):
        return f(A[0])+f(A[1:])
    else:
        return [A]

c=[5,[7,4],3,2,[],[[2,3]]]
d=[5,11,3,2,0,5]
# print(c)
# print(f(c))

def tr(A,x,y):
    uc,ud=tr(A,x-1,y) if x>0 else (0,"")
    lc,ld=tr(A,x,y-1) if y>0 else (0,"")
    if lc>uc:
        return (lc+A[x][y],"L"+ld)
    else:
        return (uc+A[x][y],"U"+ud)
#String operation takes linear time
#O(2^(2n))
ex = [[1,1,1,0],
      [0,0,1,0],
      [0,0,1,0],
      [3,0,1,1]]
print(tr(ex,3,3))

def foo(x):
    x[0]=x[0]+1
    return x
y=[3]
z=foo(y)
print(y)
print(z)

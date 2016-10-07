def f(x,n):
    temp=1
    ret=0
    while n>=0:
        ret+=temp
        temp=temp*x
        n-=1
    return ret

print(f(2,3))

def anyincommon(A,B):
    for a in A:
        if a>=B[0] and a<=B[-1]:
            for b in B:
                if a==b:
                    return True
                if a>b:
                    break
    return False

a=[0,1,2,3]
b=[-3,5,6]

print(anyincommon(a,b))

# def rev(A):
#     if len(A)<2:
#         return A
#     else:
#         return rev(A[int(len(A)/2):]) + rev(A[:int(len(A)/2)])
# print(rev(a))

def rev(A):
    ret = []
    for i in range(len(A)):
        ret.append(A.pop())
    return ret

print(rev(a))

def transpose(A):
    ret = []
    for c in range(len(A[0])):
        ret.append([m[c] for m in A])
    return ret

B=[ [1,2,3],[4,5,6],[7,8,9]]
print(transpose(B))

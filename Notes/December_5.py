#December 5th, 2016

A = "acabacbaacbaafcca"
B = "cbaaabcabaafcaaaa"
#strings don't have pops. Make them arrays
def helperLCS(A,B,a,b,T): #longest common subsequence
#Can't do T[(A,B)] because A,B have to be immutable
    if (a,b) in T:
        return T[(a,b)]
    if a==-1 or b==-1:
        return 0
    else:
        if A[-1]==B[-1]:
            w = LCS(A,B,a-1,b-1,T)
            T[(a,b)]=w #T[(A,B,a,b)] would also work but it's fine cuz A and B never changes, anyways
            return T[(a,b)]+1
        else:
            w1 = LCS(A,B,a-1,b,T)
            w2 = LCS(A,B,a,b-1,T)
            T[(a,b)]=max(w1,w2)
            return T[(a,b)]
LCS(A,B,len(A)-1,len(B)-1,T={}):
    return helperLCS(A,B,a,b,T)
#O(n^2)

def F(n,T={}):
    if n in T:
        return T[n]
    if n<2:
        T[n]=1
        return T[n]
    else:
        T[n] = F(n-1)+F(n-2)
        return Ts[n]

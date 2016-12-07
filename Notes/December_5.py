#December 5th, 2016

A = "acabacbaacbaafcca"
B = "cbaaabcabaafcaaaa"
#strings don't have pops. Make them arrays
def helperLCS(A,B,a,b,T): #longest common subsequence
#Can't do T[(A,B)] because A,B have to be immutable
    if (a,b) in T:
        return T[(a,b)]
    if a==-1 or b==-1:
        T[(a,b)]=(0,0)
        return (0,0)
    else:
        if A[-1]==B[-1]:
            w = LCS(A,B,a-1,b-1,T)
            T[(a,b)]=(w+1,(S,A[a])) #T[(A,B,a,b)] would also work but it's fine cuz A and B never changes, anyways
            return (w+1,(S,A[a]))
            """
            also:
            S.append(A[a])
            return (w+1,S)
            Faster:
            tuples in tuples in tuples...
            return (w+1,(S,A[a]))
            """
        else:
            (w1,S1) = LCS(A,B,a-1,b,T)
            (w2,S2) = LCS(A,B,a,b-1,T)
            T[(a, b)] = (w1, s1) if w1>w2 else (w2, s2)
            return T[(a,b)]
#O(n^2)

def realLCS(A,B):
    (w,s)=helperLCS(A,B,len(A),len(B),{})
    A = unparen(S)
    this = "".join(A)
    return (w,A)
def unparen(S):
    if S ==(,):
        return []
    else:
        A = unparent(S[0])
        A.append(S[1])
        return A



def F(n,T={}):
    if n in T:
        return T[n]
    if n<2:
        T[n]=1
        return T[n]
    else:
        T[n] = F(n-1)+F(n-2)
        return T[n]

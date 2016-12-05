#November 28th, 2016
"""
Sorting is n or worse. >nlogn
heapSort - O(nlogn)
mergeSort - split and reorder O(nlogn)
quickSort - O(nlogn) ... O(n^2)-best case ... worst

"""

def mergeSort(A):
    #sacrifices memory space
    if len(A)<=1:
        return A
    else:
        L = A[0:len(A)//2]
        R = A[len(A)//2:]
        ms(L)
        ms(R)
        l = 0
        r = 0
        for i in range(len(A)):
            if L[l]<R[r]:
                A[i] = L[l]
                l+=1
            else:
                A[i]=R[r]
                r+=1

def quickSort(A):
    if len(A)>1:
        P = A[0] #random is better but it takes a toll on the system
        S = []
        L = []
        for x in A[1:]:
            if x<P:
                S.append(x)
            else:
                L.append(x)
        qs(S)
        qs(L)
        return S+[P]+L

"""
ceiling(log(base 2)n!)
log(base 2) is the number of comparisons
n! is the number of permutations



"""

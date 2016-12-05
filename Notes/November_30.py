#November 30, 2016

"""
Counting sort:
For when you know what value the things are going to be

count-sort(A,k) - all the dadta is 0...k-1
    T = []*k
    for a in A:
        T[a[0]].append(a)
    i=0
    for t in T:
        for a in T:
            A[i]=a
            i+=1

for example: (1,x) (2,4) (1,2) (3,a) (2,m) (1,l)
Buckets | Things
1       | (1,x) (1,z) (1,l)
2       | (2,y) (2,m)
3       | (3,a)
4       |
5       |
Stable sort cuz it doesn't move stuff. Unlike quickSort, which moves stuff everywhere

count-sort(A,5,lambda x:x[0])
OR: count-sort(A,5,itemgetter(x))
    def itemgetter(A):
        return A[0]

radix sort can be better than counting sort when there are too many passes
python's sort is called timsort. It's stable. Breaks it into 64-bit things and checks to see if it's sorted
already, whether in ascending or descending order. Then it runs insertion sort then merge sort.

A.sort(Key=attrgetter("element"))
            lambda x: x.element()
            methodcaller("len")

Sorting tuple: it sorts the first element then the ones after that.
[("John","Iacono"),("...","..."),....]
However, for names: A.sort(Key=itemgetter(1,0))
Sorts by second element in tuple then first, so it sorts by last name first.

Selection:
0 10 20 50 71 72 73 78 84 87 89 95 98

Finding median: 73

select(A,k):
    S = sorted(A)
    return S[k]

median(A) would return select(A,len(A)//2)

8 7 10 5 52 67 51 0 1 2 6
Finding 6th largest element:
pivot: 8
smaller: 7 5 0 1 2 6
larger: 10 52 67 51

QSelect(A,k):
    p = A[0]
    s = []
    l = []
    for x in A[1:]:
        if x<p:
            s.append(x)
        else:
            l.append(x)
    if k == len(s)+1:
        return p
    elif k<len(s)+1:
        return QSelect(S,k)
    else:
        return QSelect(L,k-len(s)-1)

"""

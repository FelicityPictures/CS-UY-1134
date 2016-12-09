import math,random

def select(arr,k,lim=5):
    return selecth(arr,k,lim,0,len(arr))

def selecth(arr,k,lim,start,end):
    if end>len(arr):
        end = len(arr)
    median = MoM(arr,lim,start,end)
    if end-start>=2:
        x = start+1
        s = start+1
        l = end-1
        print(median)
        print(arr)
        while x<end and s<l:
            if arr[x]<median[0]:
                arr[s],arr[x]=arr[x],arr[s]
                s+=1
            if arr[x]>median[0]:
                arr[l],arr[x]=arr[x],arr[l]
                l-=1
                x-=1
            x+=1
    if arr[s]>median[0]:
        try:
            if arr[s-1]<median[0]:
                arr[median[1]],arr[s-1]=arr[s-1],arr[median[1]]
                median=(median[0],s-1)
            else:
                arr[median[1]],arr[s-2]=arr[s-2],arr[median[1]]
                median=(median[0],s-2)
        except IndexError:
            pass
    else:
        try:
            if arr[s+1]>median[0]:
                arr[median[1]],arr[s]=arr[s],arr[median[1]]
                median=(median[0],s)
            else:
                arr[median[1]],arr[s+1]=arr[s+1],arr[median[1]]
                median=(median[0],s+1)
        except IndexError:
            pass
        # if arr[s]<median[0] and arr[s+1]>median[0]:
        #     arr[start],arr[s]=arr[s],arr[start]
        #     median = (median[0],s) #medpt is index of array where the median is
        # else:
        #     if arr[s-1]<median[0] and arr[s]>median[0]:
        #         arr[start],arr[s-1]=arr[s-1],arr[start]
        #         median = (median[0],s-1)
    if k==median[1]:
        print(median)
        print(arr)
        print(k)
        return median[0]
    else:
        # print("median after moving stuff" + str(median))
        # print(arr)
        # print('k: ' + str(k))
        # print('median: ' + str(median))
        if k<median[1]:
            # print("s")
            return selecth(arr,k,lim,start,median[1])
        else:
            # print('l')
            # print((median[1]+1,end))
            return selecth(arr,k,lim,median[1]+1,end)

def s(arr,start,end): #does not include end
    if end>len(arr):
        end = len(arr)
    for m in range(end-start-1):
        if arr[start+m]>arr[start+m+1]:
            arr[start+m],arr[start+m+1]=arr[start+m+1],arr[start+m]
        for x in range(m):
            if arr[start+m-x]<arr[start+m-x-1]:
                arr[start+m-x],arr[start+m-x-1]=arr[start+m-x-1],arr[start+m-x]
    return arr

def MoM(arr,lim,start,end):
    if end-start<2:
        return (arr[start],start)
    numparts = math.ceil((end-start) / lim)
    for begin in range(numparts):
        s(arr,start+(begin*lim),start+(begin*lim)+lim)
    for x in range(numparts):
        if start+(x*lim)+(lim//2)>=end:
            arr[start+x],arr[start+(x*lim)+((end-(start+(x*lim)))//2)]=arr[start+(x*lim)+((end-(start+(x*lim)))//2)],arr[start+x]
        else:
            arr[start+x],arr[start+(x*lim)+(lim//2)]=arr[start+(x*lim)+(lim//2)],arr[start+x]
    return getMedian(arr,start,start+numparts)

def getMedian(arr,start,end): #Does not look at arr[end]
    # print("start,end " + str((start,end)))
    # print("from this: " +str(arr))
    if end-start-1<=2:
        return (arr[start],start)
    else:
        for x in range(end-start):
            if arr[start+x]<arr[start]:
                arr[start],arr[start+x]=arr[start+x],arr[start]
            if arr[start+x]>arr[end-1]:
                arr[end-1],arr[start+x]=arr[start+x],arr[end-1]
    return getMedian(arr,start+1,end-1)

###################################################################################################
# f = list(range(222))
# random.shuffle(f)
# print("original: " + str(f))
# # print(s(felicity,2,20))
# # print(f)
# print([select(f,i) for i in range(len(f))])
# # print(s(f,0,100))


A=list(range(24))
random.shuffle(A)
print(select(A,23))
# print([select(A,i) for i in range(220)])

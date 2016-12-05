import math
class HT:
    def __init__(self):
        self._A = []
        self._B = []
        for x in range(10):
            self._A.append(None)
            self._B.append(None)
        self._size = 0
    # def h1(self,key):
    #     v = math.degrees(key)
    #     v = math.hypot(key, v)
    #     v = v%(math.pow(10,(math.ceil(math.log(len(self._A),10)))))
    #     v = math.fabs(v-(len(self._A)))
    #     return math.floor(v)
    # def h2(self,key):
    #     v = math.degrees(key)+math.radians(key)+218
    #     v = math.hypot(key, v)
    #     v = v%(math.pow(10,(math.ceil(math.log(len(self._A),10)))))
    #     v = math.fabs(v-(len(self._A)))
    #     return math.floor(v)
    def __getitem__(self,key):
        # print('__getitem__')
        # print (key)
        if self._A[hash((key,0))%len(self._A)]!=None and self._A[hash((key,0))%len(self._A)][0]==key:
            return self._A[hash((key,0))%len(self._A)][1]
        if self._B[hash((key,1))%len(self._B)]!=None and self._B[hash((key,1))%len(self._B)][0]==key:
            return self._B[hash((key,1))%len(self._B)][1]
        return 'error'
    def _resize(self):

        #hold = self.items()
        hold=[]
        for val in self._A:
            if val != None:
                hold.append(val)
        for val in self._B:
            if val != None:
                hold.append(val)
        # print('hold')
        # print(hold)
        # for x in self._A:
        #     if x!=None:
        #         hold.append(x)
        # for x in self._B:
        #     if x!=None:
        #         hold.append(x)
        l = len(self._A)
        self._A = []
        self._B = []
        for x in range(l*2):
            self._A.append(None)
            self._B.append(None)
        for val in hold:
            self[val[0]]=val[1]
    def __setitem__(self,k,v):
        if self._size >= len(self._A)-1:
            self._resize()
        h = self._A[hash((k,0))%len(self._A)]
        if h!=None and h[0]==k:
            m = (k,v)
            self._A[hash((k,0))%len(self._A)]=m
        else:
            h=self._B[hash((k,1))%len(self._B)]
            if h!=None and h[0]==k:
                m=(k,v)
                self._B[hash((k,1))%len(self._B)]=m
            else:
                self._size += 1
                h = self._A[hash((k,0))%len(self._A)]
                self._A[hash((k,0))%len(self._A)]=(k,v)
                initial=hash((k,0))%len(self._A)
                if h != None:
                    self._help(h,1,initial)
                else:
                    return "wrong"
    def _help(self,t,arr,initial):
        if initial == hash((t[0],arr))%len(self._A):
            self._resize()
            # print('resize')
            #print(t)
            self[t[0]]=t[1]
            return
        if arr == 1:
            h = self._B[hash((t[0],1))%len(self._B)]
            # if (h[0]==t[0]):
            #     self._B[hash((t[0],1))%len(self._B)] = t
            #     return
            #print(h)
            self._B[hash((t[0],1))%len(self._B)] = t
            #print(self._B[hash((t[0],1))%len(self._B)])
            if h != None:
                if (h[0]==t[0]):
                    #self._B[hash((t[0],1))%len(self._B)] = t
                    return
                self._help(h,0,initial)
            else:
                self._size += 1
                return
        else:#if it's 0, which means A array
            h = self._A[hash((t[0],0))%len(self._A)]
            #print(h)
            self._A[hash((t[0],0))%len(self._A)] = t
            #print(self._A[hash((t[0],0))%len(self._A)])
            if h != None:
                if (h[0]==t[0]):
                    #self._A[hash((t[0],0))%len(self._A)] = t
                    return
                self._help(h,1,initial)
            else:
                self._size += 1
                return
    def __delitem__(self,k):
        if self._A[hash((k,0))%len(self._A)]!=None and self._A[hash((k,0))%len(self._A)][0]==k:
            self._A[hash((k,0))%len(self._A)]=None
            self._size -= 1
        if self._B[hash((k,1))%len(self._B)]!=None and self._B[hash((k,1))%len(self._B)][0]==k:
            self._B[hash((k,1))%len(self._B)]=None
            self._size -= 1
    def __len__(self):
        return self._size
    def __contains__(self,key):
        if self._A[hash((key,0))%len(self._A)]!=None:
            return True
        if self._B[hash((key,1))%len(self._B)]!=None:
            return True
        return False
    def __iter__(self):
        for m in self._A:
            if m != None:
                yield m
        for m in self._B:
            if m != None:
                yield m
    def keys(self):
        for i in range(len(self._A)):
            if self._A[i]!=None:
                yield self._A[i][0]
            if self._B[i]!=None:
                yield self._B[i][0]
    def values(self):
        for i in range(len(self._A)):
            if self._A[i]!=None:
                yield self._A[i]
            if self._B[i]!=None:
                yield self._B[i]
    def items(self):
        arr = []
        for x in self._A:
            if x!=None:
                arr.append(x)
        for x in self._B:
            if x!=None:
                arr.append(x)
        return arr

# for x in range(30):
#     print("x: " + str(x))
#     print(T.hash((x,0)))
#     print(T.hash((x,1)))
#
# T=HT()
# for i in range(100):
#     T[i]=i*i
# # tmp=sorted(T.keys())
# # for i in tmp:
# #     print (T[tmp])
# # print('---------')
# # print (T._A)
# # print (T._B)
# # print('---------')
# # tmp=sorted(T.keys())
# # print(tmp)
# # print('---------')
# # print (T._A)
# # print (T._B)
# # print('---------')
#
# for i in T.keys():
#     T[i]=T[i]+1
# for i in range(5,400):
#     if i in T:
#         del T[i]
# # print('---------')
# # print (T._A)
# # print (T._B)
# # print('---------')
# K=T.items()
# K.sort()
# print(K)
# print(len(K))
T=HT()
for i in range(200):
    T[i]=i*i
for i in T.keys():
    T[i]=T[i]+1
for i in range(5,400):
    if i in T:
        del T[i]
K=T.items()
K.sort()
print(K)
print(len(K))

# #output:
#[(0, 1), (1, 2), (2, 5), (3, 10), (4, 17)]
#5

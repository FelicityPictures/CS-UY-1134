#December 13th, 2016

def canReach(G,v):
    answer = {}
    answer[v] = True
    q = dequeue()
    q.push(v)
    while not q.is_empty():
        w = q.popleft()
        for e in G.incident_edges(w):
            x = e.opposite(w)
        if x not in answer:
            answer[x]=True
            q.push(x)
    return answer

#Breadth-FIrst Search
def distance(G,v):
    answer = {}
    answer[v] = 0
    q = dequeue()
    q.push(v)
    while not q.is_empty():
        w = q.popleft()
        for e in G.incident_edges(w):
            x = e.opposite(w)
        if x not in answer:
            answer[x]=answer[w]+1
            q.push(x)
    return answer

def shortestPath(G,v,y):
    answer = {}
    prior = {}
    prior[v] = None
    answer[v] = 0
    q = dequeue()
    q.push(v)
    while not q.is_empty():
        w = q.popleft()
        for e in G.incident_edges(w):
            x = e.opposite(w)
        if x not in answer:
            answer[x]=answer[w]+1
            prior[x] = w
            q.push(x)
    return answer

#OR
def shortestPath(G,v,y):
    #Path stuff
    path = []
    while prior[y] is not None:
        path.append(y)
        y = prior[y]
    path.append(y)
    path.reverse()
    return(path)

#Depth First Search
def DFS(G,v,answer,start,stop,time):
    #Assume answer is initialized to an empty dictionary
    #Start,stop are initially empty and time is initially 0
    time+=1
    start[v] = time
    answer[v]=True
    for e in G.incident_edges(v):
        w = e.opposite()
        if w not in answer:
            DFS(G,w,answer,start,stop,time)
    time+=1
    stop[v]=time

def tsort(G):
#G has to be a Directed Acyclic Graph (DAG)
    output = []
    arrowIn = {}
    zeros = []
    for v in G.vertices():
        arrowIn[v]=G.degree(v,False)
        if arrowIn[v] == 0:
            zeros.append(v)
        while not zeros.is_empty():
            v = zeros.pop()
            for e in G.incident_edges(v):
                w = e.opposite()
                if arrowIn[w]>0:
                    arrowIn[w]-=1
                    if arrowIn[w]==0:
                        zeros.append(w)
                output.append(w)

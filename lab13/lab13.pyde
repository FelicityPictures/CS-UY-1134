import copy
import xml.etree.ElementTree as etree

def getMap(file):
    """
    This loads the map and returns a pair (V,E)
    V contains the coordinates of the veritcies
    E contains pairs of coordinates of the verticies
    """
    G=open(file)   
    root = etree.parse(G).getroot()
    v={}
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e

from graph import Graph

class Map:
    def __init__(self,v,e):
        self._g = Graph()
        self._closest_edge = None
        self._discovered={}
        d = {}
        for x in v:
            d[x]=self._g.insert_vertex(x)
        for x in e:
            try:
                self._g.insert_edge(d[x[0]],d[x[1]])
            except ValueError:
                pass
    def DFS(self,e,c):
        if c<=0:
            return
        u = e.endpoints()[0]
        r = e.endpoints()[1]
        for f in self._g.incident_edges(u):# for every outgoing edge from u
            if f not in self._discovered:
                self._discovered[f] = c
                self.DFS(f,c-2) # recursively explore from v
        for f in self._g.incident_edges(r):# for every outgoing edge from u
            if f not in self._discovered:
                self._discovered[f] = c
                self.DFS(f,c-2) # recursively explore from v
         
    def calculate(self,loc):
        r = 1000
        self._discovered = {}
        for p in self._g.edges():
            v = p.endpoints()
            p1 = v[0].element()
            p2 = v[1].element()
            d1 = dist(p1[0],p1[1],loc[0],loc[1])
            d2 = dist(p2[0],p2[1],loc[0],loc[1])
            if d1<r:
                r = d1
                self._closest_edge = p
            if d2<r:
                r = d2
                self._closest_edge = p
        self.DFS(self._closest_edge,255)
            
    def draw(self):
        global maxlat,minlat,maxlon,minlon
        maxlat=40.6903
        minlat=40.7061
        maxlon=-73.9728
        minlon=-74.0065
        scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
        translate(-minlon,-minlat)
        stroke(0,0,0)
        strokeWeight(0.00001)
        for p in self._g.edges():
            v = p.endpoints()
            line(v[0].element()[0],v[0].element()[1],v[1].element()[0],v[1].element()[1])
            if self._closest_edge!=None:
                if p == self._closest_edge:
                    stroke(0,0,255)
                    strokeWeight(.0001)   
                    line(v[0].element()[0],v[0].element()[1],v[1].element()[0],v[1].element()[1])
                    stroke(0,0,0)
                    strokeWeight(0.00001)
                elif p in self._discovered:
                    stroke(255-self._discovered[p],0,self._discovered[p])
                    strokeWeight(.00005)   
                    line(v[0].element()[0],v[0].element()[1],v[1].element()[0],v[1].element()[1])
                    stroke(0,0,0)
                    strokeWeight(0.00001)
            
        
def setup():
    size(1500,1500)
    background(255)
    (v,e) = getMap('map.osm')
    global m
    m = Map(v,e)
def draw():
    background(255)
    m.draw()
    print('loop')
    print(m._closest_edge)
    
def mouseToScreen(mx,my):
    return (minlon+(mx/float(width))*(maxlon-minlon),minlat+(my/float(height))*(maxlat-minlat))

def mouseClicked():
    loc = mouseToScreen(mouseX,mouseY)
    m.calculate(loc)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
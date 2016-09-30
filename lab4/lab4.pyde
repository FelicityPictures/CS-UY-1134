#Ng, Felicity

import random
import copy

screenwidth = 1500
screenheight = 1000
s=50

class Cell:
    def __init__(self,location,color,on=False):
        self._color = color
        self._on = on
        self._x = location[0]
        self._y = location[1]
    def draw(self):
        if self._on:
            fill(*self._color)
        else:
            fill(255,255,255)
        rect(self._x,self._y,s,s)
    def loc(self):
        return self._x,self._y
    def on(self):
        return self._on
    def turnOn(self,c):
        if c==2:
            self._color=(0,0,255)
        else:
            self._color=(255,0,0)
        if c==3 and self._on==False:
            self._on=True
            # print('change')
            return
        if self._on==True:
            return
    def turnOff(self):
        # print('turnoff')
        self._on=False
    def click(self):
        self._on = not self._on
        # print(self._on)
    
def run(x,y):
        count = 0
        try:
            if grid[x+1][y].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x+1][y+1].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x+1][y-1].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x-1][y].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x-1][y+1].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x-1][y-1].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x][y+1].on():
                count+=1
        except IndexError:
            pass
        try:
            if grid[x][y-1].on():
                count+=1
        except IndexError:
            pass
        print(x,y,count)
        if count==2 or count==3:
            next[x][y].turnOn(count)
        else:
            next[x][y].turnOff()
def randomColor():
    return [random.randrange(255) for i in range(3)]
        
def setup():
    size(screenwidth, screenheight)
    frameRate(2)
    global grid,next,pause
    pause = False
    grid = []
    next = []
    x = int(screenwidth/s)-1
    y = int(screenheight/s)-1
    for i in range(x):
        # grid.append([Cell((s*i+(s/2),s*m+(s/2)),randomColor(),bool(random.getrandbits(1))) for m in range(y)])
        # next.append([Cell((s*i+(s/2),s*m+(s/2)),randomColor(),bool(random.getrandbits(1))) for m in range(y)])
        # print(100*i,100*m)
        grid.append([Cell((s*i+(s/2),s*m+(s/2)),randomColor(),False) for m in range(y)])
    next = copy.deepcopy(grid)
    
def draw():
    clear()
    background(111)
    global grid,next
    next=copy.deepcopy(grid)
    for i in range(len(grid)):
        for m in range(len(grid[i])):
            grid[i][m].draw()
            if not pause:
                run(i,m)
    grid=copy.deepcopy(next)

def keyPressed():
    if key==' ':
        global pause
        pause = not pause
        print(pause)
    if key=='n':
        global grid
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                grid[i][m].turnOff()
    if key=='r':
        global grid,next
        grid = []
        next = []
        x = int(screenwidth/s)-1
        y = int(screenheight/s)-1
        for i in range(x):
            grid.append([Cell((s*i+(s/2),s*m+(s/2)),randomColor(),bool(random.getrandbits(1))) for m in range(y)])
        next=copy.deepcopy(grid)
        
def mousePressed():
    if mouseX>s/2 and mouseX<screenwidth-s/2 and mouseY>s/2 and mouseY<screenheight-s/2:
        grid[int((mouseX-(s/2))/s)][int((mouseY-(s/2))/s)].click()
        print(int((mouseX-(s/2))/s),int((mouseY-(s/2))/s))
    
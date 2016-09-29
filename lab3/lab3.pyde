"""
pressing 's' would cause the tree to start swaying.
pressing 'l' would display leaves
pressing 'n' would display the nodes of the tree
moving your mouse over the leaves would cause them to fall
"""

import sys
import random
import math

screenwidth=2000
screenheight=1200
trunkheight = 100
trunkwidth = 50
brancht = 25
numb = 0
levels = 7
leaves = []
swayleft = -1 #default -1
swayLnumb = .001
swayright = 1 #default 1
swayRnumb= -.001
falling = []

def setup():
    size(screenwidth, screenheight)
    background(255)
    pixelDensity(displayDensity())

def drawLineAngle(color, start, angle, length, width=1):
    angle += 180  # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(0)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

class l:
    def __init__(self,location):
        self._location = location
        self._fall = False
    def drawLeaf(self):
        stroke(0, 50, 0)
        fill(100, 255, 100)
        strokeWeight(0.5)
        ellipse(self._location[0],self._location[1],20,20)
    def startFall(self,x,y):
        if math.hypot(self._location[0] - x, self._location[1] - y) <= 20:
            self._fall = True
            return True
        return False
    def stopFall(self):
        self._fall = False
    def fall(self):
        if self._fall == True:
            temp = list(self._location)
            temp[1]+=3
            self._location = tuple(temp)
        if self._location[1]>screenheight:
            del self

def drawNodes(location):
    stroke(0, 0, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0],location[1],30,30)
    stroke(255,50,0)
    global numb
    textSize(20)
    fill(0,0,0);
    temp = textWidth(str(numb))
    text(numb,location[0]-int(temp/2),location[1]+10)
    numb+=1

def drawTree(start,angle,branchlength,fat,count):
    end = drawLineAngle((255,0,0),start,angle,branchlength-3,fat+3)
    endL = drawLineAngle((0,255,255),end,angle+brancht,branchlength-5,fat-2)
    endR = drawLineAngle((0,0,255),end,angle-brancht,branchlength-5,fat-2)
    if count<levels:
         drawTree(endL,swayright*(brancht+angle),branchlength-10,fat-5,count+1)
         drawTree(endR,swayleft*(brancht-angle),branchlength-10,fat-5,count+1)
    else:
        if set:
            leaves.append(l(endL))
            leaves.append(l(endR))
    if nodes:
         drawNodes(endL)
         drawNodes(endR)
         
def s():
    global swayleft, swayLnumb, swayright, swayRnumb, set, leaves
    
    if swayL == None:
        swayleft += swayLnumb
        if swayleft>=-0.975 or swayleft<=-1:
                swayLnumb=swayLnumb*-1
        swayright += swayRnumb
        if swayright>=1 or swayright<=0.975:
                swayRnumb=swayRnumb*-1
    else:
        if swayL:
            swayleft += swayLnumb
            if swayleft>=-0.975 or swayleft<=-1:
                swayLnumb=swayLnumb*-1
        else:
            swayright += swayRnumb
            if swayright>=1 or swayright<=0.975:
                swayRnumb=swayRnumb*-1
    set=True
    # make sure it matches draw
    leaves=[]
    drawTree((int(screenwidth/2),screenheight-10),0,trunkheight,trunkwidth,0)
    set=False

def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf
        print(leaf)
        if leaf==False:
            global leaves,falling
            leaves = []
            falling = []
        else:
            global set
            set=True
            # make sure it matches draw
            drawTree((int(screenwidth/2),screenheight-10),0,trunkheight,trunkwidth,0)
            set=False
    global nodes
    if key=="n":
        nodes = not nodes
    global sway
    if key=="s":
        sway = not sway
        # set=True
        # # make sure it matches draw
        # drawTree((int(screenwidth/2),screenheight-10),0,trunkheight,trunkwidth,0)
        # set=False
def setup():
    global leaf
    leaf=False
    global nodes
    nodes=False
    background(255)
    global set
    set=True
    # make sure it matches draw
    drawTree((int(screenwidth/2),screenheight-10),0,trunkheight,trunkwidth,0)
    set=False
    global sway
    global swayL
    sway=False
    swayL=False

def draw():
    global numb
    numb=0
    clear()
    background(255)
    # make sure it matches setup
    # drawLineAngle(0, (int(screenwidth/2),screenheight), 0, 400, trunkwidth)
    drawTree((int(screenwidth/2),screenheight-10),0,trunkheight,trunkwidth,0)
    if sway:
        s()
    if leaf:
        for x in leaves:
            x.drawLeaf()
            x.fall()
        for x in falling:
            x.drawLeaf()
            x.fall()
def mouseMoved():
    if leaf:
        for x in leaves:
            if x.startFall(mouseX,mouseY):
                falling.append(x)
                leaves.remove(x)
    if sway:
        global swayL
        if mouseX<int(screenwidth/3):
            swayL=False
        else:
            if mouseX>2*int(screenwidth/3):
                swayL=True
            else:
                
                swayL = None
        
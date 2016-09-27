import sys
import random
import math

screenwidth=2000
screenheight=1200
trunkheight = 200
trunkwidth = 50
angle = 25
brancht = 25
numb = 0
levels = 7
leaves = []

def setup():
    size(screenwidth, screenheight)
    background(255)
    pixelDensity(displayDensity())

def drawLineAngle(color, start, angle,tilt, length, width=1):
    angle += 180-tilt  # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(0)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

class l():
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
    def stopFall(self):
        self._fall = False
    def fall(self):
         if self._fall == True:
            temp = list(self._location)
            temp[1]+=3
            self._location = tuple(temp)

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

def drawTree(start,leaf,):
    end = drawLineAngle((255,0,0),start,0,0,trunkheight,trunkwidth)
    endL = drawLineAngle((0,255,255),end,angle,0,trunkheight-20,trunkwidth-15)
    endR = drawLineAngle((0,0,255),end,-angle,0,trunkheight-20,trunkwidth-15)
    drawLeftBranches(endL,brancht,leaf,trunkheight-30,trunkwidth-10,0)
    drawRightBranches(endR,brancht,leaf,trunkheight-30,trunkwidth-10,0)
    if nodes:
         drawNodes(end)
         drawNodes(endL)
         drawNodes(endR)
def drawLeftBranches(start,tilt,leaf,branchlength,fat,count):
    endL = drawLineAngle((0,255,255),start,angle,-tilt,branchlength,fat)
    endR = drawLineAngle((0,0,255),start,-angle,-tilt,branchlength,fat)
    if count<levels:
        drawLeftBranches(endL,tilt+brancht,leaf,branchlength-20,fat-5,count+1)
        drawLeftBranches(endR,tilt-brancht,leaf,branchlength-20,fat-5,count+1)
    else:
        if set:
            leaves.append(l(endL))
            leaves.append(l(endR))
    if nodes:
         drawNodes(endL)
         drawNodes(endR)
def drawRightBranches(start,tilt,leaf,branchlength,fat,count):
    endL = drawLineAngle((0,255,255),start,angle,tilt,branchlength,fat)
    endR = drawLineAngle((0,0,255),start,-angle,tilt,branchlength,fat)
    if count<levels:
        drawRightBranches(endL,tilt-brancht,leaf,branchlength-20,fat-5,count+1)
        drawRightBranches(endR,tilt+brancht,leaf,branchlength-20,fat-5,count+1)
    else:
        if set:
            leaves.append(l(endL))
            leaves.append(l(endR))
    if nodes:
         drawNodes(endL)
         drawNodes(endR)

def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf
    global nodes
    if key=="n":
        nodes = not nodes
def setup():
    global leaf
    leaf=False
    global nodes
    nodes=False
    background(255)
    global set
    set=True
    drawTree((int(screenwidth/2),screenheight-10),leaf)
    set=False

def draw():
    global numb
    numb=0
    clear()
    background(255)
    drawTree((int(screenwidth/2),screenheight-10),leaf)
    if leaf:
        for x in leaves:
            x.drawLeaf()
            x.fall()
def mouseMoved():
    if leaf:
        for x in leaves:
            x.startFall(mouseX,mouseY)
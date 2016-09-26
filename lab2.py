#Felicity Ng
import turtle
import math
import random

def randomRadius(min=50):
    return random.randrange(min,150)
def randomSize(max=35):
    return random.randrange(max)+5
def randomSpeed():
    return random.uniform(.0002,.01)
def randomColor():
    return [random.random() for i in range(3)]

#size is radius
class Sun:
    def __init__(self,center,size,color):
        self._t=turtle.Turtle()
        self._size=size
        self._color=color
        self._center=center
    def draw(self):
        self._t.clear()
        turtle.tracer(0,0) #This speeds things up
        self._t.penup()
        self._t.dot(self._size*2,self._color)
    def setColor(self,color):
        self._color=color
    def inside(self,location):
        x=location[0]
        y=location[1]
        return math.hypot(self._center[0] - x, self._center[1] - y) <= self._size
        #from old homework
        # if x>=(self._center[0]-self._size) and x<=(self._center[0]+self._size) and y>=(self._center[1]-self._size) and (y<=self._center[1]+self._size):
        #     distance=math.sqrt(((self._center[0]-x)**2)+((self._center[1]-y)**2))
        #     if distance<=self._size:
        #         return True
        # return False
    def onClick(self,location):
        if self.inside(location):
            return True
        else:
            return False
    def sizeUp(self):
        self._size+=1
    def sizeDown(self):
        self._size-=1
    def randColor(self):
        self._color=randomColor()

class Planet(Sun):
    def __init__(self,orbitAround,orbitRadius,size,color,speed):
        self._orbitRadius=orbitRadius
        self._angle=0
        self._orbitAround=orbitAround
        self._t=turtle.Turtle()
        self._speed=speed
        super().__init__([x+self._orbitRadius*f(self._angle)
                            for x,f in zip(orbitAround._center, (math.sin,math.cos))],size,color)
    def biggerOrbitRadius(self):
            self._orbitRadius+=1
    def smallerOrbitRadius(self):
        if self._orbitRadius>0:
            self._orbitRadius-=1
    def faster(self):
        self._speed+=.001
    def slower(self):
        self._speed-=.001
    def move(self):
        location=[x+self._orbitRadius*f(self._angle)
                  for x,f in zip(self._orbitAround._center, (math.sin,math.cos))] #Some trig to compute the location
        self._t.penup()
        self._t.goto(*location)
        self._center=location
        self._angle+=self._speed
    def draw(self):
        Sun.draw(self)
        self.move()

def drawPlanet(center,size,color,orbitRadius,angle):
    location=[x+orbitRadius*f(angle)
              for x,f in zip(center, (math.sin,math.cos))] #Some trig to compute the location
    turtle.penup()
    turtle.goto(*location)
    turtle.dot(size*2,color) #dot takes diameter rather than radius

class SolarSystem:
    def __init__(self,numberOfBodies=3):
        global celestialBodies
        celestialBodies=[]
        celestialBodies.append(Sun((0,0), 50, "yellow"))
        for i in range(numberOfBodies):
            orbitA=random.randrange(len(celestialBodies))-int(len(celestialBodies)/2)
            if orbitA<0:
                orbitA=0
            oz=celestialBodies[orbitA]._size
            rz=randomSize(oz)
            #orbitAround,orbitRadius,size,color,speed
            celestialBodies.append(Planet(celestialBodies[orbitA],randomRadius(oz+rz),
                                    rz,randomColor(),randomSpeed()))
    def draw(self):
        global celestialBodies
        for i in celestialBodies:
            i.draw()
    def onClick(self,location):
        for i in celestialBodies:
            temp = i.onClick(location)
            if temp:
                # print(i)
                return i
    def add(self,planet):
        n = Planet(planet,randomRadius(),randomSize(planet._size),randomColor(),randomSpeed())
        celestialBodies.append(n)
        return n

ss=SolarSystem(4)
lastClicked=ss.onClick((0,0))

def onClick(x,y):
    global lastClicked
    lastClicked = ss.onClick((x,y))
    colorChange()
def sizeUp():
    lastClicked.sizeUp()
def sizeDown():
    lastClicked.sizeDown()
def radiusUp():
    lastClicked.smallerOrbitRadius()
def radiusDown():
    lastClicked.biggerOrbitRadius()
def faster():
    lastClicked.faster()
def slower():
    lastClicked.slower()
def newPlanet():
    global lastClicked
    lastClicked=ss.add(lastClicked)
def colorChange():
    lastClicked.randColor()
def draw():
    ss.draw()
    screen.ontimer(draw,0) #This tells the system to call this function again as soon as possible

turtle.tracer(0,0)
turtle.ht()
screen=turtle.Screen() #Needed for the following
screen.bgcolor("black")
screen.onclick(onClick)
screen.onkey(turtle.bye,"q") #quits if you press q
screen.onkey(sizeUp,"Up")
screen.onkey(sizeDown,"Down")
screen.onkey(radiusDown,"Left")
screen.onkey(radiusUp,"Right")
screen.onkey(slower,"[")
screen.onkey(faster,"]")
screen.onkey(newPlanet,"n")
screen.onkey(colorChange,"space")
screen.ontimer(draw,0) #Tells the system to call draw. Don't call it directly
screen.listen()
turtle.mainloop()

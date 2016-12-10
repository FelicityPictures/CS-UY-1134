class suffixTrie:
    class Node:
        def __init__(self):
            self._children={}
        def mcn(self,mc):
            if len(self._children)==0:
                return mc
            elif len(self._children)==1:
                for m in self._children:
                    r = m
                return self._children[r].mcn(mc)
            else:
                hold = []
                for x,i in zip(self._children,range(len(self._children))):
                    hold.append(self._children[x].mcn(mc+i))
                return max(hold)
    def __init__(self,string):
        self._root = self.Node()
        while len(string)>0:
            curr=self._root
            for m in range(len(string)):
                if string[m] not in curr._children:
                    curr._children[string[m]]=self.Node()
                curr = curr._children[string[m]]
            # curr._children['$'] = self.Node()
            
            string = string[1:]
    def draw(self,x,y):
        # print('new')
        b = TextBox('_',x,y)
        self._helperD(b,self._root,x,y)
        
    def _helperD(self,before,node,x,y): #m is max x coordinate
        for object in node._children:
            print(node.mcn(0))
            txt = TextBox(object,x,y+60)
            txt.draw()
            before.drawLineToOtherBoxBelow(txt)
            self._helperD(txt,node._children[object],x,y+60)
            x=x+50+(50*node._children[object].mcn(0))
            # print(x)

class TextBox:
    TEXTSIZE = 30

    def __init__(self, text, x=0, y=0):
        self._text, self._x, self._y = text, x, y
        print(len(text))

    def replaceText(self, text):
        self._text = text

    def setLocation(self, x, y):
        self._x, self._y = x, y

    def draw(self):
        textAlign(LEFT, TOP)
        textSize(TextBox.TEXTSIZE)
        rectMode(CORNER)
        fill(255)
        stroke(0)
        strokeWeight(1)
        rect(self._x, self._y, self.width(), self.height())
        fill(0)
        text(self._text, self._x + textWidth(" ") //
             2, self._y - textDescent() // 2)

    def width(self):
        textSize(TextBox.TEXTSIZE)
        return textWidth(self._text + " ")

    def height(self):
        textSize(TextBox.TEXTSIZE)
        return textAscent() + textDescent()

    def drawLineToOtherBoxBelow(self, otherBox):
        stroke(0)
        textSize(TextBox.TEXTSIZE)
        strokeWeight(1)
        line(self._x + self.width() / 2, self._y + self.height(),
             otherBox._x + otherBox.width() / 2, otherBox._y)

def keyPressed():
    global S
    if key==u'\x08':
        S=S[:-1]
    elif key!=65535:
        S+=key
    redraw()
def setup():
    global S
    S=""
    size(1200, 1000)
    pixelDensity(displayDensity())
    noLoop()
def draw():
    background(200,150,200)
    TextBox(S,10,10).draw()
    ST=suffixTrie(S+'$')
    ST.draw(50,100)
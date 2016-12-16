class suffixTrie:
    class Node:
        def __init__(self):
            self._children={}
        def mcn(self,mc=0):
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
        def getEnd(self,node,ret=''):#only for nodes that don't branch
            if len(self._children)<1:
                return ret
            for m in self._children:
                if self._children[m] == node:
                    return self._children[m]._getEndh(ret+str(m))
        def _getEndh(self,ret=''):#only for nodes that don't branch
            if len(self._children)<1:
                return ret
            for m in self._children:
                # x=m
                return self._children[m]._getEndh(ret+str(m))
        def straight(self): #returns true if node and all its children only have one or less children
            if len(self._children)==0:
                return True
            elif len(self._children)==1:
                for m in self._children:
                    r = m
                return self._children[r].straight()
            return False
    def __init__(self,string):
        self._root = self.Node()
        while len(string)>0:
            curr=self._root
            for m in range(len(string)):
                if string[m] not in curr._children:
                    curr._children[string[m]]=self.Node()
                curr = curr._children[string[m]]
            
            string = string[1:]
    def draw(self,x,y):
        # print('new')
        b = TextBox('',x,y)
        self._helperD(b,self._root,x,y)
        
    def _helperD(self,before,node,x,y): #m is max x coordinate
        if len(node._children)>0:
            m=[]
            for c in node._children:
                txt = TextBox(c,x,y+60)
                txt.draw()
                before.drawLineToOtherBoxBelow(txt)
                m.append(self._helperD(txt,node._children[c],x,y+60))
                v = max(m)
                x=v+5#(50*len(c))
            return x
        else:
            return x+before.width()

class compressedSuffixTrie(suffixTrie):
    def __init__(self,string):
        st = suffixTrie(string)
        self._root = st._root
        for c in self._root._children:
            self._compress(self._root._children[c],self._root)
    def _compress(self,curr,before):
        if len(curr._children)==0:
            return
        else:
            if len(curr._children)==1:
                w = curr._children.keys()[0]
                for x in before._children:
                    if before._children[x]==curr:
                        before._children[x+w]=curr._children[w]
                        before._children.pop(x)
                        self._compress(before._children[x+w],before)
                        
            else:
                for x in curr._children:
                    self._compress(curr._children[x],curr)
class TextBox:
    TEXTSIZE = 30

    def __init__(self, text, x=0, y=0):
        self._text, self._x, self._y = text, x, y
        # print(len(text))

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
    print(key)
    if key == '\t':
        global compress
        compress = not compress
    else:
        if key==u'\x08':
            S=S[:-1]
        elif key!=65535:
            S+=key
    redraw()
def setup():
    global S,compress
    S=""
    compress = True
    size(1500, 1000)
    pixelDensity(displayDensity())
    noLoop()
def draw():
    background(200,150,200)
    TextBox(S,10,10).draw()
    if compress:
        ST=compressedSuffixTrie(S+'$')
    else:
        ST=suffixTrie(S+'$')
    ST.draw(50,100)
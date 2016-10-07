#October 3rd, 2016

class C:
    __slots__ = ('x','y','__dict__')
    #Use slots when you know what the variables are and that you'll make a lot of it
    #__slots__ = ('x','y','__dict__') allows variables to be reassigned
    def __init__(self,x,y):
        self.x, self.y = x,y
    # def __dict__(self):

#for a linked list node
class LinkedList:
    __slots__ = ('front','back')
    def __init__(self):
        self.front=None
        self.back=None
    class Node:
        __slots__ = ('next','value')
        def __init__(self,next,value):
            self.next=next
            self.value=value
    def insert_front(self,x):
        n = Node(self.front,x)
        self.front = n
        if not self.back:
            self.back = n
    def delete_front(self):
        self.front = self.front.next
    def front(self):
        return self.front.value
    def insert_back(self,x):
        n = Node(None,x)
        if self.back:
            self.back.next = n
        else:
            self.front = n
        self.back = n
    def delete_back(self):
        #Much easier if nodes had a previous node variable
        if self.front != self.back:
            me = self.front
            while me.next != self.back:
                me=me.next
            self.back = me
            me.next = None
        else:
            self.front = self.back = None

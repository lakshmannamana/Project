class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class single:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def traversal(self):
        temp =self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("end")
    def rev(self):
        prev=None
        temp=self.head
        while temp is not None:
            n=temp.next
            temp.next=prev
            prev=temp
            temp=n
        self.head=prev
class single1:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def traversal(self):
        temp =self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("end")  
    
'''class dummy:
    def __init__(self):
        self.head = None
    def merge(self,s,s1):
        temp=s.head
        while temp.next is not None:
            temp = temp.next
        temp.next=s1.head
        
    def traversal(self):
        temp =self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("end")'''
s = single()
s.insert_at_end(1)
s.insert_at_end(2)
s.insert_at_end(3)
s.insert_at_end(4)
s.traversal()
s1 = single1()
s1.insert_at_end(11)
s1.insert_at_end(22)
s1.insert_at_end(33)
s1.insert_at_end(44)
s1.traversal()
def merge(s,s1):
    temp=s.head
    while temp.next is not None:
        temp = temp.next
    temp.next=s1.head
    return s

def add(s,s1):
    d=Node(0)
    c=d
    a=s.head
    b=s1.head
    while a or b:
        x=a.data
        y=b.data
        total=x+y
        c.next=Node(total)
        c=c.next
        a=a.next
        b=b.next
    res=single()
    res.head=d.next
    return res
add(s,s1).traversal()
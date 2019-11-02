class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def push(self, val):
    new_node = Node(val)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
LinkedList.push = push

def __str__(self):
    ret_str = "["
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next
    ret_str = ret_str.rstrip(', ')
    ret_str += "]"
    return ret_str
LinkedList.__str__ = __str__

def pop(self):
   if self.head is None:
       raise Exception("Can't pop No. Val")
   if self.head.next is None:
       val = self.head.val
       self.head = None
       return val
   temp = self.head
   while temp.next is not None:
       prev = temp
       temp = temp.next

   val = temp.val
   prev.next = None
   return val
LinkedList.pop = pop

def insert(self, index, val):
    new_node = Node(val)
    if index == 0:
        new_node.next = self.head
        return
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node
    new_node.next = temp
LinkedList.insert = insert

def remove(self, val):
    temp = self.head
    if temp is not None:
        if temp.val == val:
            self.head = temp.next
            return
    while temp is not None:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp is None:
        return
    prev.next = temp.next
LinkedList.remove = remove

a = LinkedList()

a.push(1)
print(a)
a.push(2)
print(a)
a.push(3)
print(a)
a.push(4)
print(a)
a.pop()
print(a)
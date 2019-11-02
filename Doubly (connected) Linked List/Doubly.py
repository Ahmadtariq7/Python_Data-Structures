class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
        self.prev = None  # change


class Doubly:
    def __init__(self):
        self.head = None


def __str__(self):
    ret_str = "["
    temp = self.head
    while temp is not None:
        # print(hex(id(temp.prev)), hex(id(temp)), hex(id(temp.next))) # for id checking...
        ret_str += str(temp.val) + ', '
        temp = temp.next

    ret_str = ret_str.rstrip(', ')
    ret_str += "]"
    return ret_str


Doubly.__str__ = __str__


def push(self, val):
    new_node = Node(val)
    # Case1: no Node currently
    if self.head is None:
        self.head = new_node
        return
    # Case2: Otherwise, reach end and then insert
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
    new_node.prev = last  # change


Doubly.push = push


def pop(self):
    # if there is no node
    if self.head is None:
        raise Exception("Can't pop No. Val")

    # case 1: only one node
    if self.head.next is None:
        print("Exec: Pop Case 1")
        val = self.head.val
        self.head = None  # Garbage Collection
        return val

    # case2: at least 2 nodes
    # Reach the previous to last node
    print("Exec: Pop Case 2")
    temp = self.head
    while temp.next is not None:
        prev = temp
        temp = temp.next

    val = temp.val
    prev.next = None
    return val


Doubly.pop = pop


def insert(self, index, val):
    new_node = Node(val)
    # insertion at index zero
    if index == 0:
        new_node.next = self.head
        # case 1.2   When list exists
        if self.head is not None:  # change
            self.head.prev = new_node
        self.head = new_node
        return
    # for other indices
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node
    new_node.next = prev  # change

    new_node.next = temp
    temp.prev = new_node  # change


Doubly.insert = insert


def remove(self, val):
    temp = self.head
    # Case1: at first node
    if temp is not None:
        if temp.val == val:
            if temp.next is not None:
                self.head = temp.next
                self.head.prev = None
                return
            self.head = None
            return
    # for other cases
    while temp is not None:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp is None:
        return
    prev.next = temp.next
    if temp.next is not None:
        temp.next.prev = prev


Doubly.remove = remove

d = Doubly()
d.push(1)
print(d)
d.push(2)
print(d)
d.insert(0, 5)
print(d)
d.insert(0, 7)
print(d)
d.remove(1)
print(d)
d.remove(7)
print(d)


# print("None id: ", hex(id(None)))  # 868 ending..

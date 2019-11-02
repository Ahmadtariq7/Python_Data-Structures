class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def push(self, val):
    new_node = Node(val)
    # list is empty
    if self.head is None:
        print("Exec: Push Case 1")
        self.head = new_node
        return
    # otherwise, reach end and add new node
    print("Exec: Push Case 2")
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


LinkedList.pop = pop


def insert(self, index, val):
    new_node = Node(val)
    # insertion at 0 Index
    if index == 0:
        print("Exec: Insert Case 1")
        new_node.next = self.head
        return

    # for other indices
    print("Exec: Insert Case 2")
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node
    new_node.next = temp


LinkedList.insert = insert


def len(self):
    if self.head is None:
        return
    temp = self.head
    counter = 0
    while temp is not None:
        temp = temp.next
        counter += 1
    return counter


LinkedList.len = len


def remove(self, val):
    temp = self.head
    # check first node
    if temp is not None:
        if temp.val == val:
            print("Exec: Remove Case 1")
            self.head = temp.next
            # temp = None
            return
    # let's move to next nodes
    # temp holds value of the node that will be deleted
    while temp is not None:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp is None:  # Not Found
        return
    print("Exec: Remove Case 2")
    prev.next = temp.next  # Just lose the reference to delete the node


LinkedList.remove = remove


def remove_at(self, index):
    if self.head is None:
        return
    temp = self.head
    if index == 0:
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        return
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = temp.next
    temp = None


LinkedList.remove_at = remove_at


def get_last(self):
    if self.head is None:
        return
    if self.head.next is None:
        return
    temp = self.head.next
    while temp.next is not None:
        temp = temp.next
    return temp


LinkedList.get_last = get_last


# #   Reverse List (MY LOGIC)
# def reverse_list(self):
#     temp = self.head
#     prev = None
#     while temp is not None:
#         next = temp.next
#         temp.next = prev
#         prev = temp
#         temp = next
#     self.head = prev
#
#
# LinkedList.reverse_list = reverse_list


def min_val(self):
    # Empty List
    if self.head is None:
        return None
    # List is not empty
    temp = self.head
    minimum = self.head.val
    idx = 0  # index
    counter = 0  # Counter
    while temp is not None:
        if temp.val < minimum:
            minimum = temp.val
            idx = counter
        temp = temp.next
        counter += 1
    return minimum, idx


LinkedList.min_val = min_val


def max_val(self):
    # Empty List
    if self.head is None:
        return None
    # List is not empty
    temp = self.head
    maximum = self.head.val
    idx = 0  # index
    counter = 0  # Counter
    while temp is not None:
        if temp.val > maximum:
            maximum = temp.val
            idx = counter
        temp = temp.next
        counter += 1
    return maximum, idx


LinkedList.max_val = max_val


def remove_min(self):
    if self.head is None:
        return None
    idx = self.min_val()[1]
    self.remove_at(idx)


LinkedList.remove_min = remove_min


def three_highest(self):
    if self.len() < 3:
        return None

    temp = self.head
    h1 = self.head.val
    h2 = self.head.val
    h3 = self.head.val

    while temp is not None:
        if temp.val >= h1:
            h3 = h2
            h2 = h1
            h1 = temp.val
        elif temp.val >= h2:
            h3 = h2
            h2 = temp.val
        elif temp.val >= h3:
            h3 = temp.val
        temp = temp.next
    return h1, h2, h3


LinkedList.three_highest = three_highest


def third_highest(self):
    return self.three_highest()[2]


LinkedList.third_highest = third_highest


def three_lowest(self):
    if self.len() < 3:
        return None

    temp = self.head
    l1 = self.head.val
    l2 = self.head.val
    l3 = self.head.val

    while temp is not None:
        if temp.val <= l1:
            l3 = l2
            l2 = l1
            l1 = temp.val
        elif temp.val <= l2:
            l3 = l2
            l2 = temp.val
        elif temp.val <= l3:
            l3 = temp.val
        temp = temp.next
    return l1, l2, l3


LinkedList.three_lowest = three_lowest


def third_lowest(self):
    return self.three_lowest()[2]


LinkedList.third_lowest = third_lowest


# New Alternative logic of reversing list
def rev_list(self):
    # Empty list or one node check
    if self.head is None:
        return
    if self.head.next is None:
        return

    # at least two nodes
    new_head = self.get_last()
    processing = new_head
    # print(processing)
    for i in range(self.len() - 1):  # loop till (n-1) times
        temp = self.head
        while temp.next != processing:
            temp = temp.next
        processing.next = temp
    self.head.next = None  # this is tail now
    self.head = new_head
    # print(self.head.val)


LinkedList.rev_list = rev_list


def get_counts(self):
    from collections import Counter
    cnt = Counter()
    temp = self.head
    while temp is not None:
        cnt[temp.val] += 1
        temp = temp.next
    return cnt.most_common()  # counter function


LinkedList.get_counts = get_counts


def append_list(self, lst):
    if self.head is None:
        self.head = lst.head

    last = self.get_last()
    last.next = lst.head


LinkedList.append_list = append_list


def some_op(self):
    temp = self.head
    while temp is not None:
        print(temp.val)     # operation performing on all nodes...
        temp = temp.next


LinkedList.some_op = some_op

a = LinkedList()

a.push(33)
print(a)
a.push(44)
print(a)
a.push(11)
print(a)
a.push(33)
print(a)
a.push(80)
print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.insert(1,5)
# print(a)
# a.remove(1)
# print(a)
# a.remove(2)
# print(a)
# print(a.min_val())
# print(a.max_val())
# a.remove_min()
# print(a)
# print(a.len())
# print(a.three_highest())
# print(a.three_lowest())
# print(a.third_highest())
# print(a.third_lowest())
# print(a.get_last())
# print(a.rev_list())
print("::::::::::: MOST COMMON VALUE ::::::::::::: \n")
print(a.get_counts())
print("Most common value with counter", a.get_counts()[0])  # most common value will be at top of list
print("Most common value", a.get_counts()[0][0])
print("::::::::::: LIST APPEND ::::::::::::: \n")
b = LinkedList()
b.push(1)
b.push(3)
b.push(22)
a.append_list(b)
print(a)
print(b)
b.pop()
print(a)  # see 22 got removed coz kia he hum ne.. aise he ho ga, if you don't want like this, you have to make copies..
a.some_op()
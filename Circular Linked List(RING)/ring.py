class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class Ring:
    def __init__(self):
        self.head = None


def __str__(self):
    ret_str = "["
    temp = self.head
    while temp is not None:  # Case1 handled here
        ret_str += str(temp.val) + ", "
        temp = temp.next
        if temp == self.head:  # Different for ring (Change)
            break
    ret_str = ret_str.rstrip(', ')
    ret_str += "]"
    return ret_str


Ring.__str__ = __str__


def _get_last(self):
    # No node, No last
    if self.head is None:
        return None

    # If only one node, it's last too
    if self.head.next == self.head:
        return self.head

    # Atleast two nodes..
    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next
    return temp


Ring._get_last = _get_last


def insert(self, index, val):
    new_node = Node(val)
    last = self._get_last()  # need last for ring (change)
    #   insertion at 0 index
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        # also need to set the last pointer to this new head (change)
        if last is None:
            self.head.next = self.head  # first node ever being inserted
        else:
            last.next = new_node
        return
    if self.head is None and index > 0:
        raise IndexError("Can't insert at index: " + str(index) + "  because list is empty")
    # for other indices
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node
    new_node.next = temp


Ring.insert = insert


def remove(self, val):
    # Empty Ring case
    if self.head is None:
        return
    temp = self.head
    last = self._get_last()
    # First Node matches case (Change)
    if temp.val == val:
        if last == self.head:
            self.head = None  # Just one node, now gone..
        else:
            self.head = temp.next
            last.next = self.head
        return
    #   Let's move to next nodes
    #   Temp holds the value at node that will be deleted
    prev = temp
    temp = temp.next
    while temp != self.head:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp == last.next:  # Not found
        return
    prev.next = temp.next  # Just loose reference to delete the node


Ring.remove = remove


def len(self):
    # No node
    if self.head is None:
        return 0
    # Other cases
    temp = self.head
    counter = 1
    temp = temp.next
    while temp != self.head:
        counter += 1
        temp = temp.next
    return counter


Ring.len = len


def get(self, index):
    # No node
    if self.head is None:
        raise IndexError("List is Empty")
    # Other cases
    temp = self.head
    counter = 0
    while temp is not None:
        if counter == index:
            return temp.val
        temp = temp.next
        counter += 1


Ring.get = get


def push(self, val):
    self.insert(self.len(), val)


Ring.push = push


def remove_at(self, index):
    # No node
    if self.head is None:
        return
    # Only one node and index is zero
    temp = self.head
    last = self._get_last()
    if index == 0:
        if temp.next == self.head:
            self.head = None
            return
        # index zero but list is not empty
        if temp.next != self.head:
            self.head = temp.next
            last.next = self.head
            return
    # for other indices
    counter = 0
    while counter != index:
        if counter == index:
            break
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = temp.next


Ring.remove_at = remove_at


def pop(self):
    self.remove_at(self.len() - 1)


Ring.pop = pop

r = Ring()
r.push(1)
print(r)
r.push(2)
print(r)
r.pop()
print(r)
r.pop()
print(r)

# r.remove_at(1)
# print(r)
# r.remove_at(0)
# print(r)
# r.remove_at(0)
# print(r)
# r.pop()
# print(r)


# print(r._get_last().next == r.head)     # checking it is ring or not...

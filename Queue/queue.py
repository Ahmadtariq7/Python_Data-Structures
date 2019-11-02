class Queue:
    def __init__(self):
        self.size = 5  # Took Member Variable
        self.q = list(range(self.size))  # Some dummy values
        self.i = 0
        self.o = 0

        self.is_empty = True
        self.is_full = False


def _inc(self, val):
    if val + 1 == self.size:
        return 0
    else:
        return val + 1


Queue._inc = _inc


def enqueue(self, val):
    if self.is_full:
        raise IndexError("Queue Full, can't Enqueue")

    self.q[self.i] = val
    self.i = self._inc(self.i)

    if self.i == self.o:
        self.is_full = True
    self.is_empty = False


Queue.enqueue = enqueue


def dequeue(self):
    if self.is_empty:
        raise IndexError("Queue empty, can't Dequeue")

    ret = self.q[self.o]
    self.o = self._inc(self.o)

    if self.i == self.o:
        self.is_empty = True
    self.is_full = False
    return ret


Queue.dequeue = dequeue


def __str__(self):
    return str(self.q) + " , in: " + str(self.i) + " , out: " + str(self.o)


Queue.__str__ = __str__


q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
print(q.dequeue())
print(q)
q.dequeue()
print(q)
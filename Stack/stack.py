s = []

s.append(12)
s.append(5)
s.append(55)

print(s)

print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())  # IndexError

s = []
s.append(1)
s.append(2)
s.append(3)
print(s)
print(s[1])  # It will give value, hence stack rule broken..

# so we use class and object to make stack..

print(":::::::::::::::  IMPLEMENTING STACK WITH CLASSES  ::::::::::::::::::")


class Stack:
    def __init__(self):
        self.l = []

    def push(self, val):
        self.l.append(val)

    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1]


a = Stack()
a.push(1)
a.push(2)
a.push(3)
# print(a)  # returns address which means we can't see list (Stack rule Implemented)
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a[1])     # will get error, coz now a is object not list, and we can't access it via indexing.. stack rule implemented
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
# print(a.peek())  # Nothing to peek (list is empty)


print("::::::::::::STACK CASE STUDY NO 1  (MATCHING BRACKETS)  :::::::::::::::::")


def is_matched(string):
    opening = "({["
    closing = ")}]"
    mapping = dict(zip(opening, closing))
    # print(mapping)
    # return

    stack = []

    for c in string:
        #   Case1 (Neither Opening nor Closing Bracket (digit, word etc)
        if c not in mapping.values() and c not in mapping.keys():
            continue
        #   Case2   Opening bracket
        #   Automatically checks only opening brackets
        if c in mapping:
            stack.append(mapping[c])  # we'll be looking for corresponding closing bracket
        #   Case 3  Has to be closing bracket, if we get here
        elif len(stack) == 0 or c != stack.pop():
            return False
    return len(stack) == 0  # checking stack is empty..? it should be empty


string = "{[[]]{()}}"
print(is_matched(string))
string = "2 + (3 * 5) * ((2 * 2) + 5)"
print(is_matched(string))
string = "2 + (3 * 5) * ((2 * 2) + 5) )"
print(is_matched(string))

print("::::::::::::STACK CASE STUDY NO 2  (Decimal to Binary Conversion)  :::::::::::::::::")


def dec_to_bin(num):
    s1 = []
    while num != 0:
        remainder = num % 2  # Always get 0 or 1
        num = num // 2  # Division by 2
        s1.append(remainder)

    ret = ''
    while s1:
        ret += str(s1.pop())  # Comes out in reverse order of course
    return ret


print(dec_to_bin(8))
print(dec_to_bin(9))
print(dec_to_bin(2))
print(dec_to_bin(0))

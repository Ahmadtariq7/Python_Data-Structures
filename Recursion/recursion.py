def fact(n):
    # Base Case
    if n <= 1:
        return 1
    # Induction Case
    return n * fact(n - 1)


for i in range(1, 7):
    print("Factorial of : ", i, "is: ", fact(i))

print("::::::::::::::  FIB   ::::::::::::::::::::")


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)  # More stuff after recursive call


print(fib(20))  # Order of growth is less


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib(5))


# But this is not Recursive.. so now making this logic recursion

def fib(n, a=0, b=1):
    if n == 0:
        return a
    return fib(n - 1, b, a + b)  # since everything is done in last call, called as tail recursion


# tail recursion is good coz caller skips in mid(cleaning memory)


print(fib(5))

print("::::::::::::::  TOWER OF HANOI   ::::::::::::::::::::")


def tower_of_hanoi(levels=3):
    move_tower(levels, 'A', 'C', 'B')  # Move n-level tower from A to C using B as aux


def move_tower(l, fr, to, ax):
    if l == 1:
        print_move(l, fr, to)
        return
    move_tower(l - 1, fr, ax, to)
    print_move(l, fr, to)
    move_tower(l - 1, ax, fr, to)


def print_move(l, fr, to):
    print("Move: ", l, "from", fr, "to ", to)


print(tower_of_hanoi(2))

print("::::::::::::::  Sum over a list   ::::::::::::::::::::")


def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum


l = [1, 2, 3, 4, 5]

print(sum_list(l))


def sum_list_recursive(l):
    if len(l) == 0: return 0  # Base case

    return l[0] + sum_list_recursive(l[1:])  # Induction case: head + sum of rest


print(sum_list_recursive(l))

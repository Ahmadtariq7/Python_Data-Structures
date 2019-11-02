def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)


def fib2(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print("Fib: ")
for i in range(15):
    print(fib1(i), end=", ")

print('\n\n')
print("Fib2: ")
for i in range(15):
    print(fib2(i), end=', ')

print("\n::::::Computing time for fib::::::::::")

# how to compute time for fib..

import time


def compute_times(fn, limit):
    l = []
    for i in range(limit):
        start_time = int(round(time.time() * 1000))
        fn(i)
        end_time = int(round(time.time() * 1000))
        time_taken = end_time - start_time
        l.append(time_taken)
    return l


limit = 30
fib1_times = compute_times(fib1, limit)
fib2_times = compute_times(fib2, limit)
print(fib1_times)
print(fib2_times)

# showing visual Representation... in plots
import matplotlib.pyplot as plt

plt.figure()
plt.xlabel('fib(n)')
plt.ylabel('time(ms))')
plt.plot(fib1_times)
plt.plot(fib2_times)
plt.show()

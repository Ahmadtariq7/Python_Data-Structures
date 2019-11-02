print(":::::::::: BUBBLE SORT ::::::::")


def bubble_sort(l):
    n = len(l)
    # print(n)

    # Outer loop, Goes over the whole thing 'n' times
    # (Because each time, one 'highest' will have moved to the end)
    for i in range(n):

        # Try to bubble the highest one up
        for j in range(0, (n - i) - 1):
            # Compare pairs, move higher one up ( the highest will always reach the end this way)
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
bubble_sort(l)
print(l)

print(":::::::::: INSERTION SORT ::::::::")


def insertion_sort(l):
    # Go through all elements(except first)
    # Call it key
    # Each time, the key would be 'inserted' in its place
    # At each iteration, stuff less than i would be sorted already

    for i in range(1, len(l)):
        key = l[i]  # Hold the key

        # Start comparing keys to things on its left!
        # Stop when less or equal value found (or we reach left end)
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]  # Move this to right. Slot left on j

            j -= 1
        l[j + 1] = key  # Place key in free slot... (j+1 because we decremented j above)


l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
insertion_sort(l)
print(l)

print(":::::::::: SELECTION SORT ::::::::")


def selection_sort(l):
    n = len(l)
    # For each element in the list(starting from left)
    for i in range(n):
        min_idx = i  # Find the minimum...
        # ... in the *rest* of the list
        for j in range(i + 1, n):
            if l[j] < l[min_idx]:
                min_idx = j

        # Swap the minimum value with the current element, now we have (sorted stuff till i)
        l[i], l[min_idx] = l[min_idx], l[i]


l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
selection_sort(l)
print(l)

print(":::::::::: QUICK SORT ::::::::")
import random


def qsort(l, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = l[random.randint(fst, lst)]
    while i <= j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1
    qsort(l, fst, j)
    qsort(l, i, lst)


l = [1, 2, 4, 1, 2, 5, 5, 6, 1, 110, 15]
qsort(l, 0, len(l) - 1)
print(l)

def max_heapify(lst, n, root):
    """Heapify the root element of lst which has n element in total"""

    largest = root
    l = 2 * root + 1
    r = 2 * root + 2

    if l < n and lst[l] > lst[largest]:
        largest = l
    if r < n and lst[r] > lst[largest]:
        largest = r
    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]
        max_heapify(lst, n, largest)


def min_heapify(lst, n, root):
    smallest = root
    l = 2 * root + 1
    r = 2 * root + 2

    if l < n and lst[l] < lst[smallest]:
        smallest = l
    if r < n and lst[r] < lst[smallest]:
        smallest = r
    if smallest != root:
        lst[root], lst[smallest] = lst[smallest], lst[root]
        min_heapify(lst, n, smallest)


def build_max_heap(lst):
    n = len(lst)
    for i in reversed(range(n // 2)):
        # print("Heapifying: ", lst[i])
        max_heapify(lst, n, i)


def build_min_heap(lst):
    n = len(lst)
    for i in reversed(range(n // 2)):
        # print("Heapifying: ", lst[i])
        min_heapify(lst, n, i)


def heap_sort(lst):
    n = len(lst)
    # Build max Heap
    build_max_heap(lst)
    for i in reversed(range(n)):
        # Swap
        lst[i], lst[0] = lst[0], lst[i]
        # Heapify root element again but only until the ith element
        max_heapify(lst, i, 0)


heap = [100, 5, 3, 2, 8, 15, 6, 102]
print(heap)
build_max_heap(heap)
print(":::::::::: AFTER  MAX HEAP ::::::::")
print(heap)
print(":::::::::: AFTER  MIN HEAP ::::::::")
build_min_heap(heap)
print(heap)
print(":::::::::: AFTER HEAP SORT ::::::::")
heap_sort(heap)
print(heap)
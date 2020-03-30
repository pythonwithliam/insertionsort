# Insertion Sort Python 3.x implementation
# Complexity O(n^2)

# Insertion sort is a simple sorting algorithm that builds the final sorted
# array (or list) one item at a time. It is much less efficient on large lists
# than more advanced algorithms such as quicksort, heapsort, or merge sort.
# However, insertion sort provides several advantages:
# * Efficient for (quite) small data sets, much like other quadratic sorting
#       algorithms
# * Does not change the relative order of elements with equal keys
# * Only requires a constant amount O(1) of additional memory space
# * Can sort a list as it receives it
#


def iterative_insertion_sort(arr):
    # We start at the second element since the first is by default already
    # sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

    return arr


def recursive_insertion_sort(arr, index):
    # default case
    if index <=1:
        return arr

    # sort the first n-1 elements recursively
    recursive_insertion_sort(arr, index - 1)
    last = arr[index-1]
    i = index-2

    # move elements that are greater than the key one position right
    while i >= 0 and arr[i] > last:
        arr[i+1] = arr[i]
        i = i-1

    # insert last element in its sorted position
    arr[i+1] = last

    return arr


def binary_insertion_sort(arr):
    # Finds the proper location to insert an array value
    # Slightly more efficient since Binary Search runtime is O(log n)

    for i in range(1, len(arr)):
        # set the key value, floor index, and ceiling index
        key = arr[i]
        floor = 0
        ceiling = i

        # Move the indices closer to each other
        while ceiling > floor:
            mid = (floor + ceiling) // 2
            if arr[mid] < key:
                floor = mid + 1
            else:
                ceiling = mid
        arr[:] = arr[:floor] + [key] + arr[ceiling:i] + arr[i + 1:]

    return arr

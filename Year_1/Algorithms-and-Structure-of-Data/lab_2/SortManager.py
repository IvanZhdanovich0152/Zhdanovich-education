import time

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def quick_sort_stat(data):
    array = data.copy()
    start_time = time.time()
    stats = {"comparisons": 0, "swaps": 0}

    def partition(low, high):
        pivot = array[(low + high) // 2]
        i = low - 1
        j = high + 1

        while True:
            stats["comparisons"] += 1
            while True:
                i += 1
                if array[i] >= pivot:
                    break

            while True:
                j -= 1
                if array[j] <= pivot:
                    break

            if i >= j:
                return j

            swap(array, i, j)
            stats["swaps"] += 1

    def quick_sort(low, high):
        if low < high:
            p = partition(low, high)

            quick_sort(low, p)
            quick_sort(p + 1, high)

    quick_sort(0, len(array) - 1)

    time_taken = time.time() - start_time
    return array, stats["comparisons"], stats["swaps"], time_taken

def insertion_sort(data):
    arr = data.copy()
    stats = {"comparisons": 0, "swaps": 0}
    start_time = time.time()

    for i in range(1, len(arr)):
        index = i
        stats["comparisons"] += 1
        while index > 0 and arr[index - 1] > arr[index]:
            swap(arr, index, index - 1)
            index -= 1
            stats["swaps"] += 1

    time_taken = time.time() - start_time
    return arr, stats["comparisons"], stats["swaps"], time_taken

def selection_sort(data):
    arr = data.copy()
    stats = {"comparisons": 0, "swaps": 0}
    start_time = time.time()

    n = len(arr)

    for i in range(0, n):
        min_value = arr[i]
        min_index = i

        for j in range(i, n):

            if arr[j] < min_value:
                stats["comparisons"] += 1
                min_value = arr[j]
                min_index = j

        if min_index != i:
            swap(arr, i, min_index)
            stats["swaps"] += 1
    time_taken = time.time() - start_time
    return arr, stats["comparisons"], stats["swaps"], time_taken

def cocktail_sort(data):
    arr = data.copy()
    stats = {"comparisons": 0, "swaps": 0}
    time_start = time.time()
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            stats["comparisons"] += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                stats["swaps"] += 1
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            stats["comparisons"] += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                stats["swaps"] += 1
                swapped = True

        start += 1

    time_taken = time.time() - time_start
    return arr, stats["comparisons"], stats["swaps"], time_taken

def heap_sort(data):
    arr = data.copy()
    stats = {"comparisons": 0, "swaps": 0}
    start_time = time.time()
    n = len(arr)

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            stats["comparisons"] += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            stats["comparisons"] += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            swap(arr, largest, i)
            stats["swaps"] += 1
            heapify(arr, n, largest)


    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        swap(arr, i, 0)
        stats["swaps"] += 1
        heapify(arr, i, 0)

    time_taken = time.time() - start_time
    return arr, stats["comparisons"], stats["swaps"], time_taken









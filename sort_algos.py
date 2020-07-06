def bubble_sort(array):
    for _ in array:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


def selection_sort(array):
    for i in range(len(array) - 1):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j


def insertion_sort(array):
    for i in range(1, len(array)):
        while array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]


def merge_sort(array):
    if len(array) < 2:
        return array

    half = len(array) // 2
    left = array[:half]
    right = array[half:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        elif right[j] < left[i]:
            array[k] = right[j]
            j += 1
            k += 1
        else:
            array[k] = left[i]
            i += 1
            k += 1
            array[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def quick_sort(array):
    if len(array) < 2:
        return array

    piv = len(array) - 1
    i = 0
    while len(array) > i != piv >= 0:
        if array[i] > array[piv]:
            array.append(array[i])
            array.remove(array[i])
            piv -= 1
            i -= 1
        i += 1

    l, r = array[:piv], array[piv:]

    quick_sort(l)
    quick_sort(r)

    array[:piv], array[piv:] = l, r


def radix_sort(array):
    max_len = 1
    for i in array:
        if len(str(i)) > max_len:
            max_len = len(str(i))

    dig = -1
    for _ in range(max_len):
        buckets = [[] for _ in range(10)]
        for num in array:
            num = str(num)
            try:
                char = num[dig]
                buckets[int(char)].append(int(num))
            except IndexError:
                buckets[0].append(int(num))

        array = []
        for bucket in buckets:
            array += bucket
        dig -= 1

# Selection Sort Algorithm

def SelectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        (arr[i], arr[min]) = (arr[min], arr[i])

# Bubble Sort Algorithm


def BubbleSort(arr):
    isSwapped = False
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                isSwapped = True
        if (not (isSwapped)):
            break

# Insertion Sort Algorithm


def InsertionSort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while (curr < arr[j] and j >= 0):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr

# Merge Sort Algorithm


def Merge(arr, l, mid, h):
    temp = [0] * len(arr)
    i = l
    k = l
    j = mid + 1
    while (i <= mid and j <= h):
        if (arr[i] < arr[j]):
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while (i <= mid):
        temp[k] = arr[i]
        i += 1
        k += 1
    while (j <= h):
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(l, h + 1):
        arr[i] = temp[i]


def MergeSort(arr, l, h):
    if (l < h):
        mid = (l + h)//2
        MergeSort(arr, l, mid)
        MergeSort(arr, mid + 1, h)
        Merge(arr, l, mid, h)

# Quick Sort Algorithm


def Partition(arr, l, h):
    pivot = arr[h]
    pIndex = l
    for i in range(l, h):
        if (arr[i] < pivot):
            (arr[i], arr[pIndex]) = (arr[pIndex], arr[i])
            pIndex += 1
    (arr[h], arr[pIndex]) = (arr[pIndex], arr[h])
    return pIndex


def QuickSort(arr, l, h):
    if (l < h):
        p = Partition(arr, l, h)
        QuickSort(arr, l, p - 1)
        QuickSort(arr, p + 1, h)

# Counting Sort Algorithm


def CountingSort(input_arr, r):
    output_arr = [0] * len(input_arr)
    count_arr = [0] * r
    for i in range(len(input_arr)):
        count_arr[input_arr[i]] += 1
    for i in range(1, r):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(input_arr)):
        output_arr[count_arr[input_arr[i]] - 1] = input_arr[i]
    for i in range(len(input_arr)):
        input_arr[i] = output_arr[i]

# Radix Sort Algorithm


def CountSort(arr, div):
    output_arr = [0] * len(arr)
    count_arr = [0] * 10

    for i in range(size):
        count_arr[int(arr[i]/div) % 10] += 1
    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]
    for i in reversed(range(size)):
        output_arr[count_arr[int(arr[i]/div) % 10] - 1] = arr[i]
        count_arr[int(arr[i]/div) % 10] -= 1
    for i in range(size):
        arr[i] = output_arr[i]


def RadixSort(arr):
    m = max(arr)
    div = 1
    while (int(m/div) > 0):
        div *= 10
        CountSort(arr, div)


arr = []
size = int(input("Enter the size of the Array: "))
print("Enter the elements of the array")
for i in range(0, size):
    elt = int(input())
    arr.append(elt)
print("Array Before Sorting...")
print(arr)
# Function calls
RadixSort(arr)
print("Array After Sorting...")
print(arr)

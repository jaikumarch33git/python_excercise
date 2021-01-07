# Quick Sort Algorithm

data = [10, 80, 30, 90, 40, 50, 70]


def quick_sort(arr, low=None, high=None):
    if len(arr) < 1:
        return data

    low = 0 - 1
    high = len(arr)
    pivot = arr[-1]

    for i in range(high - 1):
        if arr[i] < pivot:
            low += 1
            arr[i], arr[low] = arr[low], arr[i]

    return data


#Selection Sort
# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.

arr = [10, 80, 30, 90, 40, 50, 70]

for i in range(len(arr)):

    smallest_index = i
    for j in range(i,len(arr)):
        if arr[smallest_index]>arr[j]:
            smallest_index = j

    arr[i],arr[smallest_index]=arr[smallest_index],arr[i]

# Insertion Sort
# This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted.
# For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in
# this sorted sub-list, has to find its appropriate place and then it has to be inserted there.
# Hence the name, insertion sort.

# The array is searched sequentially and unsorted items are moved and inserted into the sorted
# sub-list (in the same array).
# This algorithm is not suitable for large data sets as its average and
# worst case complexity are of Ο(n2), where n is the number of items.

arr = [10, 80, 30, 90, 40, 50, 70]
array_length = len(arr)
count=0
for i in range(array_length):
    key = arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
        arr[j+1] =arr[j]
        j-=1
    arr[j+1] =key


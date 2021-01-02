# Bubble Sort
# Bubble sort is a simple sorting algorithm.
# This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and
# the elements are swapped if they are not in order.
# This algorithm is not suitable for large data sets as its average and
# worst case complexity are of Ο(n2) where n is the number of items.

arr = [10, 80, 30, 90, 40, 50, 70]
array_length = len(arr)

# Bubble sort with for loop
for i in range(array_length):
    swapped=False
    for j in range(0,array_length-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if swapped==False:
        break


# Bubble sort with while loop
# with while loop we will have the time complexity of Ο(n2)
i = 0
while i < array_length:
    j=0
    while j < array_length-1:
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]= arr[j+1],arr[j]
        j +=1
    i+=1
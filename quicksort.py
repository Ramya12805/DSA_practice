def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


arr = [5, 2, 8, 3, 1, 7, 6, 4]
sorted_arr = quick_sort(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

def exponential_binary_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1  # Element not found in an empty array

    index = 1  # Start from 1 for effective doubling
    while index < n and arr[index - 1] <= target:
        index *= 2 

    # Perform a binary search in the range [index / 2, min(index, n)]
    left, right = index // 2, min(index, n) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target_element = 12
result = exponential_binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")

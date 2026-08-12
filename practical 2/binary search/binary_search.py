# Time Complexity: Best: O(1), Average: O(log n), Worst: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(binary_search(arr, target))

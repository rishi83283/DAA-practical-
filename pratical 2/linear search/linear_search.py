# Time Complexity: Best: O(1), Average: O(n), Worst: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(linear_search(arr, target))

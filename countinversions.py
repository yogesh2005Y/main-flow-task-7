def merge_sort(arr):
    if len(arr) < 2:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_count = merge(left, right)
    return merged, inv_left + inv_right + inv_count

def merge(left, right):
    result = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv_count += len(left) - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, inv_count

# Example
arr = [2, 4, 1, 3, 5]
_, inversions = merge_sort(arr)
print("Inversions:", inversions)

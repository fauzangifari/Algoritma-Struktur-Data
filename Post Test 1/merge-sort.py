#merge short
import random

def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        middle = len(list) // 2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", list)
print("Sorted list: ", merge_sort(list))

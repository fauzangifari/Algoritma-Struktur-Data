import random

def shell_sort(list):
    sublistcount = len(list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    return list

def gap_insertion_sort(list, start, gap):
    for i in range(start + gap, len(list), gap):
        currentvalue = list[i]
        position = i
        while position >= gap and list[position - gap] > currentvalue:
            list[position] = list[position - gap]
            position = position - gap
        list[position] = currentvalue

list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", list)
print("Sorted list: ", shell_sort(list))

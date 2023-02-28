import random

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = random.choice(list)
        less = [i for i in list if i < pivot]
        greater = [i for i in list if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", list)
print("Sorted list: ", quick_sort(list))

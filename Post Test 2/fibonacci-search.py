def fibonacci_search(arr, item):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    index = -1
    while fib > 1:
        i = min(index + fib2, (len(arr) - 1))
        for j in range(len(arr[i])):
            if arr[i][j] == item:
                return i
        if arr[i] < item:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            index = i
        elif arr[i] > item:
            fib = fib2

            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and index < (len(arr) - 1) and arr[index + 1] == item:
        return index+1
    return -1

def main():
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
    item = str.capitalize(input("Masukkan nama yang ingin dicari: "))

    if fibonacci_search(arr, item) == -1:
        print("Nama tidak ada di dalam arr.")

    elif fibonacci_search(arr[fibonacci_search(arr, item)], item) == -1:
        print("Nama ditemukan pada indeks", fibonacci_search(arr, item))

    else:
        print("Nama ditemukan pada indeks", fibonacci_search(arr, item), "dengan kolom", fibonacci_search(arr[fibonacci_search(arr, item)], item))

main()
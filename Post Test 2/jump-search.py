def jump_search(arr, item):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    for i in range(len(arr)):
        if type(arr[i]) == list:
            for j in range(len(arr[i])):
                if arr[i][j] == item:
                    return i, j
    while arr[min(step, n) - 1] < item:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev] < item:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == item:
        return prev
    return -1

def main():
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
    item = str.capitalize(input("Masukkan nama yang ingin dicari: "))

    result = jump_search(arr, item)
    if result == -1:
        print("Nama tidak ada di dalam list.")
    else:
        if result[1] == -1: # elemen ditemukan pada indeks, tetapi bukan di dalam sublist
            print(f"Nama ditemukan pada indeks {result[0]}.")
        else: # elemen ditemukan pada sublist
            print(f"Nama ditemukan pada indeks {result[0]}, dengan kolom {result[1]}")

main()
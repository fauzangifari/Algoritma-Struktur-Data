def fibonacci_search(arr, item):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    index = -1
    while fib > 1: # perulangan akan berhenti jika fib bernilai 1
        i = min(index + fib2, (len(arr) - 1)) # cari indeks yang akan dibandingkan
        for j in range(len(arr[i])): # lakukan pencarian secara linear
            if arr[i][j] == item: # jika elemen ditemukan
                return i # kembalikan indeks list dan indeks elemen
        if arr[i] < item: # jika elemen di indeks tengah lebih kecil dari elemen yang dicari
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            index = i
        elif arr[i] > item: # jika elemen di indeks tengah lebih besar dari elemen yang dicari
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else: # jika elemen di indeks tengah sama dengan elemen yang dicari
            return i # kembalikan indeks list dan -1
    if fib1 and index < (len(arr) - 1) and arr[index + 1] == item: # jika elemen di indeks tengah sama dengan elemen yang dicari
        return index+1 # kembalikan indeks list dan -1
    return -1 # kembalikan -1

def main():
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]] # list yang akan dicari
    item = str.capitalize(input("Masukkan nama yang ingin dicari: ")) # elemen yang dicari

    if fibonacci_search(arr, item) == -1: # jika elemen tidak ditemukan
        print("Nama tidak ada di dalam arr.")

    elif fibonacci_search(arr[fibonacci_search(arr, item)], item) == -1: # jika elemen ditemukan
        print("Nama ditemukan pada indeks", fibonacci_search(arr, item))

    else: # jika elemen ditemukan dan berada di dalam list yang ada di dalam list
        print("Nama ditemukan pada indeks", fibonacci_search(arr, item), "dengan kolom", fibonacci_search(arr[fibonacci_search(arr, item)], item))

main()
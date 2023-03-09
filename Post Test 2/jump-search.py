def jump_search(arr, item):
    n = len(arr) # berapa banyak elemen di dalam list
    step = int(n ** 0.5) # berapa banyak elemen yang akan dilewati
    prev = 0 # indeks awal
    for i in range(len(arr)): # lakukan pencarian secara linear
        if type(arr[i]) == list: # jika elemen berupa list
            for j in range(len(arr[i])): # lakukan pencarian secara linear
                if arr[i][j] == item: # jika elemen ditemukan
                    return i, j # kembalikan indeks list dan indeks elemen
        else:
            if arr[i] == item:
                return i
    while arr[min(step, n) - 1] < item: # jika elemen di indeks tengah lebih kecil dari elemen yang dicari
        prev = step # indeks awal akan diubah menjadi indeks tengah
        step += int(n ** 0.5) # indeks tengah akan diubah menjadi indeks awal + indeks tengah
        if prev >= n: # jika indeks awal lebih besar dari panjang list
            return -1 # kembalikan -1
    while arr[prev] < item: # jika elemen di indeks tengah lebih besar dari elemen yang dicari
        prev += 1 # indeks awal akan diubah menjadi indeks awal + 1
        if prev == min(step, n): # jika indeks awal sama dengan indeks tengah
            return -1 # kembalikan -1
    if arr[prev] == item: # jika elemen di indeks tengah sama dengan elemen yang dicari
        return prev # kembalikan indeks list dan -1
    return -1 # kembalikan -1

def main():
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]] # list yang akan dicari
    item = str.capitalize(input("Masukkan nama yang ingin dicari: ")) # elemen yang dicari

    result = jump_search(arr, item) # simpan hasil pencarian

    if result == -1: # jika elemen tidak ditemukan
        print("Nama tidak ada di dalam arr")

    elif type(result) == int: # jika elemen ditemukan
        if type(arr[result]) == list: # jika elemen berupa list
            print("Nama ditemukan pada indeks", result)
        else: # jika elemen tidak berupa list
            print("Nama ditemukan pada indeks", result)

    else: # jika elemen ditemukan dan berada di dalam list yang ada di dalam list
        print("Nama ditemukan pada indeks", result[0], "dengan kolom", result[1])

main()

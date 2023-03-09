def binary_search(arr, left, right, x):
    if right >= left: # jika indeks kiri lebih kecil dari indeks kanan
        mid = (left + right) // 2 # cari indeks tengah

        if type(arr[mid]) == list: # jika elemen di indeks tengah adalah list
            for j in range(len(arr[mid])): # lakukan pencarian secara linear
                if arr[mid][j] == x: # jika elemen ditemukan
                    return (mid, j) # kembalikan indeks list dan indeks elemen
            if arr[mid][0] > x: # jika elemen di indeks tengah lebih besar dari elemen yang dicari
                return binary_search(arr, left, mid - 1, x) # lakukan pencarian di bagian kiri
            return binary_search(arr, mid + 1, right, x) # lakukan pencarian di bagian kanan
        elif arr[mid] == x: # jika elemen di indeks tengah sama dengan elemen yang dicari
            return (mid, -1) # kembalikan indeks list dan -1
        elif arr[mid] > x: # jika elemen di indeks tengah lebih besar dari elemen yang dicari
            return binary_search(arr, left, mid - 1, x) # lakukan pencarian di bagian kiri
        else: # jika elemen di indeks tengah lebih kecil dari elemen yang dicari
            return binary_search(arr, mid + 1, right, x) # lakukan pencarian di bagian kanan
    else: # jika indeks kiri lebih besar dari indeks kanan
        return -1 # kembalikan -1

def main():
    arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]] # list yang akan dicari
    x = str.capitalize(input("Masukkan nama yang ingin dicari: ")) # elemen yang dicari

    result = binary_search(arr, 0, len(arr) - 1, x) # panggil fungsi binary_search
    if result == -1: # jika elemen tidak ditemukan
        print("Nama tidak ada di dalam list.")
    else: # jika elemen ditemukan
        if result[1] == -1: # jika elemen ditemukan dan tidak berada di dalam list yang ada di dalam list
            print(f"Nama ditemukan pada indeks {result[0]}.")
        else: # jika elemen ditemukan dan berada di dalam list yang ada di dalam list
            print(f"Nama ditemukan pada indeks {result[0]}, kolom {result[1]}")

main()

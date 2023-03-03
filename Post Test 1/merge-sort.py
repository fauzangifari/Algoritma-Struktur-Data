import random # module untuk menghasilkan bilangan acak
import matplotlib.pyplot as plt # module untuk membuat grafik

def merge_sort(list):
    if len(list) <= 1: # jika panjang list <= 1, maka list tersebut sudah terurut
        return list # kembalikan list tersebut
    else: # jika panjang list > 1, maka lakukan pengurutan
        middle = len(list) // 2 # cari nilai tengah dari list
        left = merge_sort(list[:middle]) # lakukan pengurutan terhadap bagian kiri list
        right = merge_sort(list[middle:]) # lakukan pengurutan terhadap bagian kanan list
        return merge(left, right) # gabungkan bagian kiri dan kanan list

def merge(left, right):
    merged = [] # list untuk menyimpan hasil penggabungan
    left_index = 0 # indeks untuk bagian kiri list
    right_index = 0 # indeks untuk bagian kanan list
    while left_index < len(left) and right_index < len(right): # lakukan penggabungan sampai salah satu list habis
        if left[left_index] < right[right_index]: # jika elemen bagian kiri lebih kecil dari elemen bagian kanan
            merged.append(left[left_index]) # tambahkan elemen bagian kiri ke list hasil penggabungan
            left_index += 1 # naikkan indeks bagian kiri
        else:
            merged.append(right[right_index]) # tambahkan elemen bagian kanan ke list hasil penggabungan
            right_index += 1 # naikkan indeks bagian kanan
    merged += left[left_index:] # jika salah satu list habis, tambahkan sisa list yang belum habis ke list hasil penggabungan
    merged += right[right_index:] # jika salah satu list habis, tambahkan sisa list yang belum habis ke list hasil penggabungan
    return merged # kembalikan list hasil penggabungan

def main():
    list = [random.randint(0, 100) for i in range(10)] # buat list dengan 10 elemen yang nilainya acak antara 0 dan 100
    print("Unsorted list: ", list) # menampilkan list sebelum diurutkan
    print("Sorted list: ", merge_sort(list)) # menampilkan list setelah diurutkan

    plt.bar(range(len(list)), list, color="red") # buat grafik batang untuk list sebelum diurutkan
    plt.title("Unsorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

    plt.bar(range(len(list)), merge_sort(list), color="green") # buat grafik batang untuk list setelah diurutkan
    plt.title("Sorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

main()

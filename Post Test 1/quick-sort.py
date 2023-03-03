import random # module untuk menghasilkan bilangan acak
import matplotlib.pyplot as plt # module untuk membuat grafik

def quick_sort(list):
    if len(list) <= 1: # jika panjang list <= 1, maka list tersebut sudah terurut
        return list # kembalikan list tersebut
    else: # jika panjang list > 1, maka lakukan pengurutan
        pivot = random.choice(list) # cari nilai tengah dari list
        less = [i for i in list if i < pivot] # lakukan pengurutan terhadap bagian kiri list
        greater = [i for i in list if i > pivot] # lakukan pengurutan terhadap bagian kanan list
        return quick_sort(less) + [pivot] + quick_sort(greater) # gabungkan bagian kiri dan kanan list

def main():
    list = [random.randint(0, 100) for i in range(10)] # buat list dengan 10 elemen yang nilainya acak antara 0 dan 100
    print("Unsorted list: ", list) # menampilkan list sebelum diurutkan
    print("Sorted list: ", quick_sort(list)) # menampilkan list setelah diurutkan

    plt.bar(range(len(list)), list, color="red") # buat grafik batang untuk list sebelum diurutkan
    plt.title("Unsorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

    plt.bar(range(len(list)), quick_sort(list), color="green") # buat grafik batang untuk list setelah diurutkan
    plt.title("Sorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

main()

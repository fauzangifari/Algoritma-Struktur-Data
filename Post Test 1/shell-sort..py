import random # module untuk menghasilkan bilangan acak
import matplotlib.pyplot as plt # module untuk membuat grafik

def shell_sort(list):
    sublistcount = len(list) // 2 # cari nilai tengah dari list
    while sublistcount > 0: # melakukan perulangan selama sublistcount > 0
        for startposition in range(sublistcount): # iterasi untuk setiap elemen di list
            gap_insertion_sort(list, startposition, sublistcount)  # lalu memasukkan elemen kedalam fungsi gap_insertion_sort
        sublistcount = sublistcount // 2 # lalu floor division sublistcount dengan 2
    return list # kembalikan list tersebut

def gap_insertion_sort(list, start, gap):
    for i in range(start + gap, len(list), gap): # iterasi untuk setiap elemen di list
        currentvalue = list[i]
        position = i #
        while position >= gap and list[position - gap] > currentvalue: # melakukan perulangan selama position >= gap dan list[position - gap] > currentvalue
            list[position] = list[position - gap]
            position = position - gap

def main():
    list = [random.randint(0, 100) for i in range(10)] # buat list dengan 10 elemen yang nilainya acak antara 0 dan 100

    plt.bar(range(len(list)), list, color="red") # buat grafik batang untuk list sebelum diurutkan
    plt.title("Unsorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

    print("Unsorted list: ", list) # menampilkan list sebelum diurutkan

    plt.bar(range(len(list)), shell_sort(list), color="green") # buat grafik batang untuk list setelah diurutkan
    plt.title("Sorted list") # judul grafik
    plt.xlabel("Index") # label sumbu x
    plt.ylabel("Value") # label sumbu y
    plt.show() # tampilkan grafik

    print("Sorted list: ", shell_sort(list)) # menampilkan list setelah diurutkan

main()

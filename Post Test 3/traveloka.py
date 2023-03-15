import os
from prettytable import PrettyTable

os.system('cls')


class Flight:
    def __init__(self, airline, origin, destination, departureTime, arrivalTime, price, nextFlight=None):
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.price = price
        self.nextFlight = nextFlight

    def __str__(self):
        return f"{self.airline} {self.origin} {self.destination} {self.departureTime} {self.arrivalTime} {self.price}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def addFlight(self, airline, origin, destination, departureTime, arrivalTime, price):
        if self.head == None:
            self.head = Flight(airline, origin, destination, departureTime, arrivalTime, price)
            self.tail = self.head
            self.history.append('Add')
        else:
            self.tail.nextFlight = Flight(airline, origin, destination, departureTime, arrivalTime, price)
            self.tail = self.tail.nextFlight
        self.history.append(('Add', (airline, origin, destination, departureTime, arrivalTime, price)))

    def printFlight(self):
        temp = self.head

        t = PrettyTable(['No.', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Harga'])
        number = 1
        while temp != None:
            t.title = 'Daftar Tiket Pesawat'
            t.add_row(
                [number, temp.airline, temp.origin, temp.destination, temp.departureTime, temp.arrivalTime, temp.price])
            number += 1
            temp = temp.nextFlight
        print(t)

    def deleteFlight(self, number):
        temp = self.head
        prev = None
        count = 1
        while temp and count != number:
            prev = temp
            temp = temp.nextFlight
            count += 1

        if temp is None:
            return

        if prev is None:
            self.head = temp.nextFlight
        else:
            prev.nextFlight = temp.nextFlight
        self.history.append(
            ('Delete', (temp.airline, temp.origin, temp.destination, temp.departureTime, temp.arrivalTime, temp.price)))

    def paginate(self, page, size):
        temp = self.head
        t = PrettyTable(['No.', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Harga'])
        number = (page - 1) * size + 1
        t.title = f'Halaman {page}'
        count = 0
        while temp != None:
            if count >= (page - 1) * size and count < page * size:
                t.add_row([number, temp.airline, temp.origin, temp.destination, temp.departureTime, temp.arrivalTime,
                           temp.price])
                number += 1
            count += 1
            temp = temp.nextFlight
        print(t)

    def historyAddDelete(self):
        t = PrettyTable(
            ['No.', 'Action', 'Pesawat', 'Asal', 'Tujuan', 'Waktu Keberangkatan', 'Waktu Kedatangan', 'Harga'])
        number = 1
        for i in self.history:
            t.title = 'Riwayat Add/Delete'
            if i[0] == 'Add':
                t.add_row([number, i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]])
            elif i[0] == 'Delete':
                t.add_row([number, i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]])
            number += 1
        print(t)


def main():
    flight = LinkedList()

    flight.addFlight('Garuda Indonesia', 'Jakarta', 'Bali/Denpasar', '05:00', '06:50', 1200000)
    flight.addFlight('Lion Air', 'Surabaya', 'Balikpapan', '07:00', '08:35', 900000)
    flight.addFlight('Citilink', 'Balikpapan', 'Yogyakarta', '16:00', '18:00', 1000000)
    flight.addFlight('Air Asia', 'Jakarta', 'Medan', '16:45', '19:00', 1200000)
    flight.addFlight('Garuda Indonesia', 'Bali/Denpasar', 'Makassar', '20:50', '22:15', 1300000)
    flight.addFlight('Batik Air', 'Surabaya', 'Singapore', '08:45', '12:00', 3230000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '04:00', '06:00', 500000)
    flight.addFlight('Super Air Jet', 'Batam', 'Bali/Denpasar', '07:00', '15:30', 1720000)
    flight.addFlight('Batik Air', 'Samarinda', 'Jakarta', '08:50', '10:00', 1500000)
    flight.addFlight('Citilink', 'Jakarta', 'Malang', '12:25', '13:55', 1350000)
    flight.addFlight('Lion Air', 'Medan', 'Surabaya', '05:35', '11:05', 1440000)

    while True:
        os.system('cls')
        choice = int(input('''
            ========================================
            |          M E N U   P I L I H         |
            ========================================
            |   > 1. Tambah Tiket Pesawat          |
            |   > 2. Hapus Tiket Pesawat           |
            |   > 3. Halaman Tiket Pesawat         |
            |   > 4. Riwayat Add/Delete            |
            |   > 5. Exit                          |
            ========================================
            Pilih nomor : '''))

        if choice == 1:
            airline = str(input('Nama Pesawat : '))
            origin = str(input('Asal : '))
            destination = str(input('Tujuan : '))
            departureTime = str(input('Waktu Keberangkatan : '))
            arrivalTime = str(input('Waktu Kedatangan : '))
            price = int(input('Harga : '))
            flight.addFlight(airline, origin, destination, departureTime, arrivalTime, price)

        elif choice == 2:
            flight.printFlight()
            number = int(input('Nomor : '))
            flight.deleteFlight(number)

        elif choice == 3:
            flight.paginate(1, 5)
            yn = str(input('Lanjut ke halaman selanjutnya? (y/n) : '))
            while yn == 'y':
                page = int(input('Halaman : '))
                flight.paginate(page, 5)
                yn = str(input('Lanjut ke halaman selanjutnya? (y/n) : '))
            else:
                continue

        elif choice == 4:
            flight.historyAddDelete()

        elif choice == 5:
            break

        else:
            print('Pilihan tidak tersedia')


main()

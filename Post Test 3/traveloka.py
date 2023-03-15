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

    def addFlight(self, airline, origin, destination, departureTime, arrivalTime, price):
        if self.head == None:
            self.head = Flight(airline, origin, destination, departureTime, arrivalTime, price)
            self.tail = self.head
        else:
            self.tail.nextFlight = Flight(airline, origin, destination, departureTime, arrivalTime, price)
            self.tail = self.tail.nextFlight

    def printFlight(self):
        temp = self.head
        t = PrettyTable(['Airline', 'Origin', 'Destination', 'Departure Time', 'Arrival Time', 'Price'])
        while temp != None:
            t.add_row([temp.airline, temp.origin, temp.destination, temp.departureTime, temp.arrivalTime, temp.price])
            temp = temp.nextFlight
        print(t)

    def searchFlight(self, airline, origin, destination, departureTime, arrivalTime, price):
        temp = self.head
        while temp != None:
            if temp.airline == airline and temp.origin == origin and temp.destination == destination and temp.departureTime == departureTime and temp.arrivalTime == arrivalTime and temp.price == price:
                return True
            temp = temp.nextFlight
        return False

    def deleteFlight(self, airline, origin, destination, departureTime, arrivalTime, price):
        if self == None:
            return
        if self.head.airline == airline and self.head.origin == origin and self.head.destination == destination and self.head.departureTime == departureTime and self.head.arrivalTime == arrivalTime and self.head.price == price:
            self.head = self.head.nextFlight
            return
        temp = self.head
        while temp != None:
            if temp.nextFlight.airline == airline and temp.nextFlight.origin == origin and temp.nextFlight.destination == destination and temp.nextFlight.departureTime == departureTime and temp.nextFlight.arrivalTime == arrivalTime and temp.nextFlight.price == price:
                temp.nextFlight = temp.nextFlight.nextFlight
                return
            temp = temp.nextFlight

    def paginate(self, page, size):
        temp = self.head
        t = PrettyTable(['Airline', 'Origin', 'Destination', 'Departure Time', 'Arrival Time', 'Price'])
        count = 0
        while temp != None:
            if count >= (page-1)*size and count < page*size:
                t.add_row([temp.airline, temp.origin, temp.destination, temp.departureTime, temp.arrivalTime, temp.price])
            count += 1
            temp = temp.nextFlight
        print(t)

    def printHistory(self):
        pass


def main():
    flight = LinkedList()

    flight.addFlight('Garuda Indonesia', 'Jakarta', 'Bali', '05:00', '06:50', 1200000)
    flight.addFlight('Lion Air', 'Surabaya', 'Balikpapan', '07:00', '08:35', 900000)
    flight.addFlight('Citilink', 'Balikpapan', 'Yogyakarta', '16:00', '18:00', 1000000)
    flight.addFlight('Air Asia', 'Jakarta', 'Medan', '16:45', '19:00', 1200000)
    flight.addFlight('Garuda Indonesia', 'Bali', 'Makassar', '20:50', '22:15', 1300000)
    flight.addFlight('Batik Air', 'Surabaya', 'Singapore', '08:45', '12:00', 3230000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '04:00', '06:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '07:00', '09:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '10:00', '12:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '13:00', '15:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '16:00', '18:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '19:00', '21:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '22:00', '00:00', 500000)
    flight.addFlight('Lion Air', 'Jakarta', 'Surabaya', '01:00', '03:00', 500000)

    while True:
        os.system('cls')
        print('''
                1. Add Flight
                2. Delete Flight
                3. Print Flight
                4. Paginate Flight
                5. History add/delete
                6. Exit
                ''')
        choice = int(input('Choice : '))

        if choice == 1:
            airline = input('Airline : ')
            origin = input('Origin : ')
            destination = input('Destination : ')
            departureTime = input('Departure Time : ')
            arrivalTime = input('Arrival Time : ')
            price = int(input('Price : '))
            flight.addFlight(airline, origin, destination, departureTime, arrivalTime, price)
        elif choice == 2:
            airline = input('Airline : ')
            origin = input('Origin : ')
            destination = input('Destination : ')
            departureTime = input('Departure Time : ')
            arrivalTime = input('Arrival Time : ')
            price = int(input('Price : '))
            flight.deleteFlight(airline, origin, destination, departureTime, arrivalTime, price)
        elif choice == 3:
            flight.printFlight()
        elif choice == 4:
            page = int(input('Page : '))
            flight.paginate(page, 5)
        elif choice == 5:
            flight.printHistory()
        elif choice == 6:
            break
        else:
            print('Choice not found')

main()

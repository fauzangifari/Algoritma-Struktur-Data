from array import array

class Queue:
    def __init__(self):
        self.queue = array('i', [])

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Antrian Kosong")
        else:
            self.queue.pop(0)

    def display(self):
        if len(self.queue) == 0:
            print("Antrian Kosong")
        else:
            for i in self.queue:
                print(i, end=' ')

def main():
    q = Queue()
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list:
        q.enqueue(i)
    print("Sebelum : ", end='')
    q.display()
    print("\nSesudah : ", end='')
    q.display()

if __name__ == "__main__":
    main()
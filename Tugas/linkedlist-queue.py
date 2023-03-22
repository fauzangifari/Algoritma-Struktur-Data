class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Antrian Kosong")
        else:
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("Antrian Kosong")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next

def main():
    q = Queue()
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list:
        q.enqueue(i)
    print("Sebelum : ", end='')
    q.display()
    print("\nSesudah : ", end='')
    q.display()

main()

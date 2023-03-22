class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack Kosong")
        else:
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("Stack Kosong")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next


def main():
    s = Stack()
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list:
        s.push(i)
    print("Sebelum di push: ", end='')
    for i in list:
        print(i, end=' ')
    print("\nSetelah di push ke Stack: ", end="")
    s.display()
    s.pop()

main()

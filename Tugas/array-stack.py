class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def display(self):
        print(self.items)

def main():
    s = Stack()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in data:
        s.push(item)
    print("Sebelum : ", end='')
    s.display()
    print("Sesudah : ", end='')
    s.display()

main()

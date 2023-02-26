"""
This code defines a class called "Stack" that implements
a stack data structure using a list to store the elements.
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(5)
    print(s)
    s.push(8)
    s.push(6)
    print(s)
    print(s.size())
    print(s.pop())
    print(s)
    print(s.peek())

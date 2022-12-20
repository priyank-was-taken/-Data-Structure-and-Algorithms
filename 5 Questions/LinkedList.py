from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        node = self.head
        result = 0
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self



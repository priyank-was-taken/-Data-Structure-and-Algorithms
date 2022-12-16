
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        self.count += 1
        return "Circular Linked List is created"


CSLinkedList = CircularSinglyLinkedList()
CSLinkedList.createCSLL('hello')
print([node.value for node in CSLinkedList])

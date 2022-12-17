
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCDLL(self, value):
        node = Node(value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        print("Linked List is created")


CDLinkedList = CircularDoublyLinkedList()
CDLinkedList.createCDLL("hello")
print([node.value for node in CDLinkedList])
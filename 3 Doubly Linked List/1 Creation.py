class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # --------------------------Creation of Doubly Linked List----------------------------

    def createDLL(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node


DLinkedList = DoublyLinkedList()
DLinkedList.createDLL('hello')

print([node.value for node in DLinkedList])
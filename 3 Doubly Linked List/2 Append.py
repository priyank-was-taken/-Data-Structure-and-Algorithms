
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

    # --------------------------Append Doubly Linked List----------------------------

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode

        else:
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode


DLinkedList = DoublyLinkedList()
DLinkedList.append('hello')
DLinkedList.append('are')
DLinkedList.append('are')
DLinkedList.append('you?')

print([node.value for node in DLinkedList])
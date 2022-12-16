class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # --------------------------Append Doubly Linked List----------------------------

    def appendDLL(self, value):
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
        self.count += 1

    def deleteDLL(self, location):
        if self.head is None:
            print("Linked List doesn't exist")

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

                # to update the tail Node
                if currentNode.next is None:
                    self.tail = currentNode


DLinkedList = DoublyLinkedList()
DLinkedList.appendDLL('hello')
DLinkedList.appendDLL('how')
DLinkedList.appendDLL('are')
DLinkedList.appendDLL('you?')
print([node.value for node in DLinkedList])
DLinkedList.deleteDLL(3)
print([node.value for node in DLinkedList])
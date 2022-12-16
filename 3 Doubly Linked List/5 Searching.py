
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

    def searchSLL(self, item):
        currentNode = self.head
        index = 0
        while currentNode:
            if currentNode.value == item:
                print(f'item "{item}" found at index [{index}]')
                break
            if index == self.count - 1:
                print(f'item "{item}" does not exist')
                break
            currentNode = currentNode.next
            index += 1


DLinkedList = DoublyLinkedList()
DLinkedList.appendDLL('hello')
DLinkedList.appendDLL('how')
DLinkedList.appendDLL('are')
DLinkedList.appendDLL('you?')
print([node.value for node in DLinkedList])
DLinkedList.searchSLL("ar")


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
            if node == self.tail:
                break
            node = node.next

    # --------------------------Append Doubly Linked List----------------------------

    def appendCDLL(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            self.head = newNode
            self.tail = newNode

        else:
            newNode.prev = self.tail
            newNode.next = self.tail.next
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def searchCDLL(self, item):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.head
            index = 0
            while currentNode:
                if currentNode.value == item:
                    print(f'Item "{item}" found at index [{index}]')
                    break
                if currentNode.next == self.head:
                    print(f'Item "{item}" does not exist')
                    break
                currentNode = currentNode.next
                index += 1


DLinkedList = DoublyLinkedList()
DLinkedList.appendCDLL('hello')
DLinkedList.appendCDLL('how')
DLinkedList.appendCDLL('are')
DLinkedList.appendCDLL('you?')
print([node.value for node in DLinkedList])
DLinkedList.searchCDLL('you?')

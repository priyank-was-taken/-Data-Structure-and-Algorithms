import time


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
            if node.next == self.head:
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

    def reverseTraverseCDLL(self):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                # time.sleep(1)
                currentNode = currentNode.prev
                if currentNode == self.tail:
                    break


DLinkedList = DoublyLinkedList()
DLinkedList.appendCDLL('hello')
DLinkedList.appendCDLL('how')
DLinkedList.appendCDLL('are')
DLinkedList.appendCDLL('you?')
print([node.value for node in DLinkedList])
DLinkedList.reverseTraverseCDLL()
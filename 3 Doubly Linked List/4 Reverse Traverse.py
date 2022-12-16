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

    def reverseTraverse(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value)
            if currentNode == self.head:
                break
            currentNode = currentNode.prev



DLinkedList = DoublyLinkedList()
DLinkedList.appendDLL('hello')
DLinkedList.appendDLL('how')
DLinkedList.appendDLL('are')
DLinkedList.appendDLL('you?')
print([node.value for node in DLinkedList])
DLinkedList.reverseTraverse()
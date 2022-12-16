
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

    # ---------------------------Insertion in Doubly Linked List---------------------------

    def insertionDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                if currentNode == self.tail:
                    newNode.next = None
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = currentNode.next
                    newNode.prev = currentNode
                    newNode.next.prev = newNode  # or -- currentNode.next.prev = newNode
                    currentNode.next = newNode

    # ------------------------------------Print Nodes of Linked List-------------------------------------

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            if currentNode.next == self.head:
                break
            currentNode = currentNode.next


DLinkedList = DoublyLinkedList()
# DLinkedList.createDLL('hello')
DLinkedList.insertionDLL('hello', 0)
DLinkedList.insertionDLL('how', 1)
DLinkedList.insertionDLL('are', 2)
DLinkedList.insertionDLL('you?', 3)
# DLinkedList.insertionDLL(3)
print([node.value for node in DLinkedList])
# DLinkedList.printList()
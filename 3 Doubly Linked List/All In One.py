
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

    # -------------------------------Creation of Doubly Linked List-------------------------------

    def createDLL(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node

    # ---------------------------------Append Doubly Linked List---------------------------------

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

    # -----------------------------Traversing in Doubly Linked List------------------------------

    def traverseDLL(self):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.next

    # -----------------------------Reverse Traversing in Doubly Linked List------------------------------

    def reverseTraverseDLL(self):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                currentNode = currentNode.prev

    # -----------------------------Searching in Doubly Linked List------------------------------

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

    # -----------------------------Deletion in Doubly Linked List------------------------------

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
DLinkedList.appendDLL('hello')
DLinkedList.appendDLL('how')
DLinkedList.appendDLL('are')
DLinkedList.appendDLL('you?')
# DLinkedList.insertionDLL(3)
DLinkedList.deleteDLL(3)
print([node.value for node in DLinkedList])
DLinkedList.traverseDLL()
DLinkedList.reverseTraverseDLL()
# DLinkedList.printList()
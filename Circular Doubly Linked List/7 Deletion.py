class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
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

    # ------------------------------deletion in Circular Doubly Linked List------------------------------

    def deletionCDLL(self, location):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                currentNode.next.prev = currentNode
                if currentNode.next == self.head:
                    self.tail = currentNode
                    self.head.prev = self.tail

    # ----------------------------delete entire Linked List----------------------------

    def delete_entire(self):
        self.head = None
        self.tail = None


CDLinkedList = CircularDoublyLinkedList()
CDLinkedList.appendCDLL("hello")
CDLinkedList.appendCDLL("how")
CDLinkedList.appendCDLL("are")
CDLinkedList.appendCDLL("you?")
print([node.value for node in CDLinkedList])
CDLinkedList.deletionCDLL(2)
print([node.value for node in CDLinkedList])

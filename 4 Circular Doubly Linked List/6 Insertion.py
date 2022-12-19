
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

    def insertCDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode

            elif location == -1:
                newNode.next = self.tail.next
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.prev = currentNode
                newNode.next = nextNode


CDLinkedList = CircularDoublyLinkedList()
CDLinkedList.appendCDLL("hello")
CDLinkedList.appendCDLL("how")
CDLinkedList.appendCDLL("are")
CDLinkedList.appendCDLL("you?")
print([node.value for node in CDLinkedList])
CDLinkedList.insertCDLL('test', 3)
print([node.value for node in CDLinkedList])
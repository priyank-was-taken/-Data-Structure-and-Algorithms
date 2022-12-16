class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def appendSLL(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                currentNode = self.head
                index = 0
                while index < location-1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
                # if currentNode == self.tail:
                #     self.tail = currentNode


SLinkedList = SinglyLinkedList()
SLinkedList.appendSLL('quinn')
SLinkedList.appendSLL('harley')
SLinkedList.insertSLL('harl', 2)
print([node.value for node in SLinkedList])

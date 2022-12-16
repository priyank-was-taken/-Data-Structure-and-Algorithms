
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
        self.count += 1

    def deletionSSL(self, location):
        if self.head is None:
            print("The LinkedList doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    currentNode = self.head
                    while currentNode:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next
                    currentNode.next = None
                    self.tail = currentNode
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

                # to update the tail node
                if currentNode.next is None:
                    self.tail = currentNode

    # ----------------------------delete entire list--------------------------
    def delete_entire(self):
        if self.head is None:
            print("the singly linked list does not exist")
        else:
            self.head = None
            self.tail = None


SLinkedList = SinglyLinkedList()
SLinkedList.appendSLL('quinn')
SLinkedList.appendSLL('harley')
SLinkedList.appendSLL('summer')
print([node.value for node in SLinkedList])
SLinkedList.deletionSSL(2)
print([node.value for node in SLinkedList])

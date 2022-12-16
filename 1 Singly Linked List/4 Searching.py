
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


SLinkedList = SinglyLinkedList()
SLinkedList.appendSLL('quinn')
SLinkedList.appendSLL('harley')
print([node.value for node in SLinkedList])
SLinkedList.searchSLL('harledfy')

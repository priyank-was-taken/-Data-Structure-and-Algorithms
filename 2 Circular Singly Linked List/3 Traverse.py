
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
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

    def appendCSLL(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            if currentNode.next == self.head:
                break
            currentNode = currentNode.next


CSLinkedList = CircularSinglyLinkedList()
CSLinkedList.appendCSLL('hello')
CSLinkedList.appendCSLL('how')
CSLinkedList.appendCSLL('are')
CSLinkedList.appendCSLL('you?')
print([node.value for node in CSLinkedList])
CSLinkedList.traverse()

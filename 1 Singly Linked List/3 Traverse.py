
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singlylinkedlist:
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

    def traverseSLL(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next


SLinkedList = singlylinkedlist()
SLinkedList.appendSLL('quinn')
SLinkedList.appendSLL('harley')
print([node.value for node in SLinkedList])
SLinkedList.traverseSLL()

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singlylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createSLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node


SLinkedList = singlylinkedlist()
SLinkedList.createSLL('quinn')
print([node.value for node in SLinkedList])

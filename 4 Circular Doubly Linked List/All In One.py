
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

    # --------------------------Creation of Doubly Linked List----------------------------

    def createDLL(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        self.count += 1
        return "Circular Linked List is created"

    # -----------------------append in Circular Doubly linked list----------------------

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

    # -----------------------traversing in Circular Doubly linked list----------------------

    def traverseCDLL(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            # time.sleep(1)
            if currentNode.next == self.head:
                break
            currentNode = currentNode.next

    # -----------------------Reverse traversing in Circular Doubly linked list----------------------

    def reverseTraverseCDLL(self):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.tail
            while currentNode:
                print(currentNode.value)
                # time.sleep(1)
                currentNode = currentNode.prev
                if currentNode == self.tail:
                    break

    # -----------------------Searching in Circular Doubly linked list----------------------

    def searchCDLL(self, item):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            currentNode = self.head
            index = 0
            while currentNode:
                if currentNode.value == item:
                    print(f'Item "{item}" found at index [{index}]')
                    break
                if currentNode.next == self.head:
                    print(f'Item "{item}" does not exist')
                    break
                currentNode = currentNode.next
                index += 1

    # -----------------------Insertion in Circular Doubly linked list----------------------

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
# CDLinkedList.createDLL("hello")
CDLinkedList.appendCDLL("hello")
CDLinkedList.appendCDLL("how")
CDLinkedList.appendCDLL("are")
CDLinkedList.appendCDLL("you?")
# CDLinkedList.traverseCDLL()
# CDLinkedList.reverseTraverseCDLL()
CDLinkedList.searchCDLL("are")
# CDLinkedList.insertCDLL("test", 2)
# CDLinkedList.deletionCDLL(2)

print([node.value for node in CDLinkedList])

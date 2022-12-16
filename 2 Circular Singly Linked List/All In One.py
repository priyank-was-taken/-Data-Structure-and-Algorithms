# x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x
# x--x--x--x--x--x--------------------------CIRCULAR SINGLY LINKED LIST---------------------------------x--x--x--x--x--x
# x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x


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

    # --------------------------Creation of Circular 1 Singly Linked List------------------------------------

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        self.count += 1
        return "Circular Linked List is created"

    # ------------------------------------Insertion in Circular 1 Singly Linked List------------------------------------

    def insertCSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            # return "the head reference is None"
            self.head = newNode
            newNode.next = newNode
            self.tail = newNode
            return

        # ------------------------another method for insertion at last---------------------------
        # currentNode = self.head
        # while currentNode.next is not self.head:
        #     currentNode = currentNode.next
        # currentNode.next = newNode
        # newNode.next = self.head

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode

    # -------------------------------------traversing in Circular 1 Singly Linked List----------------------------------

    def traverseCSLL(self):
        if self.head is None:
            return "the linkedlist doesn't exist"

        else:
            currentNode = self.head
            while True:
                print(currentNode.value)
                if currentNode.next is self.head:
                    break
                currentNode = currentNode.next

    # ------------------------------------Searching in Circular 1 Singly Linked List------------------------------------

    def searchCSLL(self, item):
        if self.head is None:
            print("Linked List doesn't exist")

        else:
            currentNode = self.head
            index = 0
            while currentNode:
                if currentNode.value == item:
                    print(f'"{item}" found at index [{index}]')
                currentNode = currentNode.next
                index += 1
                if currentNode == self.head:
                    break

    # ------------------------------------Deletion In Circular Linked List----------------------------------------------

    def deletionCSLL(self, location):
        if self.head is None:
            return "the linkedlist doesn't exist"

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    currentNode = self.head
                    while True:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next
                    currentNode.next = self.head
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
                if currentNode.next == self.head:
                    self.tail = currentNode

    # ------------------------------------print method------------------------------------------------------------------

    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.value)
            if currentNode.next is self.head:
                break
            currentNode = currentNode.next

    # ---------------------------------------------delete entire SSL---------------------------------------------------

    def delete_entire(self):
        if self.head is None:
            print("the singly linked list does not exist")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


CSLinkedList = CircularSinglyLinkedList()
# CSLinkedList.createCSLL('aman')
CSLinkedList.insertCSLL('aman', 0)
CSLinkedList.insertCSLL('deep', 1)
CSLinkedList.insertCSLL('breydan', 2)
CSLinkedList.insertCSLL('logan', 3)
CSLinkedList.insertCSLL('tincy', 4)
# CSLinkedList.delete_entire()
CSLinkedList.traverseCSLL()
# CSLinkedList.searchCSLL('erer')
print([node.value for node in CSLinkedList])
CSLinkedList.deletionCSLL(2)
# # print([node.value for node in CSLinkedList])
# # CSLinkedList.insertCSLL('priyank', 4)
print([node.value for node in CSLinkedList])
# print([])
CSLinkedList.printList()
# -----------------------------------------------------

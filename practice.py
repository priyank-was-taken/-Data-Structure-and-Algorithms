class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "Circular 1 Singly Linked List is created"

    def insertCSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.head = newNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
                if currentNode == self.tail:
                    self.tail = newNode
                    self.tail.next = self.head

    def traversCSLL(self):
        if self.head is None:
            return "Linked List doesn't exist"
        else:
            currentNode = self.head
            while True:
                print(currentNode.value)
                currentNode = currentNode.next
                if currentNode == self.head:
                    break

    def searchCSLL(self, item):
        if self.head is None:
            return "Linked List doesn't exist"
        else:
            currentNode = self.head
            index = 0
            while True:
                if currentNode.value == item:
                    print("the item found at index", index)
                    break
                if currentNode.next == self.head:
                    print("item does not exist in Linked List")
                    break
                currentNode = currentNode.next
                index += 1

    def deletionCSLL(self, location):
        if self.head is None:
            return "LinkedList does not exist"
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

    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.value)
            if currentNode.next == self.head:
                break
            currentNode = currentNode.next


CSLinkedList = CircularSinglyLinkedList()
# CSLinkedList.createCSLL("priyank")
CSLinkedList.insertCSLL("priyank", 0)
CSLinkedList.insertCSLL("sam", 1)
CSLinkedList.insertCSLL("hop", 2)
CSLinkedList.insertCSLL("freak", 3)
CSLinkedList.insertCSLL("res", 4)
# CSLinkedList.traversCSLL()
# CSLinkedList.searchCSLL('sd')
print([node.value for node in CSLinkedList])
# CSLinkedList.deletionCSLL(0)
print([node.value for node in CSLinkedList])
CSLinkedList.printList()


# class Node:
#     # Singly linked node
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
# class singly_linked_list:
#     def __init__(self):
#         # Createe an empty list
#         self.tail = None
#         self.head = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append items on the list
#         node = Node(data)
#
#         if self.head is None:
#             self.head = node
#             self.tail = node
#
#         else:
#             self.tail.next = node
#             self.tail = node
#
#     def delete_item(self, data):
#         # Delete an item from the list
#         currentNode = self.head
#         prevNode = self.head
#         while currentNode:
#             if currentNode.data == data:
#                 if currentNode == self.head:
#                     self.head = currentNode.next
#                 else:
#                     prevNode.next = currentNode.next
#                 self.count -= 1
#                 return
#             prevNode = currentNode
#             currentNode = currentNode.next
#
#     def iterate_item(self):
#         # Iterate the list.
#         current_item = self.head
#         while current_item:
#             val = current_item.data
#             current_item = current_item.next
#             yield val
#
#
# items = singly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
#
# print("Original list:")
# for val in items.iterate_item():
#     print(val)

# print("\nAfter removing the first item from the list:")
# items.delete_item('Java')
# items.delete_item('Python')
# for val in items.iterate_item():
#     print(val)

# class Node:
#     # Singly linked node
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
# class singly_linked_list:
#     def __init__(self):
#         # Createe an empty list
#         self.tail = None
#         self.head = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append items on the list
#         node = Node(data)
#         if self.head:
#             self.head.next = node
#             self.head = node
#         else:
#             self.tail = node
#             self.head = node
#         self.count += 1
#
#     def __getitem__(self, index):
#         if index > self.count - 1:
#             return "Index out of range"
#         current_val = self.tail
#         for n in range(index):
#             current_val = current_val.next
#         return current_val.data
#
#     def __setitem__(self, index, value):
#         if index > self.count - 1:
#             raise Exception("Index out of range.")
#         current = self.tail
#         for n in range(index):
#             current = current.next
#         current.data = value
#
#
# items = singly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
#
# print("Modify items by index:")
# items[1] = "SQL"
# print("New value: ", items[1])
# items[4] = "Perl"
# print("New value: ", items[4])
#
# #
# def countCurrency(amount):
#     notes = [2000, 500, 200, 100, 50]
#     notesCount = {}
#
#     for note in notes:
#         if amount >= note:
#             notesCount[note] = amount // note
#             amount = amount % note
#
#     print("Currency Count ->")
#     for key, val in notesCount.items():
#         print(f"{key} : {val}")
#
#
# # Driver code
# amount = 8050
# countCurrency(amount)
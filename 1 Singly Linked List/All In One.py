# x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x
# x--x--x--x--x--x-------------------------------SINGLY LINKED LIST-------------------------------------x--x--x--x--x--x
# x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singlylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # ----------------------Append in SSL----------------------

    def append_item(self, data):
        # Append items on the list
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node
        # self.count += 1

    # --------------------insertion in SSL---------------------

    def insertSSL(self, value, location):
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
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # ----------------------------treverse in SSL----------------------------

    def treverse(self):
        if self.head is None:
            print("the singly linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # -------------------------------------Search in SSL----------------------------------

    def search(self, item):
        if self.head is None:
            print("the singly linked list does not exist")
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == item:
                    print("item found at index", index)
                index += 1
                node = node.next

    # -------------------------------------deletion in SSL--------------------------------

    def deletion(self, location):
        if self.head is None:
            print("the singly linked list does not exist")
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
                    node = self.head
                    while True:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # ---------------------------------------------delete entire SSL---------------------------------------------------

    def delete_entire(self):
        if self.head is None:
            print("the singly linked list does not exist")
        else:
            self.head = None
            self.tail = None

    def __getitem__(self, index):
        # if index > self.count - 1:
        #     return "Index out of range"
        current_val = self.head
        for n in range(index):
            current_val = current_val.next
        return current_val.value


SLinkedList = singlylinkedlist()
SLinkedList.append_item('aman')
SLinkedList.append_item('deep')
SLinkedList.append_item('breydan')
SLinkedList.append_item('logan')
SLinkedList.append_item('tincy')
# singlylinkedlist.insertSSL(33, 3)
# singlylinkedlist.insertSSL(33, 1)
# singlylinkedlist.insertSSL(33, 3)

# # print("[0,1,2,3,4]")
print([node.value for node in SLinkedList])
# # singlylinkedlist.treverse()
# # singlylinkedlist.search(33)
# singlylinkedlist.deletion(-1)
# print([node.value for node in singlylinkedlist])
# singlylinkedlist.delete_entire()
print(SLinkedList[3])
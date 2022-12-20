
# Q2 -> Implement an algorithm to find nth last in a Singly Linked List

from LinkedList import LinkedList


def nthfromlast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthfromlast(customLL, 3))

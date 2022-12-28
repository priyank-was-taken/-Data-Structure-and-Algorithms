class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isempty
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return str(value)+" pushed"

    # pop
    def pop(self):
        if self.isempty():
            return "the stack is empty"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isempty():
            return "the stack is empty"
        else:
            return self.list[len(self.list) - 1]

    # delete
    def delete(self):
        self.list = None


lst = Stack()
print(lst.isempty())
print(lst.push(1))
print(lst.push(2))
print(lst.push(3))
print(lst.push(4))
print(lst.pop(), "--- popped")
print(lst.peek(), "--- peek")
print("---------------")
print(lst)

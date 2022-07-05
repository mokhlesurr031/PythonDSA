class ArrayStack:
    """LIFO stack implementation using Python List"""

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def push(self, val):
        self.data.append(val)

    def top(self):    #return top value without deleting
        if self.is_empty():
            return None
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def show(self):
        return self.data

s = ArrayStack()
print(s.__len__())
print(s.top())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.show())
s.pop()
print(s.show())
print(s.top())
print(s.show())


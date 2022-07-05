class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
    """LIFO stack implementation using LinkedList"""

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, val):
        """Add element val to the top of the stack"""

        self.head = Node(val, self.head)
        self.size +=1

    def top(self):
        """Return the element from the top of the stack but no removal"""
        if self.is_empty():
            return None
        return self.head.element

    def pop(self):
        """Remove and return the element from the top of the stack"""

        if self.is_empty():
            return None

        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer

    def show(self):
        while self.head:
            print(self.head.element, end = ' ')
            self.head = self.head.next
        else:
            print("")


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
# print(ll.top())
# ll.show()
print(ll.__len__())
print(ll.pop())
ll.show()




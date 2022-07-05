class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def __len__(self):
        return self.size

    def _is_empty(self):
        return self.size==0

    def first(self):
        """Return the element at the front of the queue but no remove"""
        if self._is_empty():
            return None
        return self.head.element


    def dequeue(self):
        """Remove and return the first element fo the queue"""
        if self._is_empty():
            return None

        answer = self.head.element
        self.head = self.head.next
        self.size -=1
        if self._is_empty():
            return None
        return answer


    def enqueue(self, val):
        """Add an element to the back of the queue"""
        newest = Node(val, None)
        if self._is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size +=1


    def show(self):
        while self.head:
            print(self.head.element, end=' ')
            self.head = self.head.next




q = LinkedList()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# q.show()

print(q.first())
print(q.dequeue())
print(q.first())
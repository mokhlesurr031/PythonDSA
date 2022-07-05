class ArrayQueue:
    """FIFO queue implementation using Python List"""

    DEFAULT_CAPACITY = 0

    def __init__(self):
        # self.data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self.data = [0]
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def first(self):    #return first value without deleting
        if self.is_empty():
            return None
        return self.data[self.front]

    def dequeue(self):
        """Remove and return the first element of the queue"""

        if self.is_empty():
            return None
        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.size -=1
        return answer

    def enqueue(self, val):
        """Add an element to the back of the queue"""

        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = val
        self.size += 1

    def resize(self, cap):
        """Resize to a new list of capacity"""

        old = self.data
        self.data = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1+walk) % len(old)
        self.front = 0

    def show(self):
        return self.data

q = ArrayQueue()
print(q.show())
print(q.dequeue())
print(q.first())
print(q.is_empty())
print(q.__len__())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.show())
print(q.first())


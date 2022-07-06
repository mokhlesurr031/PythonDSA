class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def remove_first(self):
        self.head = self.head.next

    def insert_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def remove_last(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def insert_after(self, prev_node, data):
        node = Node(data)
        if prev_node is None:
            print("Node doesn't exists")
            return

        node.next = prev_node.next
        prev_node.next = node

    def remove_node(self, data):
        temp = self.head
        while temp.next.data!=data:
            temp = temp.next
        temp.next = temp.next.next

    def print_ll(self):
        initial = self.head
        while initial:
            print(initial.data, end=" ")
            initial = initial.next
        print("")


ll = LinkedList()
ll.head = Node(1)

ll.insert_last(2)
ll.insert_last(3)

ll.insert_first(10)

ll.insert_after(ll.head, 15)

ll.print_ll()

# ll.remove_first()

# ll.print_ll()

ll.remove_last()

ll.insert_last(15)

ll.print_ll()

ll.remove_node(2)

ll.print_ll()


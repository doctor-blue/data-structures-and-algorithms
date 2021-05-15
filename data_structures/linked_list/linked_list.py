from node import Node
import math

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self.size += 1
        return self

    def append(self, value):
        if self.is_empty:
            return self.push(value)
        self.tail.next = Node(value, self.tail.next)
        self.tail = self.tail.next
        self.size += 1
        return self

    def node_at(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node

    def insert(self, value, index):
        if index <= 0:
            return self.push(value)
        if index >= self.size:
            return self.append(value)

        after_node = self.node_at(index-1)
        node = Node(value, after_node.next)
        after_node.next = node
        self.size += 1
        return self

    def pop(self):
        if not self.is_empty:
            self.size -= 1
            result = self.head.value
            self.head = self.head.next
            if self.is_empty:
                self.tail = None
            return result

    def remove_last(self):
        if self.head is None:
            return None

        if self.head.next is None:
            return self.pop()

        self.size -= 1
        prev = self.head
        current = self.head
        next = current.next
        while next is not None:
            prev = current
            current = next
            next = next.next

        prev.next = None
        self.tail = prev
        return current.value

    def remove_last2(self):
        if self.head is None:
            return None

        if self.head.next is None:
            return self.pop()

        self.size -= 1
        last_node = self.node_at(self.size-1)
        last_node.next = None
        result = self.tail.value
        self.tail = last_node
        return result

    def remove_at(self, index):
        if index <= 0:
            return self.pop()
        if index >= self.size - 1:
            return self.remove_last()

        prev = self.head
        current = self.head
        next = current.next
        current_index = 0
        while next is not None and current_index < index:
            prev = current
            current = next
            next = current.next
            current_index += 1
        
        prev.next = next 
        self.size -=1
        return current.value

    def reverse(self):
        new_list = LinkedList()
        current = self.head
        while current is not None:
            new_list.push(current.value)
            current = current.next
        self.head = new_list.head
        self.tail = new_list.tail
        return self;

    def get_middle(self):
        return self.node_at(math.floor((self.size-1)/2)).value


    def to_string(self):
        if self.is_empty:
            return "Empty list"
        else:
            return self.head.to_string()

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def to_string(self):
        if self.next is not None:
            return "{0}->{1}".format(self.value, self.next.to_string())
        else:
            return "{0}".format(self.value)

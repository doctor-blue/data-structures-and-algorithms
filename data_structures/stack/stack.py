class Stack:
    def __init__(self):
        self.list = list()

    @property
    def is_empty(self):
        return len(self.list) == 0

    def push(self, element):
        self.list.insert(0,element)
        return self

    def pop(self):
        if self.is_empty:
            return None
        return self.list.pop()

    def to_string(self):
        str = "----top---\n"
        for i in self.list[::-1]:
            str += '{0}\n'.format(i)
        str += '----bottom----'
        return str

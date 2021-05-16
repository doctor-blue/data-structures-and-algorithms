class Queue(object):
    def __init__(self):
        self.list = list()

    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, element):
        self.list.append(element)
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.list.pop(0)

    def to_string(self):
        str = 'font-|'
        for e in self.list:
            str+='{0}|'.format(e)
        str += '-back'
        return str

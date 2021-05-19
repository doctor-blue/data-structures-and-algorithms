from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add(self, node):
        if node is not TreeNode:
            self.children.append(node)

    # Di chuyển từ trên xuống dưới và từ trái qua phải.
    # Thăm node từ gốc tới leaf trái -> phải
    def for_each_depth_first(self, visit):
        visit(self)
        for node in self.children:
            node.for_each_depth_first(visit)

    # Di chuyển theo từng tầng một
    def for_each_level_order(self, visit):
        visit(self)
        queue = Queue()
        for node in self.children:
            queue.put_nowait(node)

        node = queue.get_nowait()
        while node is not None:
            visit(node)
            for child in node.children:
                queue.put_nowait(child)
            if queue.empty():
                node = None
            else:
                node = queue.get_nowait()

    def search(self, value):
        if value == self.value:
            return self
        queue = Queue()
        for node in self.children:
            queue.put_nowait(node)

        node = queue.get_nowait()
        while node is not None:
            if node.value == value:
                return node
            for child in node.children:
                queue.put_nowait(child)
            if queue.empty():
                node = None
            else:
                node = queue.get_nowait()

        return None

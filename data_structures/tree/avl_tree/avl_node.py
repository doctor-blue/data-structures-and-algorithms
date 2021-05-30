class AVLNode:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.left_child = None
        self.right_child = None

    @property
    def left_height(self):
        if self.left_child is None:
            return -1
        else:
            return self.left_child.height

    @property
    def right_height(self):
        if self.right_child is None:
            return -1
        else:
            return self.right_child.height

    @property
    def balance_factor(self):
            return self.left_height - self.right_height

    def diagram(self, node, top="", root="", bottom=""):
        if node is not None:
            if node.left_child is None and node.right_child is None:
                return f"{root}{node.value}\n"
            else:
                return self.diagram(node.right_child, f"{top} ", f"{top}┌──", f"{top}│ ") \
                    + root + f"{node.value}\n" \
                    + self.diagram(node.left_child,
                                   f"{bottom}│ ", f"{bottom}└──", f"{bottom} ")
        return f"{root}None\n"

    def to_string(self):
        return self.diagram(self)

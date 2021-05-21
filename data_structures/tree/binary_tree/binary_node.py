class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

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

    # left-current-right
    def traverse_in_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self.value)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    # current-left-right
    def traverse_pre_order(self, visit):
        visit(self.value)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    # left-right-current
    def traverse_post_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self.value)

    def height(self, node):
        if node is not None:
            return 1 + max(self.height(node.left_child), self.height(node.right_child))
        return -1

    def traverse_pre_order_with_none(self, visit):
        visit(self.value)
        if self.left_child is not None:
            self.left_child.traverse_pre_order_with_none(visit)
        else:
            visit(None)
        if self.right_child is not None:
            self.right_child.traverse_pre_order_with_none(visit)
        else:
            visit(None)

    def to_list(self):
        values = []

        def visit(value):
            values.append(value)
        self.traverse_pre_order_with_none(visit)
        return values


def make_binary_tree(arr):
    if type(arr) is list:
        root_value = None
        if len(arr) > 0:
            root_value = arr.pop(0)
        if root_value is None:
            return None

        root = BinaryNode(root_value)
        root.left_child = make_binary_tree(arr) 
        root.right_child = make_binary_tree(arr)
        return root

from binary_node import BinaryNode


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_node(self.root, value)

    def delete(self, value):
        self.root = self.delete_node(self.root, value)

    def delete_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            if node.left_child is None and node.right_child is None:
                return None
            elif node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            minValue = node.right_child.min.value
            if minValue is not None:
               node.value = minValue
            node.right_child = self.delete_node(node.right_child, node.value)

        elif node.value > value:
            node.left_child = self.delete_node(node.left_child, value)
        else:
            node.right_child = self.delete_node(node.right_child, value)
        return node

    def contains(self, value):
        current = self.root
        while current is not None:
            if current.value == value:
                return True

            if current.value < value:
                current = current.right_child
            else:
                current = current.left_child
        return False

    def insert_node(self, node, value):
        if node is None:
            return BinaryNode(value)
        if value < node.value:
            node.left_child = self.insert_node(node.left_child, value)
        else:
            node.right_child = self.insert_node(node.right_child, value)
        return node

    def to_string(self):
        if self.root is not None:
            return self.root.to_string()
        return None

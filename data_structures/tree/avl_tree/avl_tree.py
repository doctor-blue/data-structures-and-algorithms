from avl_node import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child
        pivot.left_child = node
        if node.left_child is not None:
            node.height = max(node.left_child.height, node.right_child.height) + 1
        pivot.height = max(pivot.left_child.height, pivot.right_child.height)+1
        return pivot

    def right_rotate(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child
        pivot.right_child = node
        node.height = max(node.left_child.heigh, node.right_child.height) + 1
        pivot.height = max(pivot.left_child.heigh, pivot.right_child.height)+1
        return pivot

    def right_left_rotate(self, node):
        if node.right_child is None:
            return node
        right_child = node.right_child
        node.right_child = self.right_rotate(right_child)
        return self.left_rotate(node.node)

    def left_right_rotate(self, node):
        if node.left_child is None:
            return node
        left_child = node.left_child
        node.left_child = self.left_rotate(left_child)
        return self.right_rotate(node)

    def balanced(self, node):
        balance_factor = node.balance_factor
        if balance_factor == 2:
            if node.left_child.balance_factor == -1:
                return self.left_right_rotate(node)
            else:
                return self.right_rotate(node)
        elif balance_factor == -2:
            if node.right_child.balance_factor == 1:
                return self.right_left_rotate(node)
            else:
                return self.left_rotate(node)
        else:
            return node

    def insert(self, value):
        self.root = self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if node is None:
            return AVLNode(value)

        if node.value < value:
            node.right_child = self.insert_node(node.right_child, value)
        else:
            node.left_child = self.insert_node(node.left_child, value)
        balancedNode = self.balanced(node)
        left_height = 0
        right_height = 0
        if balancedNode is not None:
            left_height = balancedNode.left_height
            right_height = balancedNode.right_height
        balancedNode.height = max(left_height, right_height) + 1
        return balancedNode
    
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

        balancedNode = self.balanced(node)

        balancedNode.height = max(balancedNode.left_height, balancedNode.right_height) + 1
        return balancedNode

    def to_string(self):
        if self.root is not None:
            return self.root.to_string()
        return None

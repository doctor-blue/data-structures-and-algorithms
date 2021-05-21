from binary_node import BinaryNode,make_binary_tree

zero = BinaryNode(0)
one = BinaryNode(1)
three = BinaryNode(3)
five = BinaryNode(5)
eight = BinaryNode(8)
ten = BinaryNode(10)
nine = BinaryNode(9)
four = BinaryNode(4)


zero.left_child = one
zero.right_child = three

one.left_child = five
one.right_child = eight

three.left_child = ten
three.right_child = nine

nine.left_child = four

# print(zero.to_string())

def visit(value):
    print(value)

# zero.traverse_in_order(visit)
# zero.traverse_pre_order(visit)
# zero.traverse_post_order(visit)
# print(zero.height(zero))

# print(zero.to_list())
print(make_binary_tree(zero.to_list()).to_string())


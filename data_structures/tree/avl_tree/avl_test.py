from avl_tree import AVLTree

tree = AVLTree()

for i in range(0,14):
    tree.insert(i)

print(tree.to_string())
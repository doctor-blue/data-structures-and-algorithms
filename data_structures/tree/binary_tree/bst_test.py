from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(3);
bst.insert(1)
bst.insert(4)
bst.insert(2)
bst.insert(0)
bst.insert(5)


print(bst.to_string())
bst.delete(3)
print(bst.to_string())
print(bst.contains(3))
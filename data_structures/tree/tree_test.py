from tree_node import TreeNode

orange = TreeNode("Orange")
red = TreeNode("Red")
yellow = TreeNode("Yellow")

brown = TreeNode("Brown")
black = TreeNode("Black")
pink = TreeNode("Pink")
white = TreeNode("White")

black.add(pink)
red.add(brown)
red.add(black)
yellow.add(white)

orange.add(red)
orange.add(yellow)

# orange.for_each_depth_first(lambda node: print(node.value))
# orange.for_each_level_order(lambda node: print(node.value))
print(orange.search("Pink"))
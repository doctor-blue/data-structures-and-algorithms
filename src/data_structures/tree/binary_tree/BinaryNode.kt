package data_structures.tree.binary_tree

class BinaryNode<T>(val value: T) {
    var leftChild: BinaryNode<T>? = null
    var rightChild: BinaryNode<T>? = null

    override fun toString() = diagram(this)

    private fun diagram(node: BinaryNode<T>?,
                        top: String = "",
                        root: String = "",
                        bottom: String = ""): String {
        return node?.let {
            if (node.leftChild == null && node.rightChild == null) {
                "$root${node.value}\n"
            } else {
                diagram(node.rightChild, "$top ", "$top┌──", "$top│ ") +
                        root + "${node.value}\n" + diagram(node.leftChild,
                        "$bottom│ ", "$bottom└──", "$bottom ")
            }
        } ?: "${root}null\n"
    }

    fun traverInOrder(visit: Visitor<T>) {
        leftChild?.traverInOrder(visit)
        visit(value)
        rightChild?.traverInOrder(visit)
    }

    fun traverPreOrder(visit: Visitor<T>){
        visit(value)
        leftChild?.traverPreOrder(visit)
        rightChild?.traverPreOrder(visit)
    }
    fun traverPostOrder(visit: Visitor<T>){
        leftChild?.traverPostOrder(visit)
        rightChild?.traverPostOrder(visit)
        visit(value)
    }
}
typealias Visitor<T> = (T) -> Unit
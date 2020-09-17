package data_structures.tree.binary_tree

fun main() {
    val one = BinaryNode(1)
    val zero = BinaryNode(0)
    val three = BinaryNode(3)
    val five = BinaryNode(5)
    val eight = BinaryNode(8)
    val ten = BinaryNode(10)

    one.leftChild = zero
    one.rightChild = three

    zero.rightChild = five
    zero.leftChild = ten

    three.rightChild = eight

    val tree = one

    print(tree)

    println("\n Traver In-Order\n")
    tree.traverInOrder {
        println(it)
    }

    println("\n Traver Pre-Order\n")
    tree.traverPreOrder {
        println(it)
    }

    println("\n Traver Post-Order\n")
    tree.traverPostOrder {
        println(it)
    }
}
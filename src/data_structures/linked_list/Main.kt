package data_structures.linked_list

fun main() {
/*    val node1=Node(value = 1)
    val node2=Node(value = 5)
    val node3=Node(value = 8)
    node1.next=node2
    node2.next=node3
    println(node1)*/


    //Create linkedList
    val linkedList = LinkedList<Int?>()
    //add to first
    linkedList.addToFirst(1).addToFirst(3).addToFirst(-2)

    //add to end
    linkedList.addToEnd(-32).addToEnd(5)

    //insertAt
    linkedList.insert(null, 2)

    //pop
    val poppedValue = linkedList.pop()

    //remove last
    val removedValue = linkedList.removeLast()

    //remove at 3
    val value=linkedList.removeAt(1)

    println("$linkedList size = ${linkedList.size}")


}
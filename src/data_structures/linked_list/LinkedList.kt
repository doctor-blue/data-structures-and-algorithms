package data_structures.linked_list

class LinkedList<T> {
    private var head: Node<T>? = null
    private var tail: Node<T>? = null
    var size: Int = 0

    fun isEmpty(): Boolean = size == 0

    fun addToFirst(value: T): LinkedList<T> {
        head = Node(value, head)
        if (tail == null) {
            tail = head
        }
        size++
        return this
    }

    fun addToEnd(value: T): LinkedList<T> {
        if (isEmpty()) {
            addToFirst(value)
            return this
        }
        tail?.next = Node(value)
        tail = tail?.next
        size++
        return this

    }

    fun nodeAt(index: Int): Node<T>? {
        var currentNode = head
        var currentIndex = 0

        while (currentNode != null && currentIndex < index) {
            currentNode = currentNode.next
            currentIndex++
        }
        return currentNode
    }

    fun insert(value: T, index: Int): LinkedList<T> {

        if (index >= size-1) return addToEnd(value)

        if (index <= 0) return addToFirst(value)

        val beforeNode = nodeAt(index - 1)
        val newNode = Node(value, beforeNode?.next)
        beforeNode!!.next = newNode
        size++
        return this

    }

    fun pop(): T? {
        if (!isEmpty()) size--

        val result = head?.value
        head = head?.next
        if (isEmpty()) tail = null

        return result
    }

    fun removeLast(): T? {
        val head = head ?: return null
        if (head.next == null) return pop()

        size--
        var pre = head
        var current = head

        var next = current.next
        while (next != null) {
            pre = current
            current = next
            next = current.next
        }
        pre.next = null
        tail = pre
        return current.value
    }

    fun removeAt(index: Int): T? {
        if (index >= size-1) return removeLast()
        if (index <= 0) return pop()

        val afterNode = nodeAt(index-1)
        val result = afterNode?.next?.value
         size--

        afterNode?.next = afterNode?.next?.next
        return result
    }


    override fun toString(): String {
        return if (isEmpty()) "Empty list" else head.toString()
    }

}
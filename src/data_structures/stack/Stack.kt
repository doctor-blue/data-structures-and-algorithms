package data_structures.stack

class Stack<T>() {
    companion object {
        fun <T> create(list: Iterable<T>): Stack<T> {
            val stack = Stack<T>()
            list.forEach {
                stack.push(it)
            }
            return stack
        }

        fun <T> stackOf(vararg item: T): Stack<T> {
            return create(item.asList())
        }
    }

    private val storage = arrayListOf<T>()

    val size: Int
        get() = storage.size

    val isEmpty: Boolean
        get() = size == 0

    fun push(element: T) {
        storage.add(element)
    }

    fun pop(): T? {
        if (!isEmpty) {
            return storage.removeAt(storage.size - 1)
        }
        return null
    }


    override fun toString(): String = buildString {
        appendln("=====top=====")
        storage.asReversed().forEach {
            appendln("$it")
        }
        appendln("=============")
    }
}
package data_structures.queues

class Queues<T> {
    private val list = arrayListOf<T>()
    val count: Int
        get() = list.size
    val isEmpty: Boolean
        get() = list.isEmpty()

    fun peek(): T? = list.getOrNull(0)

    fun enqueue(element: T): Boolean {
        list.add(element)
        return true
    }

    fun dequeue(): T? = if (isEmpty) null else list.removeAt(0)

    override fun toString(): String = buildString {
        append("- front - ")
        list.forEach {
            append("| $it ")
        }
        append(" - back -")
    }
}
package data_structures.queues

fun main() {
    val queues:Queues<Int> = Queues()
    queues.apply {
        enqueue(1)
        enqueue(2)
        enqueue(3)
        enqueue(4)
        enqueue(5)
    }

    println(queues)

    println("Dequeue")

    queues.dequeue()
    queues.dequeue()
    println(queues)

}
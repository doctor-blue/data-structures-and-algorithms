package data_structures.stack

fun main() {
    val stack=Stack<Int>().apply {
        push(1)
        push(2)
        push(3)
        push(4)
        push(5)
    }
    println(stack)
    val poppedElement=stack.pop()
    if (poppedElement!=null)
        println("Popped = $poppedElement")

    println(stack)

    val list= listOf<String>("A","B","C","D")
    val alphabetStack=Stack.create(list)
    println(alphabetStack)

    val doubleStack=Stack.stackOf(0.2,0.9,8.6,2.7,5.3)
    println(doubleStack)

}
package data_structures.tree

fun main() {
    /* val vegetarian = TreeNode("vegetarian")
     val nonVegetarian = TreeNode("non-vegetarian")
     val food = TreeNode("food").run {
         add(vegetarian)
         add(nonVegetarian)
     }*/

    val food = TreeNode("Food")

    val freshFood = TreeNode("Fresh food")
    val fastFood = TreeNode("Fast food")

    val vegetables = TreeNode("Vegetables")
    val spinach = TreeNode("Spinach")
    val eggplant = TreeNode("Eggplant")
    val broccoli = TreeNode("broccoli")

    val meat = TreeNode("Meat")
    val chicken = TreeNode("Chicken")
    val turkey = TreeNode("Turkey")

    val burger = TreeNode("Burger")
    val pizza = TreeNode("Pizza")

    food.add(fastFood)
    food.add(freshFood)

    fastFood.add(burger)
    fastFood.add(pizza)

    freshFood.add(vegetables)
    freshFood.add(meat)

    vegetables.add(spinach)
    vegetables.add(eggplant)
    vegetables.add(broccoli)

    meat.add(chicken)
    meat.add(turkey)

    println("Depth First\n")
    //Depth First

    food.forEachDepthFirst {
        println(it.value)
    }
    println("\n===============\n")
    println("Level-order traversal\n")
    //Level-order traversal
    food.forEachLevelOrder {
        println(it.value)
    }
    println("\n===============\n")
    println("Search")

    food.search("Apple")?.let {
        println("Found node: ${it.value}")
    } ?: println("Couldn't find Apple")


    food.search("Spinach")?.let {
        println("Found node: ${it.value}")
    } ?: println("Couldn't find Spinach")

}
from linked_list import LinkedList
import math
list = LinkedList()

list.push(1).push(20).push(10).append(12).append(30)

list.insert(-2, 2)
list.insert(22,2)

print(list.to_string())
# popped = list.remove_last()
# print(popped)
list.reverse()
print(list.to_string())

print(list.get_middle())
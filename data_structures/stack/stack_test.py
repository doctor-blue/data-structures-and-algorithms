from stack import Stack

stack = Stack()
stack.push(2).push(5).push(10).push(25)

print(stack.to_string())

print(stack.pop())

print(stack.to_string())

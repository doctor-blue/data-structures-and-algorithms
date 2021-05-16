from queues import Queue

queue = Queue()

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(9)

print(queue.to_string())

print(queue.dequeue())

print(queue.to_string())

from queue import PriorityQueue

t = PriorityQueue()
t.put(1)
t.put(2)
t.put(-9)

a = t.get()
print(a)

print(t.queue)

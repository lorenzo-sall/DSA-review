import adts


# TESTING THE Stack CLASS
print("-------------- TESTING STACK --------------")
s = adts.Stack()
print(s.is_empty())
for i in range(10):
    s.push(i+100)
print(f"peek: {s.peek()}")
print(f"pop: {s.pop()}")
print(f"pop: {s.pop()}")
print(f"pop: {s.pop()}")
print(f"is_empty: {s.is_empty()}")
print(f"size: {s.size()}")

# TESTING THE Queue CLASS
print("-------------- TESTING QUEUE --------------")
q = adts.Queue()
print(q.is_empty())
for i in range(10):
    q.enqueue(i+100)
print(f"peek: {q.peek()}")
print(f"dequeue: {q.dequeue()}")
print(f"dequeue: {q.dequeue()}")
print(f"dequeue: {q.dequeue()}")
print(f"is_empty: {q.is_empty()}")
print(f"size: {q.size()}")

# TESTING THE Deque CLASS
print("-------------- TESTING DEQUE --------------")
d = adts.Deque()
print(d.is_empty())
for i in range(5):
    d.add_front(i+100)
for i in range(5):
    d.add_rear(i+200)
print(f"peek: {d.peek()}")
print(f"remove_front: {d.remove_front()}")
print(f"remove_rear: {d.remove_rear()}")
print(f"is_empty: {d.is_empty()}")
print(f"size: {d.size()}")
print(f"peek: {d.peek()}")

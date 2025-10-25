from queue import Queue
q2 = Queue()
q = Queue()

# Add elements
q.put(100)
q.put(200)

# Remove elements
print(q.get())  
print(q.get())  

print(dir(q))
print(q.queue)
print(q.empty())
print(q.full())
print(q.qsize())
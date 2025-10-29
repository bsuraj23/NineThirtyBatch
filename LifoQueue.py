from queue import LifoQueue
obj = LifoQueue()
obj.put('A')
obj.put('B')

print(obj.get())  
print(obj.get())  

obj.put('C')
print(obj.get())  
print("is obj empty",obj.empty())  
print("is obj full",obj.full())   
print("obj size",obj.qsize())  
print("obj max size",obj.maxsize) 
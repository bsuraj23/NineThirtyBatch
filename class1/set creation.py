#set creation
s={1,2,3,4,5,5,5,6,7,8,9,}
print(s)
s1=set([2,3])
print(s1)
s2=set(['apple','banana'])
print(s2)
s3=set(range(5))
print(s3)
s3.add(666)
print(s3)
s = {1, 2}
s.add(3)
print(s)
s.update([4, 5])
print(s)
s.remove(4)
print(s)
s.discard(10)  # no error
print(s)
s.clear()
print(s)
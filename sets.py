


s1=set()
print(s1)

fruits={"apple","banana","cherry"}
print(fruits)

num=set([1,2,3,1,2])
print(num)

#set methods
#add,update
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.add("blue berry")
print(fruits)
fruits.update(["kiwi","pineapple"])
print(fruits)

#removing elements
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.remove("orange")
print(fruits)

#remove
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.remove("banana")
print(fruits)

#discard
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.discard("mango")
print(fruits)

#pop
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.pop()
print(fruits)

#clear
fruits={"apple","banana","mango","orange","cherry","guava","grapes"}
fruits.clear()
print(fruits)

#set operations
a={1,2,3,4,5}
b={3,4,6,7,8}
#union
print(a|b)
print(a.union(b))

a={1,2,3,4,5}
b={3,4,6,7,8}
#intersection
print(a&b)
print(a.intersection(b))

#difference
a={1,2,3,4,5}
b={3,4,6,7,8}
print(a-b)
print(a.difference(b))
print(b-a)

#symmetric difference
a={1,2,3,4,5}
b={3,4,6,7,8}
print(a^b)
print(a.symmetric_difference(b))

#copy
a={1,2,3,4,5}
b={3,4,6,7,8}
c=a.copy()
print(c)
d=b.copy()
print(d)

#superset and sub set
a={1,2,3,4,5}
b={3,4,6,7,8}
print(a.issuperset(b))
print(b.issuperset(a))
print(a.issubset(b))
print(b.issubset(a))

#disjoint
a={1,2,3,4,5}
b={3,4,6,7,8}
print(a.isdisjoint(b))
print(b.isdisjoint(a))
print(a.isdisjoint({7,8}))

#frozenset
fs=frozenset([1,2,3,4,5])
print(fs)

fs1=frozenset(["apple","banana","cherry"])
print(fs1)
=======
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


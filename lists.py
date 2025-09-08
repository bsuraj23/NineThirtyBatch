#list 

li=[]
print(li)
print(type(li))

#indexing
li1=[1,2,3,4,5]
print(li1[0])

fruits=["apple","banana","cherry","orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

li=[1,2,"apple","orange",10,20]
#list methods
#append
li.append(30)
print(li)

#extend
li=[1,2,"apple","orange",10,20]
li.extend([40,50,60])
print(li)

#insert
li=[1,2,"apple","orange",10,20]
li.insert(2,"ammu")
print(li)

#remove
li=[1,2,"apple","orange",10,20]
li.remove(10)
print(li)

#pop
li=[1,2,3,4,5,6]
li.pop()
li.pop(2)
li.pop(3)
print(li)

#clear
li=[1,2,3,4,5,6]
li.clear()
print(li)

#index
li=[1,2,3,4,5,6,2]
print(li.index(2))
print(li.index(2,2))

#count
li=[1,2,"apple","orange",10,20,1,2,1,1,2,10]
print(li.count(1))
print(li.count(2))

#sort
li=[9,8,7,6,5,4,3,2,1]
li.sort()
print(li)

li=[1,2,3,4,5,6]
li.reverse()
print(li)

fruits=["apple","cherry"]
new=fruits.copy()
print(new)
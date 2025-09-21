#Removing duplicates from List 

#using set()

fruits=["apple", "banana", "guava","apple","guava","mango"]
unique=list(set(fruits))
print(unique)


#using dict.fromkeys()

Alphabets=["A","K","H","I","L","A","K","O","L","L","I"]
unique=list(dict.fromkeys(Alphabets))
print(unique)

#using loop

numbers=[1,2,3,1,4,3,6,6]
unique=[]
for i in numbers:
        if i not in unique:
                unique.append(i)
print(unique)

#slicing operations in list and strings
list=[1,2,3,4,5,6,7,8,9,0]
print(list[1:5])
print(list[:6])
print(list[2:])
print(list[::3])
print(list[::-1])


String="Python"
print(String[1:3])
print(String[:4])
print(String[2:])
print(String[::-1])



#enumerate() 
Id=[101,102,103,104]
for index,Id in enumerate(Id,start=1):
        print(index,Id)
        
iterate through dictionary
Student={"name":"Akhila","age":21,"course":"python"}

for key in Student:
        print(key)
for value in Student.values():
        print(value)
for key,value in Student.items():
        print(key,value)
for index,(key,value) in enumerate(Student.items()):
        print(index,key,value)

#list comprehension
nums = [1, 2, 3, 4, 5]
squarednums= [x**2 for x in nums]
print(squarednums)  # [1, 4, 9, 16, 25]

#Removing duplicates from List 

#using set()

fruits=["apple", "banana", "guava","apple","guava","mango"]
unique=list(set(fruits))
print(unique)


#using dict.fromkeys()

Alphabets=["A","K","H","I","L","A","K","O","L","L","I"]
unique=list(dict.fromkeys(Alphabets))
print(unique)

#using loop

numbers=[1,2,3,1,4,3,6,6]
unique=[]
for i in numbers:
        if i not in unique:
                unique.append(i)
print(unique)

#slicing operations in list and strings
list=[1,2,3,4,5,6,7,8,9,0]
print(list[1:5])
print(list[:6])
print(list[2:])
print(list[::3])
print(list[::-1])


String="Python"
print(String[1:3])
print(String[:4])
print(String[2:])
print(String[::-1])



#enumerate() 
Id=[101,102,103,104]
for index,Id in enumerate(Id,start=1):
        print(index,Id)
        
iterate through dictionary
Student={"name":"Akhila","age":21,"course":"python"}

for key in Student:
        print(key)
for value in Student.values():
        print(value)
for key,value in Student.items():
        print(key,value)
for index,(key,value) in enumerate(Student.items()):
        print(index,key,value)

#list comprehension
nums = [1, 2, 3, 4, 5]
squarednums= [x**2 for x in nums]
=======
#Removing duplicates from List 

#using set()

fruits=["apple", "banana", "guava","apple","guava","mango"]
unique=list(set(fruits))
print(unique)


#using dict.fromkeys()

Alphabets=["A","K","H","I","L","A","K","O","L","L","I"]
unique=list(dict.fromkeys(Alphabets))
print(unique)

#using loop

numbers=[1,2,3,1,4,3,6,6]
unique=[]
for i in numbers:
        if i not in unique:
                unique.append(i)
print(unique)

#slicing operations in list and strings
list=[1,2,3,4,5,6,7,8,9,0]
print(list[1:5])
print(list[:6])
print(list[2:])
print(list[::3])
print(list[::-1])


String="Python"
print(String[1:3])
print(String[:4])
print(String[2:])
print(String[::-1])



#enumerate() 
Id=[101,102,103,104]
for index,Id in enumerate(Id,start=1):
        print(index,Id)
        
iterate through dictionary
Student={"name":"Akhila","age":21,"course":"python"}

for key in Student:
        print(key)
for value in Student.values():
        print(value)
for key,value in Student.items():
        print(key,value)
for index,(key,value) in enumerate(Student.items()):
        print(index,key,value)

#list comprehension
nums = [1, 2, 3, 4, 5]
squarednums= [x**2 for x in nums]
print(squarednums)  # [1, 4, 9, 16, 25]

#Removing duplicates from List 

#using set()

fruits=["apple", "banana", "guava","apple","guava","mango"]
unique=list(set(fruits))
print(unique)


#using dict.fromkeys()

Alphabets=["A","K","H","I","L","A","K","O","L","L","I"]
unique=list(dict.fromkeys(Alphabets))
print(unique)

#using loop

numbers=[1,2,3,1,4,3,6,6]
unique=[]
for i in numbers:
        if i not in unique:
                unique.append(i)
print(unique)

#slicing operations in list and strings
list=[1,2,3,4,5,6,7,8,9,0]
print(list[1:5])
print(list[:6])
print(list[2:])
print(list[::3])
print(list[::-1])


String="Python"
print(String[1:3])
print(String[:4])
print(String[2:])
print(String[::-1])



#enumerate() 
Id=[101,102,103,104]
for index,Id in enumerate(Id,start=1):
        print(index,Id)
        
iterate through dictionary
Student={"name":"Akhila","age":21,"course":"python"}

for key in Student:
        print(key)
for value in Student.values():
        print(value)
for key,value in Student.items():
        print(key,value)
for index,(key,value) in enumerate(Student.items()):
        print(index,key,value)

#list comprehension
nums = [1, 2, 3, 4, 5]
squarednums= [x**2 for x in nums]
>>>>>>> e84268f32216806d305d49d007d8050e6d72e80f
print(squarednums)  # [1, 4, 9, 16, 25]
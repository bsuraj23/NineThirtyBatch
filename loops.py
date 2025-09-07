
#  FOR 

# Print squares of numbers from 1 to 10
print("Squares from 1 to 10:")
for i in range(1, 11):
    print(f"{i}² = {i*i}")

# Loop through a list of cities
cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai"]
print("\nList of cities:")
for city in cities:
    print(city)

# Count vowels in a string
text = "Python programming is fun"
vowel_count = 0
for char in text:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"\nVowel count in '{text}':", vowel_count)

# Print all odd numbers between 1 and 50
print("\nOdd numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print()

# WHILE 

# Countdown timer
print("\nCountdown from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1

# Sum of digits of a number
num = 12345
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"\nSum of digits of {num}:", sum_digits)

# Reverse a string using while loop
word = "loop"
reversed_word = ""
index = len(word) - 1
while index >= 0:
    reversed_word += word[index]
    index -= 1
print(f"\nReversed word of '{word}':", reversed_word)

# Print multiplication table of a number
num = 7
i = 1
print(f"\nMultiplication table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1

#loops are for,while
#for loop
n=10
for i in range(1,n):
    print(i)

fruits=["apple","orange","cherry","watermelon"]
for i in fruits:
    print(i)

#prime or not
num=23
if num>1:
    for i in range(2,num):
        if num % i==0:
            print("not a  prime")
            break
    else:
        print("prime")

#length of the list
li=[10,20,30]
count=0
for i in li:
    count+=i
print(count)

#even numbers print
e=20
for i in range(1,101):
    if(i%2==0):
        print(i)


#while loop
i=0
while i<5:
    print(i)
    i+=1
#sum of first 10 natural numbers
i=1
total=0
while i<=10:
    total+=i
    i+=1
    print(total)



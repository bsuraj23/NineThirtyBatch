# Example of input() function in Python

name = input("Enter your name: ")        # Takes input as a string
age = input("Enter your age: ")          # Takes input as a string

print("Hello,", name)
print("You are", age, "years old.")

# If you want to use age as an integer:
age_int = int(age)
print("Next year, you will be", age_int + 1, "years) old.")
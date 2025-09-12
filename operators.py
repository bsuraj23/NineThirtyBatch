# Arithmetic Operators
a = 10  # Assign 10 to variable a
b = 3   # Assign 3 to variable b

sum_result = a + b        # Addition
diff_result = a - b       # Subtraction
prod_result = a * b       # Multiplication
div_result = a / b        # Division (float result)
mod_result = a % b        # Modulus (remainder)
exp_result = a ** b       # Exponentiation (a to the power of b)
floor_div_result = a // b # Floor division (quotient without decimals)

print("Arithmetic Operators:")
print("a + b =", sum_result)           # Prints addition result
print("a - b =", diff_result)          # Prints subtraction result
print("a * b =", prod_result)          # Prints multiplication result
print("a / b =", div_result)           # Prints division result
print("a % b =", mod_result)           # Prints modulus result
print("a ** b =", exp_result)          # Prints exponentiation result
print("a // b =", floor_div_result)    # Prints floor division result

print("\nAssignment Operators:")
x = 5           # Assign 5 to x
x += 2          # Add 2 to x (x = x + 2)
print("x after x += 2:", x)  # Prints 7
x -= 1          # Subtract 1 from x (x = x - 1)
print("x after x -= 1:", x)  # Prints 6
x *= 3          # Multiply x by 3 (x = x * 3)
print("x after x *= 3:", x)  # Prints 18
x /= 2          # Divide x by 2 (x = x / 2)
print("x after x /= 2:", x)  # Prints 9.0
x %= 4          # x = x % 4 (remainder after division by 4)
print("x after x %= 4:", x)  # Prints 1.0

print("\nComparison Operators:")
m = 8
n = 6
print("m == n:", m == n)   # Checks if m is equal to n
print("m != n:", m != n)   # Checks if m is not equal to n
print("m > n:", m > n)     # Checks if m is greater than n
print("m < n:", m < n)     # Checks if m is less than n
print("m >= n:", m >= n)   # Checks if m is greater than or equal to n
print("m <= n:", m <= n)   # Checks if m is less than or equal to n

print("\nLogical Operators:")
p = True
q = False
print("p and q:", p and q)   # True if both p and q are True
print("p or q:", p or q)     # True if either p or q is True
print("not p:", not p)       # True if p is False, otherwise False
#function methods

#square method
def square(n):
    return n * n

print("Square of 2 is", square(2))
print("Square of 12 is", square(12))
  

#repeat_line
def repeat_line(text,times):
    for i in range(times):
        print(text)
repeat_line("kee and srili is besties",5)
print(repeat_line) 


#abs 
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num
print("Absolute value of -4 is", absolute_value(-4))
print("Absolute value of 5 is", absolute_value(5))

#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is", factorial(5))
print("Factorial of 0 is", factorial(0))

#fibonacci
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
print("Fibonacci of 7 is", fibonacci(7))
print("Fibonacci of 10 is", fibonacci(10))

#gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
print("GCD of 48 and 18 is", gcd(48, 18))
print("GCD of 56 and 98 is", gcd(56, 98))




def factorial(n):
    if n<0:
        raise ValueError("Factorial Is Not Defined For Negative Numbers")
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
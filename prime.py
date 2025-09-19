def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    if num == 2:
        return True   # 2 is the only even prime number
    if num % 2 == 0:
        return False  # other even numbers are not prime

    # Check from 3 to sqrt(num), skipping even numbers
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Test it
number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
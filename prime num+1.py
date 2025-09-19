def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    # Check for divisors from 2 up to the square root of n
    # This optimization reduces the number of checks needed
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it is prime

# Example usage:
number_to_check = 17
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

number_to_check = 25
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
    #oghuiugiurg4
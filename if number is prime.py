# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check till sqrt(n)
        if n % i == 0:
            return False
    return True

# Example
num = 19
print("Number:", num)
print("Is prime?", is_prime(num))
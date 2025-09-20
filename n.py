def primes_upto_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # check up to √num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(primes_upto_n(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

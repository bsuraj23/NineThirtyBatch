def prime_numbers_up_to_n(n):
    prime_numbers=[]
    for num in range(2,n+1):
        is_prime=True
        i=2
        while i * i <= num:
            if num % i==0:
                is_prime=False
                break
            i=i+1
        if is_prime:
              prime_numbers.append(num)
    return prime_numbers
print(prime_numbers_up_to_n(50))
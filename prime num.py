def is_prime(n):
    if n <= 1:
        return False 
    if n == 2:
        return True
    if n % 2 == 0:
        for i in range (3, int (n ** 0.5)+1,2):
            if n % i == 0:
                return False
            return True
        num + int(input("Enter a number :"))
        print(num,"is a prime number :")
    else:
        print(num ,"is not a prime number ") 
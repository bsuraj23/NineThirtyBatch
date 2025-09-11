#check if the number is prime

import math

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "not a prime numberr")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(num, "not a prime number")
            break
    else:
        print(num, " it is a prime number")
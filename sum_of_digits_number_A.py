def sum_of_digits(num):
    num=abs(num)
    total=0
    while num>0:
        total=total+num%10
        num=num//10
    return total
print(sum_of_digits(145737))
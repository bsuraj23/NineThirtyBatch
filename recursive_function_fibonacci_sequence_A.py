def fib(num):
    if num<0:
        raise ValueError("num must be non negative")
    if num==0:
        return 0
    if num==1:
        return 1
    return fib(num-1)+fib(num-2)
for i in range(11):
    print(fib(i),end=' ')
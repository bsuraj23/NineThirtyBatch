def fibonacci_sequence(n):
    if n<=0:
        return
    a,b=0,1
    print(a,end=' ')
    print(b,end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a,b=b,c
fibonacci_sequence(7)
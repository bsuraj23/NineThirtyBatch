num=int(input("Enter a Number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"IS NOT PRIME")
            break
    else:
        print(num,"IS PRIME")
else:
    print("IS NOT PRIME")
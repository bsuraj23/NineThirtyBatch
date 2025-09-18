a=78
try:
    lst = [1, 2, 3]
    print(lst[6])
    num = int(input("Please enter a interger "))
    c= a/num
    print(c)
except IndexError:
    print("Index out of range please check what your trying to access")



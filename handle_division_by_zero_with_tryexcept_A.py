def division(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("!cannot divide by 0!")
        return None
    else:
        return result
print(division(8,2))
print(division(17,0))
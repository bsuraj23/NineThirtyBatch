try:
    d = {"a": 1}
    print(d["a"])
    
    print("I amm after line 3 ")

except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Division by zero error")
except KeyError:
    print("Key not found which your trying to access ")
finally:
    print("Execution completed.I am finally block")   

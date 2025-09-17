try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero error line 4")

   
def add():
    try:
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        print("Addition is ", a + b)    
    except ValueError:
        print("Invalid input, please enter numeric values.") 




a=90
try:
    a=90
    b= int(input("enter b value  "))
    c=a/b
    print("Result is ",c)

except ValueError:
    print("Invalid input, please enter a valid number. Please take care")
except ZeroDivisionError:
    print("Invalid input, please enter a positive and non zero  number. Please take care")
except Exception as e:
    print("An unexpected error occurred:", e)   
finally:  
    print("Execution completed. and this will surely be executed ")
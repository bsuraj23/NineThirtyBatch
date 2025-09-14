# type() function is used to find the data type of a value or variable

a = 10            # Integer value
print(type(a))    # <class 'int'> → shows that 'a' is an integer

b = 10.5          # Floating-point value
print(type(b))    # <class 'float'> → shows that 'b' is a float

c = "Hello"       # String value
print(type(c))    # <class 'str'> → shows that 'c' is a string

d = True          # Boolean value
print(type(d))    # <class 'bool'> → shows that 'd' is a boolean

e = None          # NoneType value (represents nothing)
print(type(e))    # <class 'NoneType'> → shows that 'e' is None

f = [1, 2, 3]     # List value
print(type(f))    # <class 'list'> → shows that 'f' is a list

g = (1, 2, 3)     # Tuple value
print(type(g))    # <class 'tuple'> → shows that 'g' is a tuple

h = {1, 2, 3}     # Set value
print(type(h))    # <class 'set'> → shows that 'h' is a set

i = {"a": 1, "b": 2} # Dictionary value
print(type(i))       # <class 'dict'> → shows that 'i' is a dictionary

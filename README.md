1. What are Python’s key features? Why is it called an interpreted language?

Key Features:

Easy syntax, dynamically typed.

Cross-platform, open-source.

Rich standard library.

Supports OOP and functional programming.

Automatic memory management (garbage collection).

Interpreted: Python code is executed line by line by the Python interpreter (no separate compilation step).

2. Difference between Python 2 and Python 3?

Print:

Python 2 → print "Hello"

Python 3 → print("Hello")

Division:

Python 2 → 5/2 = 2 (integer division)

Python 3 → 5/2 = 2.5 (true division)

Unicode: Strings are Unicode by default in Python 3.

✅ Python 2 is outdated, Python 3 is the standard.

3. Explain indentation in Python. What happens if it’s incorrect?

Python uses indentation (spaces/tabs) to define code blocks instead of {} or begin/end.

if True:
    print("Valid block")


❌ If incorrect:

if True:
print("Error")   # IndentationError

4. What are Python keywords? Can you use them as variable names?

Keywords: Reserved words with predefined meaning (e.g., if, for, while, class, def).

You cannot use them as variable names.

import keyword
print(keyword.kwlist)  # List of Python keywords

5. Difference between list, tuple, set, and dictionary.
Type	Ordered	Mutable	Duplicates	Example
List	✅ Yes	✅ Yes	✅ Allowed	[1, 2, 3]
Tuple	✅ Yes	❌ No	✅ Allowed	(1, 2, 3)
Set	❌ No	✅ Yes	❌ Unique	{1, 2, 3}
Dict	✅ Yes (3.7+)	✅ Yes	Keys unique	{"a":1, "b":2}
6. Difference between mutable and immutable data types?

Mutable: Can be changed after creation (list, dict, set).

Immutable: Cannot be changed (int, str, tuple).

x = "hello"
x[0] = "H"   # ❌ Error → strings are immutable

lst = [1,2,3]
lst[0] = 100  # ✅ Works → lists are mutable

7. Explain == vs is operator.

== → compares values.

is → compares memory identity (same object).

a = [1,2,3]
b = [1,2,3]
print(a == b)  # True (values equal)
print(a is b)  # False (different objects in memory)

8. Difference between append() vs extend() in lists?

append(x) → adds element as a single item.

extend(iterable) → adds each element individually.

lst = [1, 2]
lst.append([3, 4])   # [1, 2, [3, 4]]
lst.extend([3, 4])   # [1, 2, 3, 4]

9. Shallow copy vs deep copy.

Shallow copy: Copies references of objects → nested objects still linked.

Deep copy: Full independent copy (including nested objects).

import copy
a = [[1,2],[3,4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)


shallow[0][0] = 99 → affects a.

deep[0][0] = 99 → does NOT affect a.

10. How does Python handle memory management (Garbage collection)?

Python uses:

Reference counting (track number of references).

Garbage collector for cyclic references (gc module).

import gc
print(gc.get_threshold())  # shows GC thresholds

🔹 Intermediate Level (OOPs, Functions, Advanced Data Types)
1. What are functions in Python? Difference between *args and **kwargs?

Function: Block of reusable code, defined using def.

*args → variable positional arguments (tuple).

**kwargs → variable keyword arguments (dict).

def demo(a, *args, **kwargs):
    print(a)          # first argument
    print(args)       # tuple
    print(kwargs)     # dict

demo(10, 20, 30, x=1, y=2)
# a=10, args=(20,30), kwargs={'x':1, 'y':2}

2. Explain decorators in Python with an example.

Decorator: Function that modifies another function, often for logging, authentication, etc.

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

3. What are generators and the yield keyword?

Generator: Function that returns an iterator using yield.

More memory-efficient than returning a list.

def gen():
    for i in range(3):
        yield i

for x in gen():
    print(x)   # 0, 1, 2

4. Difference between iterable, iterator, and generator.

Iterable: Any object usable in a loop (list, str, tuple).

Iterator: Object with __iter__() and __next__() methods.

Generator: Special iterator created with yield.

lst = [1,2,3]
it = iter(lst)   # iterator
print(next(it))  # 1

5. Explain list comprehension with an example.

Compact way to create lists.

squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

6. Difference between classmethod, staticmethod, and instance method.

Instance method: Default, takes self.

Class method: Uses @classmethod, takes cls.

Static method: Uses @staticmethod, takes neither self nor cls.

class Demo:
    def instance_method(self): print("instance")
    @classmethod
    def class_method(cls): print("class")
    @staticmethod
    def static_method(): print("static")

7. Explain OOP concepts: inheritance, polymorphism, encapsulation.

Inheritance: Child class inherits from parent.

Polymorphism: Same function name, different behavior.

Encapsulation: Hiding internal details (private variables).

class Animal: 
    def speak(self): print("Generic sound")
class Dog(Animal): 
    def speak(self): print("Woof!")

8. What are magic/dunder methods? Examples.

Special methods with __double_underscores__.

Used for operator overloading, object behavior.

class Book:
    def __init__(self, name): self.name = name
    def __str__(self): return f"Book: {self.name}"

b = Book("Python")
print(b)   # Calls __str__

9. Explain Python’s Global Interpreter Lock (GIL). Why is it important?

GIL: A mutex that allows only one thread to execute Python bytecode at a time.

Needed because of Python’s memory management.

Good for I/O-bound tasks, but limits CPU-bound multi-threading.

10. Difference between deepcopy vs copy.copy().

copy.copy() → shallow copy (copies references).

copy.deepcopy() → full independent copy.

import copy
a = [[1,2],[3,4]]
b = copy.copy(a)      # shallow
c = copy.deepcopy(a)  # deep



🔹 Data Handling & Error Management
1. Explain try, except, finally, else in Python.

try: Code block to test.

except: Handles exceptions.

else: Runs if no exception occurs.

finally: Always runs (cleanup code).

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("No error, result =", x)
finally:
    print("This always executes")

2. What are custom exceptions? How do you create one?

You can define your own exceptions by inheriting from Exception.

class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except MyError as e:
    print(e)

3. Explain with statement and context managers in Python.

with statement ensures proper resource management (auto-close files, release locks).

Context manager implements __enter__ and __exit__.

# Using with
with open("test.txt", "w") as f:
    f.write("Hello")

# Custom context manager
class MyContext:
    def __enter__(self): print("Enter"); return self
    def __exit__(self, exc_type, exc_val, exc_tb): print("Exit")

with MyContext():
    print("Inside block")

4. What are lambda functions? Example with map, filter, reduce.

Lambda: Anonymous one-line function.

from functools import reduce

nums = [1, 2, 3, 4]

print(list(map(lambda x: x*2, nums)))      # [2,4,6,8]
print(list(filter(lambda x: x%2==0, nums))) # [2,4]
print(reduce(lambda a,b: a+b, nums))        # 10

5. Difference between isinstance() vs type().

type(obj) → exact type (does not check inheritance).

isinstance(obj, Class) → checks type and inheritance.

class A: pass
class B(A): pass

b = B()
print(type(b) == A)        # False
print(isinstance(b, A))    # True (because B inherits A)

🔹 Modules & Intermediate Concepts
1. Difference between module and package in Python.

Module → A single Python file (.py).

Package → A collection of modules in a directory with an __init__.py file.

# module: math_utils.py
def add(a,b): return a+b

# package structure:
# mypkg/
#   __init__.py
#   module1.py
#   module2.py

2. What are Python namespaces and scope (LEGB rule)?

Namespace: Mapping of names → objects.

Scopes follow LEGB rule:

Local → inside function

Enclosing → in nested functions

Global → module-level

Built-in → default Python names

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # Local wins
    inner()

outer()

3. Explain import vs from-import.

import module → import whole module.

from module import func → import specific items.

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

4. What is a virtual environment (venv) in Python? Why is it needed?

Virtual environment: Isolated Python environment for a project.

Prevents dependency conflicts.

python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows

5. Difference between shallow copy, deep copy, and assignment operator.

= → Assignment → both variables refer to the same object.

copy.copy() → Shallow copy → copies outer object, references inner ones.

copy.deepcopy() → Full independent clone.

import copy
a = [[1,2],[3,4]]
b = a               # assignment
c = copy.copy(a)    # shallow
d = copy.deepcopy(a) # deep

6. Explain how JSON is handled in Python (json module).

Use json module to serialize (dump) and deserialize (load).

import json

data = {"name":"Alice","age":25}

# Python → JSON
json_str = json.dumps(data)
print(json_str)  # {"name": "Alice", "age": 25}

# JSON → Python
obj = json.loads(json_str)
print(obj["name"])  # Alice

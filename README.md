my theory answers for today's questions
## Frequently Asked Questions (Python)

### 1. What are variables in Python?

**Answer:**  
In Python, variables are used to store data values. You do not need to declare the type of a variable explicitly; Python automatically assigns the data type based on the value you provide. Variable names should start with a letter or an underscore and are case-sensitive. For example, you can create variables to store numbers, text, or other data.

---

### 2. How do you take user input in Python?

**Answer:**  
In Python, you can take user input using the `input()` function. This function waits for the user to type something and press Enter, then returns the input as a string. You can store this input in a variable for further use in your program.

---

### 3. What are data types in Python? Give some examples.

**Answer:**  
Data types in Python represent the kind of value a variable holds. Common Python data types include:
- `int` for whole numbers (e.g., 10)
- `float` for decimal numbers (e.g., 3.14)
- `str` for text (e.g., "hello")
- `bool` for boolean values (True or False)
Python automatically determines the data type based on the value assigned to a variable.

---

### 4. How do you convert user input to an integer in Python?

**Answer:**  
Since the `input()` function always returns a string, you can convert user input to an integer using the `int()` function. This allows you to perform mathematical operations on the user's input if it represents a number.

---

#INTERVIEW QUESTIONS
## 🔹 Python Interview Questions (Beginner Level)

### 1. What are Python’s key features? Why is it called an interpreted language?
Python is easy to read and write, dynamically typed, cross-platform, and has a large standard library. It supports multiple programming styles like object-oriented and functional programming. Python is called interpreted because its code is executed line by line at runtime by an interpreter, not compiled beforehand.

### 2. Difference between Python 2 and Python 3
Python 3 is the modern version and is not backward compatible with Python 2. Key differences include syntax for print statements, division behavior, and Unicode handling. Python 2 is no longer supported by the community.

### 3. Explain indentation in Python. What happens if indentation is incorrect?
Indentation is used to define code blocks in Python. If indentation is missing or inconsistent, Python raises an error and the program will not run.

### 4. What are Python keywords? Can you use them as variable names?
Python keywords are reserved words that have special meaning in the language (like `if`, `for`, `while`). They cannot be used as variable names.

### 5. Difference between list, tuple, set, and dictionary. Give examples.
- List: Ordered, changeable (mutable), allows duplicate elements.
- Tuple: Ordered, unchangeable (immutable), allows duplicate elements.
- Set: Unordered, changeable, contains only unique elements.
- Dictionary: Unordered (insertion order preserved since Python 3.7), stores data as key-value pairs.

### 6. What is the difference between mutable and immutable data types?
Mutable data types can be changed after creation (like lists and dictionaries). Immutable data types cannot be changed after creation (like integers, strings, and tuples).

### 7. Explain == vs is operator in Python.
`==` checks if the values of two variables are equal, while `is` checks if two variables refer to the exact same object in memory.

### 8. What is the difference between append() vs extend() in lists?
`append()` adds a single element to the end of the list. `extend()` adds each element from another iterable (like another list) to the end of the list.

### 9. Explain shallow copy vs deep copy in Python.
A shallow copy creates a new object but does not create copies of nested objects; they are still referenced. A deep copy creates a new object and also recursively copies all nested objects, making them completely independent.

### 10. How does Python handle memory management (Garbage collection)?
Python handles memory management automatically using reference counting and a built-in garbage collector that removes objects that are no longer needed to free up memory.

#INTERMEDIATE LEVEL (OOPS,Functions,Advanced Data Types)

1. What are functions in Python? Difference between *args and **kwargs?

Functions are reusable blocks of code that perform a specific task when called.
*args allows you to pass a variable number of positional arguments to a function.
**kwargs allows you to pass a variable number of keyword (named) arguments.

2. Explain decorators in Python.

Decorators are a way to modify or enhance the behavior of functions or methods without changing their code. They "wrap" another function, adding extra functionality before or after the original function runs.

3. What are generators and yield?

Generators are special functions that return an iterator, yielding values one at a time as you iterate over them, rather than returning everything at once.
The yield keyword is used to produce a value and pause the function, resuming where it left off on the next call.

4. Difference between iterable, iterator, and generator.

Iterable: Any object you can loop over (like a list or a string).
Iterator: An object that keeps state and produces the next value when you call next() on it.
Generator: A type of iterator created by a generator function, which uses yield to produce values.

5. Explain list comprehension.

List comprehension is a concise way to create lists based on existing lists, applying an expression or filter to each item.

6. Difference between classmethod, staticmethod, and instance method.

Instance method: Belongs to an object; can access and modify object state.
Class method: Belongs to the class, not an object; can access or modify class state.
Static method: Doesn’t access or modify class or object state; it’s just grouped with the class for convenience.

7. Explain Python’s OOP concepts: inheritance, polymorphism, encapsulation.

Inheritance: One class can inherit traits and behavior from another class.
Polymorphism: Different classes can have methods with the same name, and the correct one is called depending on the object.
Encapsulation: Hiding internal details and showing only necessary features.

8. What are magic/dunder methods? Examples: __str__, __init__.

Magic methods (also called dunder methods) are special methods with double underscores before and after their names, used to define how objects behave (like initialization, string conversion, etc.).

9. Explain Python’s Global Interpreter Lock (GIL).

The GIL is a mechanism that allows only one thread to execute Python bytecode at a time, which affects the performance of multi-threaded programs in CPython.

10. Difference between deepcopy vs copy.copy() in Python.

copy.copy() makes a shallow copy (copies the object, but not nested objects).
copy.deepcopy() makes a deep copy (copies the object and all nested objects recursively).

#Data Handling & Error Management
1. Explain try, except, finally, else in Python.

try → Used to write the code that may raise an error.

except → Handles the error if it occurs.

else → Executes only if no error occurs inside try block.

finally → Always executes, whether an error occurs or not (used for cleanup like closing files).

2. What are custom exceptions? How do you create one?

Custom exceptions are user-defined exceptions.

They are used when built-in exceptions are not enough.

We create them by making a new class that inherits from the Exception class.

3. Explain with statement and context managers in Python.

The with statement simplifies resource management like handling files, database connections, and locks.

It ensures that resources are properly closed or released, even if errors occur.

A context manager defines how to acquire a resource (setup) and how to release it (cleanup).

4. What are lambda functions? Give an example with map, filter, reduce.

Lambda functions are small anonymous functions defined without using def.

They are written in one line using the syntax lambda arguments: expression.

map → Applies a function to all elements in a sequence.

filter → Filters elements based on a condition.

reduce → Reduces a sequence into a single value by repeatedly applying a function.

5. Difference between isinstance() vs type().

type(obj) → Returns the exact type of an object. It does not consider inheritance.

isinstance(obj, class) → Checks whether an object is an instance of a class or its subclass.

Use type() for exact type checking.

Use isinstance() when subclass relationships should be considered.

#Modules & Intermediate Concepts
1. Difference between module and package in Python.

A module is a single Python file (.py) that contains functions, classes, or variables.

A package is a collection of multiple modules organized in a directory with an __init__.py file.

Module = single file, Package = folder of modules.

2. What are Python namespaces and scope (LEGB rule)?

A namespace is a mapping between names and objects (like a dictionary of variable names and values).

Scope decides where a variable can be accessed.

Python follows the LEGB rule:

L (Local) → Names inside the current function.

E (Enclosing) → Names in outer functions (when functions are nested).

G (Global) → Names defined at the top level of the script/module.

B (Built-in) → Predefined names in Python (like len, print).

3. Explain import vs from-import.

import module → Brings the whole module, and we access functions/classes with module.name.

from module import name → Imports only specific functions or classes directly, so we can use them without prefix.

import keeps namespace cleaner, while from-import gives direct access.

4. What is virtual environment (venv) in Python? Why is it needed?

A virtual environment (venv) is an isolated environment for Python projects.

It has its own Python interpreter and dependencies, separate from the system-wide installation.

Needed because:

Prevents conflicts between packages of different projects.

Helps maintain project-specific dependencies.

Ensures reproducibility of the project environment.

5. Difference between shallow copy, deep copy, assignment operator.

Assignment (=) → Creates a new reference to the same object (no copy made).

Shallow copy → Creates a new object but only copies references of nested objects (changes in inner objects affect both copies).

Deep copy → Creates a completely independent copy, including all nested objects (changes don’t affect the original).

6. Explain how JSON is handled in Python (json module).

Python has a built-in json module for working with JSON data.

Converting Python → JSON: json.dumps()

Converting JSON → Python: json.loads()

Working with files:

json.dump() → Write JSON data to a file.

json.load() → Read JSON data from a file.

Used for data exchange in APIs, web apps, and configuration files.








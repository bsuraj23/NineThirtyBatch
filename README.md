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
Yes, in Python, you can change the value stored in a variable at any time by assigning a new value to it. The variable will then hold the new value, regardless of its previous value or data type.

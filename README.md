 1. What are Python’s key features? Why is it called an interpreted language?
Key Features of Python:
Easy to Read & Write: Simple syntax, close to natural language.

Interpreted Language: No need for compilation; code runs line by line.

Dynamically Typed: No need to declare variable types.

Extensive Libraries: Rich standard library and external packages.

Cross-platform: Runs on Windows, macOS, Linux.

Object-Oriented & Procedural: Supports both paradigms.

Automatic Memory Management: Manages memory automatically (via Garbage Collection).

Why Interpreted?
Python is called an interpreted language because the Python code is executed line by line by the Python interpreter at runtime, without needing a separate compilation step into machine code.

✅ 2. Difference between Python 2 and Python 3
Feature	Python 2	Python 3
Print Statement	print "Hello"	print("Hello") (Function)
Integer Division	5 / 2 → 2	5 / 2 → 2.5
Unicode Support	ASCII by default	Unicode by default
xrange()	Exists	Removed (use range())
Maintenance	End-of-life (2020)	Actively maintained
✅ 3. Explain indentation in Python. What happens if indentation is incorrect?
Indentation defines code blocks in Python (unlike braces {} in other languages).

if True:
    print("Indented block")
If indentation is incorrect, Python raises an IndentationError:

if True:
print("Wrong indentation")  # IndentationError
Indentation improves code readability and enforces clean structure.

✅ 4. What are Python keywords? Can you use them as variable names?
Keywords: Reserved words that have special meaning in Python (e.g., if, else, for, class, def, import).

You cannot use keywords as variable names.

import keyword
print(keyword.kwlist)  # List all keywords

# Invalid:
if = 5  # SyntaxError
✅ 5. Difference between list, tuple, set, and dictionary with examples
Data Type	Mutable	Ordered	Example
List	✅ Yes	✅ Yes	[1, 2, 3]
Tuple	❌ No	✅ Yes	(1, 2, 3)
Set	✅ Yes	❌ No (unordered, unique)	{1, 2, 3}
Dictionary	✅ Yes	✅ Yes (since Python 3.7)	{'a': 1, 'b': 2}
List: Allows duplicates, changeable, ordered.

Tuple: Immutable, ordered.

Set: Unordered, no duplicates.

Dictionary: Key-value pairs, keys unique.

✅ 6. What is the difference between mutable and immutable data types?
Mutable	Immutable
Can be changed after creation	Cannot be changed after creation
Example: list, set, dict	Example: int, float, tuple, str
lst = [1, 2, 3]
lst[0] = 5  # Allowed

tup = (1, 2, 3)
tup[0] = 5  # TypeError
✅ 7. Explain == vs is operator in Python with examples
==: Compares values of objects.

is: Compares identity (whether both refer to the same object in memory).

a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True (same content)
a is b  # False (different objects)

c = a
a is c  # True
✅ 8. What is the difference between append() vs extend() in lists?
append(): Adds a single element at the end.

extend(): Adds all elements from an iterable.

lst = [1, 2]
lst.append([3, 4])
# lst = [1, 2, [3, 4]]

lst = [1, 2]
lst.extend([3, 4])
# lst = [1, 2, 3, 4]
✅ 9. Explain shallow copy vs deep copy in Python
Shallow Copy: Copies the object, but nested objects remain references.

import copy
lst1 = [[1, 2], [3, 4]]
shallow = copy.copy(lst1)
shallow[0][0] = 100
print(lst1)  # [[100, 2], [3, 4]]
Deep Copy: Copies the object and all nested objects recursively.

deep = copy.deepcopy(lst1)
deep[0][0] = 999
print(lst1)  # [[100, 2], [3, 4]]
✅ 10. How does Python handle memory management (Garbage collection)?
Python uses automatic memory management and garbage collection (GC) to reclaim unused memory.

Based on reference counting and generational GC:

Objects are destroyed when reference count becomes 0.

GC periodically checks for reference cycles that reference counting alone cannot handle.

import gc
gc.collect()  # Forces garbage collection



what is invalidate cache?
ans)invalidate cache means clearing the stored data to fetch new results

how can you print all the attributes of functions or class
ans)Use dir(object) to list all attributes and methods of a function or class.  
For example: print(dir(MyClass)) or print(dir(my_function)).
 

Python Basics & Core Concepts (Beginner Level)

1. What are Python’s key features? Why is it called an interpreted language?
Python is easy to read and write, works on many platforms, and supports different styles of coding. It’s called interpreted because it runs code line by line, not all at once like compiled languages.

 2. Difference between Python 2 and Python 3?
 Python 3 handles text better because it uses Unicode by default, while Python 2 uses ASCII, which can cause issues with non-English characters. Also, many new features like f-strings, better error handling, and cleaner syntax are only available in Python 3, making it the recommended version for all new projects.

3. Explain indentation in Python. What happens if indentation is incorrect?
Indentation means using spaces to show which lines of code belong together. If it’s wrong, Python gives an error and won’t run the code.

4. What are Python keywords? Can you use them as variable names?
Keywords are special words like if, for, True, etc. You can’t use them as variable names because Python already uses them for specific tasks.

5. Difference between list, tuple, set, and dictionary. Give examples
- List is a collection that allows you to store multiple items in a specific order. You can change the items (it's mutable), and it allows duplicates. For example, [1, 2, 2, 3] is a valid list. Lists preserve the order and values exactly as you add them.
- Tuple is similar to a list, but you cannot change its contents once it's created (it's immutable). It also keeps the order and allows duplicates. For example, (1, 2, 2, 3) is a tuple. Tuples are useful when you want to protect data from being modified.
- Set is a collection of unique items. It does not preserve order, and it automatically removes duplicates. For example, {1, 2, 2, 3} becomes {1, 2, 3}. Sets are great when you want to filter out repeated values.
- Dictionary stores data in key-value pairs, like a mini database. It keeps the order (in Python 3.7 and above), and each key must be unique. For example, {"name": "Hameed", "age": 21} is a dictionary. You can quickly look up values using their keys.

6. What is the difference between mutable and immutable data types?
Mutable means you can change the value (like lists). Immutable means you can’t change it (like strings and tuples).

7. Explain == vs 'is' operator in Python with examples.
- == checks if values are the same → 5 == 5 is True
- 'is' checks if they are the same object in memory → a is b

8. What is the difference between append() vs extend() in lists?
- append() adds one item → list.append(4) → [1, 2, 3, 4]
- extend() adds multiple items → list.extend([5, 6]) → [1, 2, 3, 4, 5, 6]

9. Explain shallow copy vs deep copy in Python.
- Shallow copy copies only the outer part.
- Deep copy copies everything, even inside nested objects.

10. How does Python handle memory management (Garbage collection)?
Python manages memory automatically using a system called reference counting and a built-in garbage collector. Reference counting means Python keeps track of how many variables or objects are pointing to a particular value. Every time you assign or use an object, its reference count goes up, and when it's no longer needed, the count goes down. If the count reaches zero, Python knows the object isn’t being used anymore and deletes it from memory. For cases where objects refer to each other (like circular references), Python uses a garbage collector to clean them up and free memory. This way, developers don’t have to manually manage memory — Python does it behind the scenes.






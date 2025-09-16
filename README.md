features of python and why it is called interpreted language ?
1.potable 2.dynamically typed 3.interpreted langauge 4.object oriented 5.easy to learn
the code is executed line by line by a interpreter ,without producing a saperate machine code ,so it called interpreted language

intendation?
spaces at the beginning of line in code.in python,indentation is mandatory because it defines block of code.
incorrect intendation is refers to intendation error or logical error

python keywords and can we use keywords as variables ?
in python keywords are reserved words are used to define the syntax and structure.if,else,for,while,etc
no we cannot use keywords as variables because python will throw syntax error.

What is the difference between mutable and immutable data types? Ans.Mutable datatypes that can be modified or changed after the creation Ex:list,set,dictionary Immutable datatypes that cannot be modified after the creation Ex:int,string,tuple

Explain == vs is operator in Python with examples? Ans."==" is the equality operator it checks whether the values of two objects are equal. "is" is the identity operator it checks whether two names (variables) refers to the exact same object in memory.

What is the difference between append() vs extend() in lists? Ans.list.append(x) adds its argument x as a single element to the end of the list. list.extend(iterable) takes an iterable like another list, tuple, string and adds each element.

Explain shallow copy vs deep copy in Python? Ans.Shallow copy: creates a new container/object, but does not copy the nested (inner) objects. It just copies references to the inner objects. So the outer object is a separate object, but the inner ones are shared between original and copy. Deep copy: creates a new container/object and recursively copies all objects found in the original. So neither the outer nor any inner/mutable parts are shared. The copy is fully independent.

How does Python handle memory management (Garbage collection)? Ans.Memory management refers to how Python allocates memory to objects, how it keeps track of what can be used and what can be freed, and how it reclaims unused memory. Python makes most of this automatic so you usually don’t need to manually free memory (unlike in C).

What are Python’s built-in data types? Ans.int,float,complex,string,list,tuple,range,dict,set,frozenset,boolean,None

How are integers and floats stored in memory in Python? Ans.Integers in Python are stored as arbitrary‑precision objects (with a header + an array of “digits”), growing in size as needed,but Floats are stored as 64‑bit IEEE‑754 double‑precision values inside a Python object with metadata.


16/09/2025
self? self is the convention used within class definition used to refer to the instance of class itself.

static variable? the variable that belongs to the class,not to the specific object
instance variable? unique for each object
local variable? variable that declared inside the function and can only be accessed with in that function





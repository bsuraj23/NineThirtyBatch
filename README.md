# NineThirtyBatch
Tasks(30 july 2025)

1Q. What is the history of python ?
*creater of python is "Guido van rossum", he was named the programming language as python from british comedy group "Monty Python's Flying Circus" and it was started in 1989.

2Q.What is the famous web application develpoed using python ?
* Instagram is the famous web application.
  
3Q.What is compilation ?
* In python, compilation means converting .py file into bytecode(.pyc) ,then executed by python interpreter.

(05 Aug 2025)

4Q. find any 5 commands to implement in the command prompt ?
-ipconfig:Displays your computer's IP address and network details , and also used to reset your password.
-Ping:Tests connectivity to another network device or website.
-cd(change directory):Navigates between folders in CMD.
-dir:Lists files and folders in the current directory.
-cls:Clear the command prompt screen.

5Q.What are the features of python ?
* Easy to learn and use.
* Large standard library.
* Supports multiple paradiagrams.
* open source.
* Interpreted language.
  
6Q. Is the 'char' exist in python or not ?
There is no separate 'char' in python, a character in python is just a string of length 1.

(13 Aug 2025)

7Q. Difference between compilation and interpreter ?
Here, firstly compilation converts the code into intermediate level and then the interpreter will run the code.and finally it gives the output.

8Q. understand about vs code and the shortcuts ?
It is free, lightweight, cross-platform code editor made by microsoft, and it supports many programming languages through extensions.

9Q.find the difference between single(=) and double (==) equal ?
= stores a value in a variable ,
== comparision operator.

(14 Aug 2025)

10Q.find the difference between break and continue ?
Break: It will break the condition ,when it reaches the given condition and then if there is next loop then it will goes to another loop.
Continue: It just skip the condition/iteration and continues next iteration of the loop.

11Q. What are conversion specifiers and their use ?
Conversion specifiers are special symbols(place holders) used inside strings to format values when you use the % operator.
Example:
* %d and %i are for integers
* %f for float
* %s for string
* %c for single character

(18 Aug 2025)

12Q. What is HTTP and HTTPS ?
HTTP(HyperText Transfer Protocal):
* HTTP is the protocal(set of rules) used by web browsers and servers to communicate.
* It sends data in plain text but, its not secure.
* here, anyone like hacker can intercept and read your data.
* It works on port 80 by default.
HTTPS(HyperText Transfer Protocal Secure):
* It is the secured version of HTTP.
* It uses SSL/TLS encrypted to protect communication between browser and server, so any hackers cannot read it.
* used for baning, payments, login pages, personal info..
* It works on port 443 by default.
* shows a padlock symbol in the browser.

(19 Aug 2025)

13Q. Difference between List and Set ?
LIST:
* An ordered collection of items.
* It allows duplicates and preserves insertion order.
* Supports indexing & slicing (list[0], list[1:3]).

SET:
* An unordered collection of unique items.
* It not allows duplicates and does not preserves order.
* Not supports.

14Q. Difference between remove() and discard() ?
remove() :Removes a specific element from a set and raises a key error.
discard() :Removes a specific element from a set and doesn't raises any error.

(25 Aug 2025)

15Q. Is the tuple mutable or not ?
* Tuple is immutable that means if we create a tuple then we can't change its elements.But, if a tuple contains mutable objects like lists or dictionaries then we can modify those contents.

(26 Aug 2025)

16Q. What is RAG ?
RAG is a method where a language model (like GPT) is combined with an external retriever system that fetches relevant documents, facts, or data before generating an answer. This helps the model give more accurate, up-to-date, and context-specific responses.

(28 Aug 2025)

17Q. What is the difference between single(')and double(") quotes?
If your string contains a single quote ', use double quotes " ". If your string contains a double quote ", use single quotes ' '. If your string contains both ' and ", you can Use escape characters with \ or we can triple codes ex: """ hello it's "rainy" today""".

(29 Aug 2025)

18Q. What is the use of 'Self' keyword?
If we declare the 'self' keyword in the local of a function then we can use those parameters at both local and global variables.

19Q.How can we restart the vs code by using cache?
VS Code can be restarted and cache cleared to fix performance issues by manually removing cache files or using built-in commands.
* Manual cache deletion
* Terminal commands (Mac/Linux)
* Clear Extension Cache
* Clear Workspace Storage & Editor History

20Q. How can we print all the attributes of a function or class?
All the attributes of a function or class in Python can be printed using tools like :
* dir():Returns a list of all attribute and method names
* __dict__:Provides a dictionary of an object's or class's namespace
* vars():Equivalent to accessing __dict__, but more portable.

21Q. how can we check the processing power percentage using the python code?
The processing power percentage (CPU usage) in Python can be checked using the psutil library, which provides a simple and cross-platform way to retrieve real-time CPU statistics.
* No special permissions are required to run this code, and it works on Windows, macOS, and Linux.
* psutil.cpu_percent() can be called without arguments for instant usage, but accuracy improves with an interval.
* This code reports the total (or per-core) processing power usage as a percentage, which helps monitor system load in real time.

(1 Sep 2025)

22Q.how to implement the global variable in the end of the function?
A global variable in Python can be modified inside a function by declaring it with the global keyword.
* Declare the global variable outside the function
* Use the global keyword inside the function before assignment
* You can place global variable_name at the end of the function before you assign or modify the variable, but it must come before any usage of      that variable in the function
* Attempting to assign the variable before declaring it global inside the function will cause an error; so, declare global just before usage—even   if it's at the end

23Q.What is Hexa, Octa, Ordinary, Complex in python?
In Python, Hexa (Hexadecimal), Octa (Octal), Ordinary (Decimal), and Complex refer to different numeric types and representations used in code and computations.
* Hexadecimal:
Represents numbers using base 16 , Uses digits 0-9 and letters A-F
* Octal
Represents numbers using base 8, Uses digits 0-7 only.
* Decimal
Represents numbers using base 10, Uses digits 0-9.
* Complex
Represents complex numbers with real and imaginary parts.

24Q. what is openAI ? give some examples.
OpenAI is an artificial intelligence research organization and company that develops state-of-the-art AI models, including natural language processing models like GPT.
* Advanced AI models for language understanding and generation
* Tools for computer vision, code generation, chatbots, and more
* APIs for developers to build intelligent applications easily.

(2 Sep 2025)

25Q. What is the factorial of '0'?
* The factorial of zero (0!) is defined as 1.
* This is a special mathematical convention that makes formulas and combinatorics work consistently.
* if n=0, that multiplication has no numbers in it. The result of an empty product is defined as 1.

26Q. What is palindrome and their examples?
A palindrome is a word, phrase, number, or sequence that reads the same backward as forward.
Examples of palindromes:
Words: madam, level, refer.
Numbers: 121, 1331.
Phrases (ignoring spaces, punctuation, and capitalization): * nurses run
                                                            * A man, a plan, a canal, Panama!

27Q.What is the meaning of purge?
The word “purge” has a few related meanings depending on context, but in general it means to remove or get rid of something unwanted or harmful.

28Q. What is conflict? how do solve conflict?
A conflict is a disagreement, clash, or struggle between two or more people, groups, or ideas.It usually happens when people have different opinions, needs, values, or goals.
steps to solve conflict:
* Identify the cause
* Listen actively
* Stay calm and respectful
* Find common ground
* Brainstorm solutions
* Agree and take action
  
(3 Sep 2025)

29Q. Understand the difference between exception and error?
ERROR:
* Errors are serious problems that occur in a program and usually cannot be handled by the program itself.
* It caused by issues external to the program or low-level problems.
* Errors are not expected to be caught or recovered from using exception handling (like try-except).

EXCEPTION:
* Exceptions are problems that occur during the execution of a program but can be handled in the code.
* It caused by logical mistakes or invalid operations.
* Exceptions are expected and recoverable using try-except blocks.

30Q. How many types of exceptions are there in python?
There are two types of exceptions:
1.Built-in Exceptions
These come with Python by default. They are further divided into two groups:
a. Standard Exceptions (commonly used)
-ZeroDivisionError → division by zero
-ValueError → invalid value (e.g., converting "abc" to int)
-IndexError → invalid list index
-KeyError → invalid dictionary key
-TypeError → operation on wrong data type
-FileNotFoundError → file doesn’t exist
-IOError → input/output operation failure
-AttributeError → invalid attribute access
-ImportError / ModuleNotFoundError → module not found
b.System-related Exceptions (less common, more serious)
-MemoryError → out of memory
-RecursionError → too much recursion
-SystemExit → program exit
-KeyboardInterrupt → user stops program (Ctrl+C)
2.User-defined Exceptions
You can create your own exceptions by inheriting from the Exception class.

31Q. Is 'none' datatype or not in python?
* In Python,'None' is not a data type by itself,instead it is a special constant in Python.
* It represents the absence of a value or null value, and the data type of None is called NoneType.

32Q. How can you fix input function and can able to access the boolean and null values?
* The input() function in Python always returns a string,that means if you type True, False, or None, Python treats them as strings ("True", "False", "None") instead of boolean/null values.
solution:
1. eval()
   It can evaluate the input as Python code.It is unsafe if you take input from untrusted users, because it can execute malicious code.
2. custom conversion logic
   Instead of eval(), you can manually check and convert.

33Q. What are the five pillars of OOPS?
there are five main pillars (sometimes you’ll see 4, but the 5th is often added in modern teaching):
1. Encapsulation-Wrapping data (attributes) and methods (functions) together into a single unit (class).
2. Abstraction-Hiding the complex implementation details and showing only the essential features.
3. Inheritence-One class (child) can derive properties and methods from another class (parent).
4. polymorphism-The ability to take many forms (same method name behaving differently).
5. Association-Defines how objects are related to each other (Has-A relationship).

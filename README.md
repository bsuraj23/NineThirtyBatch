# NineThirtyBatch
30 july

1Q) what is history of phthon?
 Developed by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands.
 Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility.
 Python  is one of the most popular languages.
 Widely used in AI, machine learning, data science, web development, automation, and scientific computing.

 2Q) what is open source and close source?
 Open Source in Python means the source code of Python and its libraries is freely available to the public.
 Anyone can view, use, modify, and distribute it without paying.
 Python itself is open source, licensed under the Python Software Foundation License (PSFL).
 Examples:
 Instagram → uses Django (open-source framework) for its web app.
 Netflix → uses Flask, Pandas, NumPy for recommendations and data handling.
 YouTube → uses TensorFlow (open-source AI library) for video suggestions.
 Spotify → uses Scikit-learn, TensorFlow for music recommendations
 Close source
 closed source means software, libraries, or applications built with Python but whose source code is not available to the public.
 You can use the software, but you cannot see, edit, or share its original code.

 3Q) what is complilation?
 Compilation is the process of converting human-readable code (source code) into machine-readable code (binary/executable) so that the computer can understand and run it.
 Done by a program called a Compiler.
 Without compilation, the computer cannot directly understand our code.

 4Q) what is famous web appliacations?
 A Web Application is a software or program that runs in a web browser.
 It uses the internet and can be accessed on computers, mobiles, or tablets.
 Unlike normal apps, you don’t need to install them; you just open them through a browser (like Chrome, Edge, or Firefox).
 Examples:
 Google Apps
   Gmail (email service)
   Google Docs, Sheets, Drive (online office & storage)
   
 Social Media
   Facebook
   Instagram
   Twitter (X)
   
Entertainment
   YouTube (video sharing)
   Netflix (movies & shows)
   Spotify (music streaming)
   Shopping / E-commerce
   
Communication
   WhatsApp Web
   Zoom
   Google Meet
   Microsoft Teams
   Education & Learning

5 August

5Q) what are the five different commands?
 commands are instructions we give to the computer to perform a specific task.
 They are written as functions, keywords, or statements.
 When we write a command in Python and run it, Python’s interpreter executes that instruction
 print() Command
         Definition: Used to display messages, values, or results on the screen.
 print() → Displays output.
 
 input() Command
         Definition: Allows the user to give input (like text or numbers) while the program is running.
 input() → Takes input from the user.
 
 len() Command
       Definition: Returns the number of items in a string, list, or any collection.
 len() → Counts length of a string/list.

 type() Command
        Definition: Shows the data type of a value or variable (like integer, string, float).
 type() → Shows data type. 

 Help() Command
        Definition: Displays help/documentation about Python functions, classes, or modules. 
 Help() → Shows documentation/help.

 6Q) what is features of phyton?
  * Simple & Easy to Learn
 Python has a very clean and simple syntax, like plain English.
 Example: print("Hello") is easier than other programming languages.
 
  * Interpreted Language
 Python does not need compilation; code runs line by line using the interpreter.
 Open Source & Free
 Anyone can download, use, and even modify Python freely.
 
  * Cross-Platform
 Works on Windows, Mac, Linux, and even mobile devices without changing code.
 
  * Object-Oriented
 Supports concepts like classes and objects for better code structure.

7Q) is char exist in phthon or not ?
❌ No, Python does not have a special char (character) data type like C, C++, or Java.
✅ In Python, a character is just a string of length 1.

11 August 

8Q) what is product base company?
A Product-Based Company is a company that builds and sells its own products (software or hardware) to customers.
Their main focus is on developing products like applications, tools, or platforms.
They don’t just provide services to others, but create products that are used worldwide.
Examples:
* Google → Uses Python for search, AI, and cloud products.
* Microsoft → Uses Python in Azure, Office 365, and AI tools.
* Facebook (Meta) → Uses Python for backend, AI, and data analysis.
* Instagram → Entirely built using Django (Python framework).

9Q) How do cpmpiled and run it phthon?
Python is an interpreted language, but internally it also does a kind of compilation before running.
* Compilation to Bytecode (.pyc)
  When you run the code, Python first compiles it into bytecode (low-level instructions).
  This bytecode is stored in __pycache__ folder as .pyc files.

* Python Virtual Machine (PVM) Executes
  The PVM (Python Virtual Machine) reads the bytecode and executes it line by line.
  That’s why Python is called an interpreted language.

* IDEs (Integrated Development Environments)
  Run Python in tools like PyCharm, VS Code, Jupyter Notebook, IDLE.

13 August

10Q) Different blw compilation and interpreter?
compilation 
  Compilation is the process of translating the entire program (source code) into machine code (binary) before execution.
  Done by a compiler.
  After compilation, the program can run many times without recompiling.
  Example Languages: C, C++, Java
  
Interpreter 
   Interpretation is the process of translating and executing the program line by line directly.
   Done by an interpreter.
   Stops immediately when it finds the first error.
   Example Languages: Python, JavaScript, Ruby

11Q) Understand about vs code and the shorts cuts?
 Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft.
 Supports many programming languages (Python, C, Java, JavaScript, etc.).
 * Lightweight but powerful, with features like:
 * Syntax highlighting
 * Auto-completion
 * Debugging tools
 * Extensions for Python, Git, AI tools, etc.
 * Runs on Windows, macOS, and Linux.
 * Developers love it because it’s simple, fast, and customizable.

 Useful VS Code Shortcuts
🔹 General
   Ctrl + Shift + P → Open Command Palette (access all commands).
   Ctrl + P → Quick Open (search and open any file).
   Ctrl + S → Save file.
   Ctrl + Shift + S → Save As.
   Ctrl + N → New file.
   Ctrl + W → Close current file.

12Q) Different blw single and equal?
1. Single Equal (=)
2. Definition: In Python, a single equal sign (=) is called the assignment operator.
3. Use: It is used to assign a value to a variable.

1. Double Equal (==)
2. Definition: In Python, a double equal sign (==) is called the equality comparison operator.
3. Use: It is used to compare two values. If both are equal, it returns True, otherwise False

18 August

13Q) Explore the database technologies?
A database is a structured collection of data that can be stored, managed, and retrieved easily.
Python provides many ways to connect and work with databases — from simple file-based storage to large relational and NoSQL systems.

Examples in Python:
* SQLite
Built-in with Python (sqlite3 module).
Lightweight, file-based DB (good for small apps).

* MySQL
Popular open-source DB for web apps.
Python library: mysql-connector-python or PyMySQL.

* PostgreSQL
Advanced open-source SQL database.
Python library: psycopg2.

* Oracle Database / MS SQL Server
Enterprise-level databases.
Python libraries: cx_Oracle, pyodbc.

19 August

14Q) Different blw remove and discard?
1. remove()
2. Definition: Deletes an element from a set.
3. Error Handling: If the element is not present, it raises an error (KeyError).

1. discard()
2. Definition: Deletes an element from a set.
3. Error Handling: If the element is not present, it does NOT raise an error.
   
28 August

15Q) Different blw doubles codes and single codes?
Both single quotes and double quotes are used to represent string literals.
They are almost the same, but the main difference is in convenience when writing strings.

1. Single Quotes (' ')
   Used to create string values.
   Handy when the string contains double quotes inside.
  
2. Double Quotes (" ")
   Also used to create string values.
   Handy when the string contains single quotes inside.
   
   




     



  
  

  


 


 
       
 
 
       
         

         
         
 
 


  DATE:18-08-2025

"Explore the technologies of the data base"
 types of data bases
 -->relational databases:stored data in tables,use sql,best for structured data and transactions
   ex:my sql,oracle
 -->No sql databases:Schema-less,handle unstructured data,scalable for bigdata & real time apps.
   ex:Mongo db,cassandra 
 -->New sql databases:Combination of sql and no sql,scalable but with strong transactions
   ex:Cockroach db,google spanner
 -->In memory databases:Stored data in ram for very fast access
   ex:Redis,SAP HANA
 -->cloud databases:Managed in the cloud ,easy scaling,less maintenance
   ex:AWS rds,Google cloud sql 
 -->specialized databases:Graph Db-relationships,Time-series DB-Sensors,Vector DB-Semantic search


 Difference between HTTP and HTTPS
 
 HTTP:
 -->hyper text transfer protocol
 -->Not secure and data sent as plaintext 
 -->Uses port 80
 -->Vulnerable to hackers,man in the middle attack
 -->This http feature used in simple websites,blogs,public info

 HTTPS:
 -->Hyper text transfer protocol secure
 -->Secure data is encrypted  using SSL/TLS
 -->Uses port 443
 -->Protects data from eavesdropping & tampering
 -->This https feature used in banking,shopping,login systems 



 Different types of browsers:
 1)Google chrome:Best for speed and extensions
 2)Mozilla firefox:Best for privacy and opensource fans
 3)Microsoft edge:Best for windows integration
 4)Apple safari:Best for apple devices
 5)Opera:Best for built-in tools,VPN and ad-blocker
 6)Brave:Best for privacy and ad-free experience



 RAG-(How it works)
 A modern ai/ml technique often implemented using python libraries like LangChain,Haystack or Liamaindex and the abbreviation of RAG is Retrieve Augmented Generation
 -->How it works:
 Retrieve:Pulls relevant information from an external knowledge base 
 Augment:Adds that information to the user's query
 Generate:Passes it to a Large Language Model(LLM) tp produce a more accurate answer

Difference between single quotes(') and double quotes(")
 single quotes
-->No difference both represent string
-->Use when string contains double quotes inside
-->Less used for doc strings

 Double quotes
-->No difference both represent string
-->Use when string contains single quotes inside
-->Preferred for doc strings (or) documentation


What is Self?
-->Self is the instance the method is acting on the "current object".its just a name but by convention we write self
-->In python,methods are just functions defined inside the class.when you call obj.method(X),
Python actually does: Class.method(obj,x).So the instance (obj) is passed as the first argument.we capture it with self.self.value means the value belonging to this particular object& self is used to keep your code readable and idiomatic
for example to use:
-->Inside instance methods to read/write the object's data
-->In init to set up per-object attributes
-->In properties to access instance data




What is Inavlid Cache?
An invalid cache means the stored data is outdated,corrupted or no longer matches the actual data in memory or datbase,cache data that has become outdated,incorrect or unusable so it should not be used anymore 



Globals and loclas(Attributes)
Global:
-->Declared outside of all the functions
-->Can be accessed anywhere in the program
--->Exists as long as the program is running
-->Cannot be changed inside a function without using the global keyword
-->Stored in global memory (program-level)

Local:
-->Declared inside a function
-->Can only be accesed inside the function where it is created
-->Exists only until the function finishes the execution
-->Can be freely modified inside the function
-->stored in stack memory(function-level)


# 🐍 Python Interview Questions (Beginner → Intermediate)

## 🔹 Beginner Level (Basics & Core Concepts)

1. What are Python’s key features? Why is it called an interpreted language?
Ans: Easy to learn,and dynamically typed,object oriented,and large functional support,large standard library and third party modules.python code is executed by the python interpreter line by line instead of being compiled into machine code first
2. Difference between **Python 2 and Python 3**?
Ans:In python 2 strings are ascii by default      In python 3 strings are unicode by default 
    python 2 is no longer supported               python 3 is present and future

3. Explain **indentation** in Python. What happens if indentation is incorrect?
Ans:Indentation:Spaces or tabs at the beginning of  a line to define code blocks.If indentation is incorrect python raises an indentation error

4. What are Python **keywords**? Can you use them as variable names?
Ans:If,for,def,class,return.No we can't use 
5. Difference between **list, tuple, set, and dictionary**. Give examples.
Ans:List                       Set                                Tuple
  1)List is mutable         1)Set is mutable                    1)Tuple is immutable
  2)it allows duplicates    2)it doesn't allows duplicates      2)it allows duplicates
  3)it is ordered           3)it is unordered                   3)it is ordered
6. What is the difference between **mutable and immutable** data types?
Ans:mutable can be changed after creation   Immutable cannot be changed after creation
  EX:List,Set,Dictionary                    Ex:int,float,string
7. Explain **== vs is** operator in Python with examples.
Ans: == compares the values(checks equality)       compares identities
8. What is the difference between **append() vs extend()** in lists?
  Ans:append:adds the whole object x as single element
      Extend:adds elements of iterable one by one
9. Explain **shallow copy vs deep copy** in Python.
Ans:Shallow copy:Copies outer object,but references inner object
    Deep Copy:Copies both outer and inner objects
10. How does Python handle **memory management** (Garbage collection)?
Ans:Python uses reference counting-keeps track of how many reference an object has.Garbage collector cleans upn unused objects

Interview question 2
8. What are Python’s built-in data types?
Ans:Python built in data types
  1)Numeric types
  2)Sequence types
  3)text types
  4)Set types
  5)Mapping types
  6)Boolean types
  7)Binary types

10. How are integers and floats stored in memory in Python?
    Ans:  Integers                                             Floats
         1)Stored in binary (0s & 1s)                         1)Stored in IEEE 754 (64-bit format)
         2)No size limit                                      2)Fixed 64-bit size
         3)Exact values                                       3)Approximate values
         4)Whole numbers will be used in use case             4)Decimal / fractional numbers will be used in use case
16. What is the difference between `break`, `continue`, and `pass`?
Ans:break stops the loop, continue skips current iteration, pass does nothing
Code:for i in range(5):
    if i == 2:
        break     
    print(i)

17) What is the purpose of the `else` clause in loops?
Ans:Runs only if loop finishes without break.
Code:for i in range(3):
    print(i)
else:
    print("Loop finished without break")

18) How does `enumerate()` work in Python?
Ans:Gives (index, value) pairs while iterating.
Code:for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
19) How do you iterate through a dictionary?
Ans:Use .keys(), .values(), or .items().
Code:my_dict = {"a": 1, "b": 2}
for k, v in my_dict.items():
    print(k, v)
20)How do you use list comprehension in Python?
Ans:Short way to create lists.
Code:squares = [x**2 for x in range(5)]
print(squares)  

    

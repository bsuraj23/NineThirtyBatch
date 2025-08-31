TASKS
(05-Aug-2025)
Q1.Give any 5 commands of command prompt on windows.
   mkdir foldername:used to create one more directories
   del filename:deletes a file
   dir:list all files and folders in the current directory
   cd foldername:changes current directory to specified folder
   ipconfig:displays the computer's ip configuration
Q2.Give 5 features of python.
  ->easy to learn and readable syntax
  ->interpreted and dynamically typed
  ->high level language
  ->portable
  ->free and open source
Q3.Find if char datatype exist in python or not?
   No, Python does not have a separate char (character) data type. Instead, any single character is represented as a string of length 1, which belongs to the "str" type.
   
(13-08-2025)
Q1.Difference between compiler and interpreter?
   compiler-A compiler is a program that translates the entire source code (written in a high-level language) into machine code  in one go, before execution.
   interpreter-An interpreter processes the source code line by line and executes it immediately without producing a separate executable file. Some interpreters convert source code to an intermediate form (like        bytecode) and execute that.
Q2.Difference Between = and ==?
   "=" is used to assign the value to any variable
   "==" is used to compare the variable to the value
Q3.How many types of range functions are there to use in loops?
   range(stop):with a single argument it starts from 0 till not including stop before the stop ex:for i in range(3) it gives values 0,1,2
   range(start,stop):it starts from start and end before the stop ex:for i in range(1,6) it gives the values 1,2,3,4,5
   range(start,stop,step):it starts from start and ends before the stop and increments by step ex:for i in range(1,15,3) it gives the values 1,4,7,10,13 if we want to count from backwards we will use for i in                                        range(15,1,-3) it gives the values 15,12,9,6,3.

(14-08-2025)
Q1.Difference between break and continue statements?
   Break:break terminates the program according to the condition ex:for i in range(1,15) if we give the condition if i==5 then break then the output will be 1,2,3,4.
   Continue:continue only skips the value given in the condition and print the remaining as same ex:for i in range(1,7) if the condition is if i==3 then itb gives the output 1,2,4,5,6.
Q2.Explore about %d,%f,%s,%t,/n?
   %d used for the digit values,%s used for string values,%t used for tab values,/n is used for new line or next line,%f used for floating point numbers.
   
(18-08-2025)
Q1.Explore about http and https?
   HTTP:http stands for hypertext transfer protocol,HTTP transmits data in plaintext, meaning that anyone monitoring the connection like on public Wi-Fi can intercept and read messages, including sensitive                information.
   HTTPS:https stands for HyperText Transfer Protocol Secure. it’s simply http layered over TLS (Transport Layer Security), sometimes referred to as SSL, its older counterpart it is very safe.
Q2.Find how does a search engine works?
   Search engines use automated bots (crawlers or spiders) to scan the web and discover new or updated content, which they then index into a massive searchable database. When you enter a query, the engine quickly    searches this index and uses ranking algorithms to return the most relevant results based on relevance, quality, and other factors.

(19-08-2025)
Q1.What is the difference between list and set?
   LIST:Insertion order-preserved
        Duplicates-allowed
        Mutable-yes
   Set:Insertion order-not preserved
       Duplicates-not allowed
       Mutable-yes
       But Sets can only contain hashable (immutable) elements like numbers, strings, or tuples,they cannot include unhashable types like lists or dictionaries.
Q2.Difference between remove and discard?
   remove()-Attempts to remove the specified element from the set. If the element does not exist, it raises a Keyerror.
   discard()-Attempts to remove the specified element from the set. If the element does not exist, it does nothing no error is thrown.
Q3.What is the purpose of the symbol :: in sets?
   In Python,:: is part of extended slice syntax for sequences like lists, tuples, and strings. It appears as start:stop:step
   ex:my_list=[0,1,2,3,4,5,6] print my_list[::3] it gives the output 0,3,6.

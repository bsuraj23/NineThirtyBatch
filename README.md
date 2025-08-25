# NineThirtyBatch
Assigned tasks (05-Aug-2025)

Q1.Give any 5 commands of command prompt on windows.
del:Delete one or more files
move:Moves one or more files from one directory to another directory
erase:Deletes one or more files
call:calls one batch program from another
color:Sets defalt foreground and background colors.

Q2.Give 5 features of python.
*Extensive Standard Library
*Object oriented and functional
*Supports multiple programming 
*Embedded and Extensible
*Large community support

Q3.Find if char datatype exist in python or not?
*char datatype dosenot exist in python because char is holding a single alphabet or a letter.
*So, in python string holds single alphabet,letter and also group of alphabets which is called as a string.

(13-08-2025)

Q1.Difference between compiler and interpreter?
   Compiler checks the entire code at once and gives the errors present in the respective lines 
   Interpreter check the code line by line and if there is any error in line no.2 then the interpreter terminates the program and gives the error.
   In python the compiler firstly converts source code into intermediate code which is called as byte code and interpreter converts the intermediate code into machine level.
   
Q2.Difference Between = and ==?
   = is used to assign values to a particular variable
   == is used to check if the  value is present in the variable or not.

   
Q3.How many types of range functions are there to use in loops?
   range(stop)	Starts at 0, ends before stop	for i in range(5): print(i)	0 1 2 3 4
   range(start, stop)	Starts at start, ends before stop	for i in range(2, 6): print(i)	2 3 4 5
   range(start, stop, step)	Starts at start, ends before stop, increments by step	for i in range(1, 10, 2): print(i)	1 3 5 7 9
   range(start, stop, -step)	Counts backward	for i in range(10, 0, -2): print(i)	10 8 6 4 2
   range(0)	No numbers produced	for i in range(0): print(i)	(no output)
   range(negative, positive)	Works with negative start values	for i in range(-3, 3): print(i)	-3 -2 -1 0 1 2
   range(start, stop, large_step)	Skips values according to step size	for i in range(0, 20, 5): print(i)	0 5 10 15

(14-08-2025)

Q1.Difference between Break and continue?
   Break terminates the program according to the condition give. ex: if i==2 then break; here at the value i=2 the break statement terminates the program.
   Continue skips the value given in the condition and executes the next values. ex: if i=5 then continues skips the value 5 and executes 1,2,3,4,6,7,....
   
Q2. explore about %d, %s, %t, /n?
   The %d, %s, %t, /n are the conversion specifiers where,
   %d is used at digit values
   %s is used at string values
   %t is used for tab values
   /n is used for new line or next line

   (18-08-2025)

Q1.What is S in https?
   HTTPS stands for Hyper Text Transfer Protocol Secure 
   HTTP is used for transferring data between a web browser and a website.
   HTTPS adds a security layer using SSL/TLS encryption, which ensures data privacy and protection from attackers.

Q2.How a Search engine Works?
   Search engines use web crawlers (bots/spiders) that go from page to page on the internet.
   They follow links, read the content, and collect data.
   Example: If a crawler visits a blog, it also checks all links on that blog to discover new pages.

(19-08-2025)

Q1.What is the difference between List and Set?
   LIST                                                                                SET
   An ordered collection of elements                                                   An unordered collection of unique elements
   Maintains the order of insertion                                                    Does not maintain any order (unordered)
   Allows duplicate elements                                                           Does not allow duplicates
   Mutable – you can add, remove, or change elements                                   Mutable – you can add or remove elements, but elements must be immutable (no lists inside a set)

Q2.What is the difference between remove() and discard()?
   remove() → Removes an element, but raises an error if it’s missing.
   discard() → Removes an element, but does nothing if it’s missing.

Q3.What is the purpose of the symbol :: in set()?
   start → where slicing begins (default = 0).
   stop → where slicing ends (default = end of sequence).
   step → the interval between elements (default = 1). ex: sequence[start : stop : step]

(25-08-2025)

Q1.Check Whether tuple is mutable or not?
   Tuple is imutable. But it becomes mutable when tuple is combimed in List or set or dictionary.


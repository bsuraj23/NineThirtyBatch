
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

 


#Dictionary 
print("Welcome to Nandy's Food court")
print("This Dictionary consists of menu of food items ")
#Dictionary creation 
d={'Menu':'Nonveg,Veg,Deserts','price':500,'offers':'available','timings':'10AM-10PM'}
print(d)
#Accessing Dictionary Elements
print(d['Menu'])
print(d.get('timings'))
#Basic Operations
print(len(d))
print('Menu' in d)
print('Nonveg' in d['Menu'])  
#Adding 
d['location']='Ameerpet'
print(d)  
#Updating
d['price']='1000'
print(d)
d.update({'offers':'not available'})
print(d)
#Deleting
d.pop('location')
print(d)
#Methods can be performed on Dictionaries
print(d.keys())  #returns the keys of the dictionary
print(d.values())  #returns the values of the dictionary
print(d.items())  #returns the key-value pairs of the dictionary
print(d.copy())
d.popitem() #removes the last inserted key-value pair
print(d)
print(dict.fromkeys(['a','b'],0)) #creates a new dictionary with keys from the given iterable and values set to 0
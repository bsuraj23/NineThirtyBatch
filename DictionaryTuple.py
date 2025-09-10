
#Dictionary creation with Tuple
d2={'Nonveg':{'Mutton':('biryani','curry','pulao','staters')}}
#Accessing elements
print(d2['Nonveg']['Mutton'])  
#Adding Elements
# Tuples are immutable, so we cannot add elements directly. 
# However, we can convert it to a list, add elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])
mutton_list.append('salad')  # Add into Mutton list 
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)
#Removing
# Tuples are immutable, so we cannot remove elements directly.  
# However, we can convert it to a list, remove elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])
mutton_list.remove('salad')  # Remove 'salad' from Mutton list
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)           
#Updating
# Tuples are immutable, so we cannot update elements directly. 
# However, we can convert it to a list, update elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list[0] = 'updated_biryani'  # Update the first element
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)   
# Searching
print('biryani' in d2['Nonveg']['Mutton'])  # Check if 'biryani' is in Mutton tuple
print(d2['Nonveg']['Mutton'].index('curry'))  # Get the index of 'curry'
# Sorting       
# Tuples are immutable, so we cannot sort them directly. 
# However, we can convert it to a list, sort it, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list.sort()  # Sort the Mutton list in ascending order
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)       
# Reversing
# Tuples are immutable, so we cannot reverse them directly.
# However, we can convert it to a list, reverse it, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list.reverse()  # Reverse the Mutton list
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)
# Copying
d2_copy = d2['Nonveg']['Mutton']  # Create a copy of the Mutton tuple
print(d2_copy)  # Display the copied tuple  
#tuple methods
print(d2['Nonveg']['Mutton'].count('biryani'))  # Count occurrences of 'biryani'
print(d2['Nonveg']['Mutton'].index('curry'))  # Get the index of 'curry'
print(len(d2['Nonveg']['Mutton']))  # Get the length of the Mutton tuple
print(d2['Nonveg']['Mutton'].count('staters'))  # Count occurrences of 'staters'    

#Dictionary creation with Tuple
d2={'Nonveg':{'Mutton':('biryani','curry','pulao','staters')}}
#Accessing elements
print(d2['Nonveg']['Mutton'])  
#Adding Elements
# Tuples are immutable, so we cannot add elements directly. 
# However, we can convert it to a list, add elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])
mutton_list.append('salad')  # Add into Mutton list 
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)
#Removing
# Tuples are immutable, so we cannot remove elements directly.  
# However, we can convert it to a list, remove elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])
mutton_list.remove('salad')  # Remove 'salad' from Mutton list
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)           
#Updating
# Tuples are immutable, so we cannot update elements directly. 
# However, we can convert it to a list, update elements, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list[0] = 'updated_biryani'  # Update the first element
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)   
# Searching
print('biryani' in d2['Nonveg']['Mutton'])  # Check if 'biryani' is in Mutton tuple
print(d2['Nonveg']['Mutton'].index('curry'))  # Get the index of 'curry'
# Sorting       
# Tuples are immutable, so we cannot sort them directly. 
# However, we can convert it to a list, sort it, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list.sort()  # Sort the Mutton list in ascending order
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)       
# Reversing
# Tuples are immutable, so we cannot reverse them directly.
# However, we can convert it to a list, reverse it, and convert it back to a tuple.
mutton_list = list(d2['Nonveg']['Mutton'])  
mutton_list.reverse()  # Reverse the Mutton list
d2['Nonveg']['Mutton'] = tuple(mutton_list)  # Convert back to tuple
print(d2)
# Copying
d2_copy = d2['Nonveg']['Mutton']  # Create a copy of the Mutton tuple
print(d2_copy)  # Display the copied tuple  
#tuple methods
print(d2['Nonveg']['Mutton'].count('biryani'))  # Count occurrences of 'biryani'
print(d2['Nonveg']['Mutton'].index('curry'))  # Get the index of 'curry'
print(len(d2['Nonveg']['Mutton']))  # Get the length of the Mutton tuple
print(d2['Nonveg']['Mutton'].count('staters'))  # Count occurrences of 'staters'    


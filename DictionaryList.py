
#Dictionary creation with List
d1={'Nonveg':{'Chicken':['biryani','Curry','Pulao','Staters']}}
#Accessing elements
print(d1['Nonveg']['Chicken'])  # Accessing Chicken list    
#Adding Elements
d1['Nonveg']['Chicken'].append('salad')  # Add into Chicken list
print(d1)
d1['Nonveg']['Chicken'].extend(['soup', 'fries'])  # Add multiple elements into Chicken list
print(d1)
d1['Nonveg']['Chicken'].insert(2, 'noodles')  # Insert 'noodles' at index 2
print(d1)
#Removing  
d1['Nonveg']['Chicken'].remove('salad')  # Remove 'salad' from Chicken list
print(d1)
d1['Nonveg']['Chicken'].pop()  # Remove the last element from Chicken list
print(d1)
del d1['Nonveg']['Chicken'][1]  # Delete the element at index 1
print(d1)
#updating 
d1['Nonveg']['Chicken'][0] = 'updated_biryani'  # Update the first element
print(d1)
#searching
print('biryani' in d1['Nonveg']['Chicken'])  # Check    if 'biryani' is in Chicken list
print(d1['Nonveg']['Chicken'].index('Pulao'))  # Get the index of 'Curry'
#Sorting 
# Sorting the Chicken list
d1['Nonveg']['Chicken'].sort()  # Sort the Chicken list in ascending order          
print(d1)
# Reversing the Chicken list    
d1['Nonveg']['Chicken'].reverse()  # Reverse the Chicken list
print(d1)
#copying
d1_copy = d1['Nonveg']['Chicken'].copy()  # Create a copy of the Chicken list
print(d1_copy)  


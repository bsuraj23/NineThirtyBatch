#Dictionary creationwith Set
d={'veg':{'Paneer':{'biryani','curry','pulao','saters'}},
   'price':{350,200,250,150}}
#Adding Elements
d['veg']['Paneer'].add('salad')   # Add into Paneer set
d['price'].add(199)
d['price'].update([210,220])    #Add into price set
print(d)
#Removing
d['price'].remove(210) 
print(d)
d['price'].discard(220)
print(d)
#We can also use pop
#Set operations beetween two dictionaries
d1={'vegies':{'all':{'pulao','biryani','salad','sambar'}}}
#union operation
u=(d['veg']['Paneer']|d1['vegies']['all'])
print(u)
#intersection operation
i=(d['veg']['Paneer']&d1['vegies']['all'])
print(i)
#difference operation
dif=(d['veg']['Paneer']-d1['vegies']['all'])
print(dif)
#set methods
print(d['veg']['Paneer'].issubset(d1['vegies']['all']))  # Check if Paneer is subset of all
print(d['veg']['Paneer'].issuperset(d1['vegies']['all']))  # Check if Paneer is superset of all
print(d['veg']['Paneer'].isdisjoint(d1['vegies']['all']))  # Check if Paneer is disjoint with all
print(d['veg']['Paneer'].copy())  # Create a copy of the Paneer set
print(d['veg']['Paneer'].clear())  # Clear the Paneer set            
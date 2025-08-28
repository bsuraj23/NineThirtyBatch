print("Hello people!...welcome to chinni's mobile store")
print("here we have new smart phones  store available....")
#dictionary creation
dict1={'types':{'Basic phones':1,'Smart phones':2}}
print(dict)
#Basic phones
Basic={'d':['Nokia','Samsung']}
print(Basic)
#Smart phones
Smart={'d':['Samsung GalaxyS','Apple','Xiaomi'',OnePlus','Oppo','Vivo'',realme']}
print(Smart)
#basic operators
#membership operator
print("Features"not in dict1)
#comparision operator
print(Basic!=Smart)
#merge operator
dict2={'types':{'Ear phones':3}}
print(dict1|dict2)
#methods
#Accesing values
print(dict1.get("Basic phones"))
print(dict2.keys())
#removing
dict1.clear()
print(dict1)
#copying
dict3=dict1.copy()
print(dict3)
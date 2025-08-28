#dictionary creation with list
dList1={'Basic phones':['Nokia','Samsung']}
dList2={'Smart phones':['Apple','Xiaomi','OnePlus']}
#list operators
#append
dList1['Basic phones'].append('Itel')
print(dList1)                   #adding Itel to dList1
#Insert
dList2['Smart phones'].insert(1,'samsung galaxyS')
print(dList2)                   #inserting samsung galaxyS at index 1
#remove
dList2['Smart phones'].remove('OnePlus')
print(dList2)                   #removes OnePlus from smart phones
#pop
dList1['Basic phones'].pop()
print(dList1)                   #deletes last element 
#length
print(len(dList2))                   #gives length of apple
#clear
dList1['Basic phones'].clear()
print(dList1)                   #clear the list
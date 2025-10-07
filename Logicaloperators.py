print("Logical Operators")
#Logical operator - AND
sun="Its very hot and clear sky (yendakotting chemata putting)"
moon="I'm mr.cool (Chandamama)"
print(len(sun))
print(len(moon))
if(len(sun)==57 and len(moon)==24):
    print("And logical operator is completed")
else:
    print("And logical operator is not completed")
#Logical operator - OR
if(len(sun)==10 or len(moon)==2):
    print("OR logical operator is not completed")
else:
    print("OR logical operator is completed")
#Logical operator - NOT
if( not (len(sun)>len(moon))):
    print("NOT logical operator is not completed")
else:
    print("NOT logical operator is completed")
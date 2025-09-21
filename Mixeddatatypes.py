#creating a list of mixed datatypes and returning the dicionary which contains count of datatypes in list
def count_datatypes(list):
    type_count={"int":0,"bool":0,"float":0,"str":0}
    for i in list:
        if isinstance(i,bool):
            type_count["bool"]+=1
        elif isinstance(i,int):
            type_count["int"]+=1
        elif isinstance(i,float):
            type_count["float"]+=1
        elif isinstance(i,str):
            type_count["str"]+=1
    return type_count
mixed_list=[1,0.9,5.6,"Akhila","ch",True,5,0,False]
print(count_datatypes(mixed_list))

def remove_duplicates(list):
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates([2,4,2,7,18,24,7,9]))

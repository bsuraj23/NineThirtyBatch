def remove_duplicates(list):
    result=[]
    for str in list:
        if str not in result:
            result.append(str)
    return result
print(remove_duplicates([2,4,2,7,18,24,7,9]))
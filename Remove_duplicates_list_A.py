def removing_duplicates(lst):
    unique_list=[]
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
print(removing_duplicates([2,2,3,5,3,6,7,1,5]))

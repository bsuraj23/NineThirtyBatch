def flatten_list(nested):
    single_lst=[]
    for item in nested:
        if isinstance(item,list):
            single_lst.extend(flatten_list(item))
        else:
            single_lst.append(item)
    return single_lst
lst=[[2, 4], [7, [9, 12]], [15, 19]]
print(flatten_list(lst))
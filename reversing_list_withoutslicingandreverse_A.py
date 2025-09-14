def reversing_list(list):
    left=0
    right=len(list)-1
    while left<right:
        list[left],list[right]=list[right],list[left]
        left=left+1
        right=right-1
my_list=[2,3,5,6,3,9,11,5,12]
reversing_list(my_list)
print(my_list)
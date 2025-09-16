def reverse_in_place(lst):
    left=0
    right= len(lst)-1
    while left < right:
        lst[left],lst[right]=lst[right],lst[left]
        left += 1
        right -= 1
my_list=[1,2,3,4,5,6,7]
reverse_in_place(my_list)
print(my_list)
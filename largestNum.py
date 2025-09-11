#largest number from list

numb=[36,42,32,9,20]
large=numb[0]
for num in numb:
    if num > large:
        large=num
        print(large)
# Top half of the diamond
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        print("*", end=" ")
    print()

# Bottom half of the diamond
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(1, i * 2):
        print("*", end=" ")
    print()
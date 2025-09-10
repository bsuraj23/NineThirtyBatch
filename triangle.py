rows = 5
col=5
#for temp in range(1, rows + 1):        
    #print("*"  * temp )
for i in range(1,rows+1):
    for j in range(1,col+1):
        if(i==j or i==3 and j==2 or i==4 and j==2 or i==4 and j==3 or i==5 or j==1):
            print("*", end=" ")   
        else:
            print(" ", end=" ")
    print()          




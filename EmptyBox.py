#Empty box
a=11
for i in range(1,a+1):
    if i==1 or i==a:
        for j in range (1,a+1):
            print("*",end=" ")
    elif i%2==1:
        for k in range(1,a+1):
            if k==1 or k==a:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
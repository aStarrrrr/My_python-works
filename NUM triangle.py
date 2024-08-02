limit = int(input("ENTER THE RANGE : "))
for i in range(1,limit+1):
    k=1
    for j in range(1,i+1):
        print(k , end=" ")
        k+=1
    print("\r")
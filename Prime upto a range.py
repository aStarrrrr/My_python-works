limit= int(input("Enter the limit upto which we have to print the prime numbers : "))
for i in range(2,limit+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        print(i,end=" ")
        print("\r")
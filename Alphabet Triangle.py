limit = int(input("Enter the range to print :"))
for i in range(0,limit):
    order=ord('A')
    for j in range(0,i+1):
        print(chr(order),end=" ")
        order+=1
    print("\r")
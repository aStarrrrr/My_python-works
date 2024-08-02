multi = int(input("Which table have to be print : "))
limit = int(input("Enter the limit upto which the table have to be printed :"))
i=1
for i in range(limit+1):
    print(i," x ",multi," = ",i*multi)
    i=+i
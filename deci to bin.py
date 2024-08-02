def decitobin(n):
    if n==0:
        return 0
    bin=""
    while n>0:
        remainder=n%2
        bin=str(remainder)+bin
        n=n//2
    return bin
deci=int(input("Enter the decimal: "))
print(decitobin(deci))
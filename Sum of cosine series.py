import math
def cosine(x,n):
    cosx=1
    sign=-1
    for i in range(2,n,2):
        pi=(22/7)
        y=x*(pi/180)
        cosx += sign * (y ** i) / math.factorial(i)
        sign=-sign
        return cosx
x=int(input("Enter the angle:"))
n=int(input('Enter the number of terms:'))
cosine(x,n)
print(cosine)
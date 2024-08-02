def perimeter(r):
    perm=round(2*r*(22/7))
    print("Perimeter of the circle is : ",perm,"cm")
def area(r):
    area=(22/7)*(r**2)
    print("Area of the circle is : ",area,"cm^2")
r=int(input("Enter the area of the circle :"))
perimeter(r)
area(r)
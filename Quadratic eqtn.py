# import math
# print("Equation : ax^2+bx+c=0")
# a=int(input("Enter value for a : "))
# b=int(input("Enter value for b : "))
# c=int(input("Enter value for c : "))
# disc=math.sqrt((b**2)-4*a*c)
# if disc>0:
# 	x1=(-b+disc)/(2*a)
# 	x2=(-b-disc)/(2*a)
# 	x1=round(x1,2)
# 	x2=round(x2,2)
# 	print("There are two real and unequal solutions to the quadratic equation,x1=",str(x1),"x2=",str(x2))
# elif disc==0:
# 	x1=(-b)/(2*a)
# 	x1=round(x1,2)
# 	print("There is a single real solution to the quadratic equation,x1=",str(x1))
# elif disc<0:
# 	print("Solution to the quadratic equation is complex.")


import math
print("ax^2+bx+c=0")
a =int(input("Enter the value of a :"))
b =int(input("Enter the value of b :"))
c =int(input("Enter the value of c :"))
result=(b^2)-(4*a*c)
if(result>0):
    root1=(-b+math.sqrt(result))/(2*a)
    root2=(-b-math.sqrt(result))/(2*a)
    print(root1,roo2)
elif(result==0):
    root=-b/(2*a)
    print(root)
elif(result<0):
    real=-b/(2*a)
    complexpart=math.sqrt(-result)/(2*a)
    root1=(real,complexpart)
    root2=(real,complexpart)
    print(root1,root2)
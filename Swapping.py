a = int(input("Enter the roll number of Abhinand Shaji :"))
k = int(input("Enter the roll number of Karthika R : "))

print("type of  first roll no :",type(a))
print(type(k))

print("We are going to interchange the roll numbers !")

temp = a
a = k
k = temp

print("Roll number of Abhinand Shaji : "+str(a))
print("Roll number of Karthika R : "+str(k))
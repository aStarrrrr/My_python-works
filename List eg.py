a = ["Abhinand","Karthika","Afsana","Gopika","Rakendu"]
print(a)

print(a[1])

print(a[0:2])

print(a[-1])

print(a[3:])

print(a[-2])

print(a[0:3])

a = a+["Amrutha","Gowri"]
print(a)

a.append("Kukku")
print(a)

a.append(input("Enter the name to add : "))
print(a)

print("The length of the list is : ",len(a))

print("The type is : ",type(a))

#Another way to create a list
k=list(("Acha","Mommy","Kannan"))
print(k)

k[0]="Achan"
print(k)

k.insert(2,"Gopu")
print(k)
# limit = int(input("Enter the limit to check odd or even : "))
# even=0
# odd=0
# for i in range(1,limit+1):
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("Count Of Even Numbers :",even)
# print("Count Of Odd Numbers :",odd)

num=int(input("Enter the range : "))
even=0
odd=0
for i in range (1,num+1):
	if(i%2==0):
		even+=1
	else:
		odd+=1
print("Even Numbers between 1 and ",str(num),":",str(even))
print("Odd Numbers between 1 and ",str(num),":",str(odd))


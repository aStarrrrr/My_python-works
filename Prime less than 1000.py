# for i in range(2,1001):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#     if(flag==0):
#         print(i,end=" ")
#         print("\r")
#

#
# for i in range(2,1001):
# 	flag=0
# 	for j in range(2,i):
# 		if(i%j==0):
# 			flag=1
# 	if(flag==0):
# 		print(i,end=" ")

















print("PRIME NUMBER LESSER THAN 1000")
for i in range(2,1001):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        print(i,end=" ")
        print("\r")
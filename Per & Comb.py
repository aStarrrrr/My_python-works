def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
def perm(n,r):
    permutation=int(fact(n)/fact(n-r))
    print("resu;t is :",permutation)
def comb(n,r):
    combination=int(fact(n)/(fact(n-r)*fact(r)))
    print("result is :",combination)

n=int(input("enter num of ele:"))
r=int(input("Enter num of selec or arrangmnt:"))
perm(n,r)
comb(n,r)









#
# def fact(n):
# 	f=1
# 	for i in range(1,n+1):
# 		f*=i
# 	return f
# def perm(n,r):
# 	perm=int(fact(n)/fact(n-r))
# 	print("Number of Permutations : ",str(perm),"ways")
# def comb(n,r):
# 	comb=int(fact(n)/(fact(n-r)*fact(r)))
# 	print("Number of Combinations : ",str(comb))
# n=int(input("Enter total number of elements : "))
# r=int(input("Enter number of elements to be selected/arranged : "))
# ch=int(input("ENTER-1.Permutation 2.Combination : "))
# if ch==1:
# 	perm(n,r)
# elif ch==2:
# 	comb(n,r)
# else:
# 	print("ERROR!")
#
#
#

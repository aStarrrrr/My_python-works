inputfile=open("test.txt","r")
numbers=[]
for line in inputfile:
    wordlist=line.split()
    for word in wordlist:
        numbers.append(float(word))
numbers.sort()
midpoint=len(numbers)//2
if len(numbers)%2==1
    print(number[midpoint])
else:
    print(number[midpoint]+number[midpoint-1]/2)

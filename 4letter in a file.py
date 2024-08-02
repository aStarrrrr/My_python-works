inputfile=open("test.txt","r")
count=0
for line in inputfile:
    wordlist=line.split()
    for word in wordlist:
        if len(word)==4:
            count+=1
print("Count is : ",count)
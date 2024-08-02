import datetime
start = datetime.datetime.now()
print(datetime.datetime.now())
print(datetime.date.today())

print(start.strftime("%d/%m/%Y"))

print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

x = datetime.datetime(2004 ,5 ,6)
y = datetime.datetime(2004,1,26)

print(x)
print(y)

dif = x-y
print("Difference : ",dif)

print("Finding the time taken by the program to complete :\n")
end = datetime.datetime.now()

time_taken = end-start
print("Time taken to complete :",time_taken)
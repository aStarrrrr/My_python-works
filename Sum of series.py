def sumseries(x,n):
    sum=1
    for i in range(1,n):
        term=(x**i)/math.factorial(i)
        sum+=term
    return sum
x=
n=
result=sumseries(x,n)
print(result)
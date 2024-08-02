deno=10
try:
    result=(40/deno)
    print(result,"\nTry block executed")

except ZeroDivisionError:
    print("The number can't be divided by ZERO!")

print("The Programm Executed And Ended")
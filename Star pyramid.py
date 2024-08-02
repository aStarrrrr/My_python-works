"""
n=1
while(n<=10):
    print("*")
    n=n+1

def print_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)
"""

limit = int(input("Enter the number of rows to print the star : "))
for i in range(limit):
    for j in range(limit):
        print("*")
        print("\r")
        print("\n")

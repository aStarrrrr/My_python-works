# def is_armstrong(number):
#     str_num = str(number)
#     num_digits = len(str_num)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
#     return sum_of_powers == number
#
#
# number = int(input("Enter a number: "))
#
#
# if is_armstrong(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")
#

def armstrong(number):
    strnumber=str(number)
    strlength=len(strnumber)
    sumvalue=sum(int(digit)**strlength for digit in strnumber)
    return sumvalue==number
number=int(input("Enter the number : "))

if armstrong(number):
    print("Is armstrong")
else:
    print("Not armstrong")
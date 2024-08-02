def palindrome(s):
    s=s.replace(" ","").lower()
    return s == s[::-1]
str=input("Enter the string : ")
if palindrome(str):
    print("Palindrome")
else:
    print("Not Palindrome")

# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]
# input_string = input("Enter a string: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

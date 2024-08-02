# Function to check if a number is palindrome
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    # Reverse the string
    reversed_num_str = num_str[::-1]
    # Check if the original string is equal to the reversed string
    return num_str == reversed_num_str

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

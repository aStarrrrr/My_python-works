print("HOTEL KARTHIKA")
print("MENU")
print("1.Biriyani\n 1.1.Chicken\n 1.2.Beaf\n 1.3.Mutton\n 1.4.Fish\n 1.5Prons\n2.Meals\n3.Porotta\n4.Masala Dosa\n5.Ghee Roast\n6.Beaf\n 6.1.Curry\n 6.2.Roast\n 6.3.Fry\n 6.4.Chilly Beaf\n 6.5.BDF\n7.Chicken\n 7.1.Curry\n 7.2.Roast\n 7.3.Fry\n 7.4.Chilly Chicken\n 7.5.Broast\n8.Mandhi\n 8.1.Chicken\n 8.2.Beaf\n 8.3.Mutton\n 8.4.Alfam")

"""
a = []
for i in range(limit):
    a.append(int(input("Enter the sl numbers : ")))
print("Your order is : ")
for i in range(8):
    if (a[i] == 1):
        print("Biriyani")
    else:
        print("Enter a valid food item")
"""

ord = float(input("Place Your Order By entering the seriel numbers.."))

if (ord == 1.3):
    print("You ordered Mutton Biriyani ")
elif (ord ==1.1):
    print("You ordered Chicken Biriyani ")
elif (ord ==1.2):
    print("You ordered Beaf Biriyani ")
elif (ord ==3):
    print("You ordered Porotta ")
elif (ord ==4):
    print("You ordered Masala Dosa")
elif (ord ==5):
    print("You ordered Ghee Roast")
elif (ord ==6.1):
    print("You ordered Beaf Curry")

else:
    print('You are a fooooooooool!! ')
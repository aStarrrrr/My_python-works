class First:
    def display(self):
        print("FIRST")
class Second:
    def display(self):
        print("SECOND")
class Third(First,Second):
    def display_third(self):
        print("Third")

x = Third()

x.display_third()
x.display()

#the order of revolution of mrthofe "Third"
#methode resolution order

print(Third.mro())
class First:
    def display_first(self):
        print("First Class")
class Second(First):
    def display_second(self):
        print("Second Class")
class Third(Second):
    def display_third(self):
        print("Third Class")

x = First()
y = Second()
z = Third()

z.display_first()
z.display_second()
z.display_third()